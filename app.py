import streamlit as st
import pandas as pd
import os
from datetime import datetime
from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_classic.chains import create_retrieval_chain
from langchain_community.vectorstores import Chroma
from langchain_groq import ChatGroq

st.set_page_config(page_title="Enterprise Support & Analytics Platform", layout="wide")

@st.cache_resource
def load_rag_system():

    from langchain_community.embeddings import HuggingFaceEmbeddings
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    vector_db = Chroma(persist_directory = "./chroma_db", embedding_function=embeddings)

    llm = ChatGroq(
        groq_api_key=st.secrets["GROQ_API_KEY"],
        model_name="llama-3.1-8b-instant",
        temperature=0.2
    )

    system_prompt = (
        "You are an expert customer support assistant. Use the following pieces of retrieved "
        "context to answer the user's question. If you don't know the answer, say that you don't "
        "know. Keep the answer concise.\n\n"
        "Context:\n{context}"
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}"),
    ])

    retriever = vector_db.as_retriever(search_kwargs={"k": 2})
    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)
    
    return rag_chain

qa_system = load_rag_system()

LOG_FILE = "support_analytics_logs.csv"

def log_interaction(query, category):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_data = pd.DataFrame([[timestamp, query, category]], columns = ["Timestamp", "Query", "Category"])

    if not os.path.exists(LOG_FILE):
        new_data.to_csv(LOG_FILE, index=False)
    else:
        new_data.to_csv(LOG_FILE, mode = 'a', header=False, index= False)

def categorize_query(query):
    q= query.lower()
    if "refund" in q or "return" in q or "broken" in q or "damage" in q:
        return "Refunds & Returns"
    elif "shipping" in q or "delivery" in q or "days" in q or "order" in q:
        return "Shipping & Delivery"
    elif "premium" in q or "member" in q or "discount" in q or "rupees" in q:
        return "Memberships & Rewards"
    else:
        return "General Inquiry"

st.title("AI support center & Executive Analytics Platform")
st.markdown("---")

tab1,tab2 = st.tabs(["💬 Customer Support Assistant", "📊 Executive Analytics Dashboard"])

with tab1:
    st.header("Ask our enterprise knowledge base")
    st.write("Our local context-aware LLM will instantly extract answers from secure company policies.")

    user_query = st.text_input("Type your query here:")

    if st.button("Submit Query"):
        if user_query.strip() != "":
            with st.spinner("AI is retrieving company records and analyzing..."):

                result = qa_system.invoke({"input": user_query})
                response = result["answer"]

                category = categorize_query(user_query)
                log_interaction(user_query, category)

                st.markdown("### 📋 AI Assistant Response:")
                st.success(response)
        else:
            st.warning("Please enter a valid query before pressing submit.")
with tab2:
    st.header("Real-time operational metrics")
    st.write("This analytics layer monitors operational friction points using live user interaction logs.")

    if os.path.exists(LOG_FILE):
        df_logs = pd.read_csv(LOG_FILE)

        col1,col2,col3 = st.columns(3)

        with col1:
            st.metric("Total Interacted Inquiries", len(df_logs))
        with col2:
            most_common_cat = df_logs["Category"].mode()[0] if not df_logs.empty else "N/A"
            st.metric("Top Support Friction Driver", most_common_cat)
        with col3:
            st.metric("System Availability Status", "100% (local Node)")
        
        st.markdown("---")

        st.subheader("Distribution of support volume by category")
        category_counts = df_logs["Category"].value_counts()
        st.bar_chart(category_counts)

        st.subheader("Raw Transaction Logs (Auditable Event Stream)")
        st.dataframe(df_logs.sort_values(by= "Timestamp", ascending= False), use_container_width = True)
    else:
        st.info("No query logs detected yet. submit a few questions in the Chatbot tab to populate live analytics data!")