# 🤖 Enterprise Support AI Center & Executive Analytics Platform (RAG)

An enterprise-ready, context-aware Retrieval-Augmented Generation (RAG) system combined with an operational Business Intelligence analytics layer. This application allows a company to securely ingest internal policy documentation, extract factually bounded answers for consumers via high-speed cloud inference, and analyze support metrics through a live administrative dashboard.

## 🔗 Production Links
👉 **[Live Interactive Dashboard](https://dz8ecbab6irzey3xvqxtrj.streamlit.app/)**

---

## 💡 System Architecture & Technical Flow

[User Query] 
   │
   ├──> 1. Vector Search ──> [ChromaDB (HuggingFace Embeddings)] ──> Extracts relevant policy text
   │
   └──> 2. Contextual Prompt ──> [Llama 3.1 Engine via Groq Cloud API] ──> Synthesizes safe answer
   │
   └──> 3. Logging Layer ──> [Pandas ETL] ──> Populates Live BI Dashboard Charts

* **Zero-Hallucination Guardrails:** The LLM architecture is constrained strictly to the context retrieved from the database, preventing it from inventing policies.
* **Cloud-Optimized Footprint:** Designed to bypass the resource constraints of standard cloud environments by decoupling the embedding layer and leveraging high-throughput serverless API routing.

---

## 🛠️ Modern Data Stack & Tooling
* **LLM Engine:** Llama-3.1-8b-instant (Hosted via Groq Cloud for sub-second, production-grade inference)
* **Vector Database:** ChromaDB
* **Embeddings Model:** HuggingFace `all-MiniLM-L6-v2` (Open-source semantic sentence mapping)
* **Framework Orchestration:** LangChain v0.3
* **Data Processing & Analytics:** Pandas & NumPy
* **Deployment & UI:** Streamlit Cloud Architecture & Streamlit Secrets Management

---

## 📂 Project Blueprint
```text
├── app.py                      # Production Web interface and analytics layer
├── ingest.py                   # Vector pipeline database execution script
├── chroma_db/                  # Persisted directory containing mathematical document vectors
├── knowledge_base/
│   └── policies.txt            # Unstructured source text for company business logic
└── requirements.txt            # Explicit cloud environment dependencies
