# 🤖 Enterprise Support AI Center & Executive Analytics Platform (RAG)

An enterprise-ready, context-aware Retrieval-Augmented Generation (RAG) system combined with an operational Business Intelligence analytics layer. This application allows a company to securely feed private internal policy documentation to an LLM, extract factually bounded answers for consumers, and analyze customer pain points via a live administrative dashboard.

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
* **Hybrid Layout:** Built using a dual-tab matrix—serving customer inquiries on the frontend while processing event streams for management on the backend.

---

## 🛠️ Modern Data Stack & Tooling
* **LLM Engine:** Llama-3.1-8b-instant (Configured via Groq Cloud infra for sub-second inference latency)
* **Vector Vector DB:** ChromaDB
* **Embeddings Model:** HuggingFace `all-MiniLM-L6-v2` (100% open-source semantic mapping)
* **Framework Orchestration:** LangChain v0.3 Core Components
* **Data Processing & Analytics:** Pandas & NumPy
* **Deployment & UI:** Streamlit Cloud Architecture

---

## 📂 Project Blueprint
```text
├── app.py                      # Production Web interface and analytics layer
├── ingest.py                   # Local vector pipeline execution script
├── chroma_db/                  # Persisted directory containing mathematical document vectors
├── knowledge_base/
│   └── policies.txt            # Unstructured source markdown for company business logic
└── requirements.txt            # Explicit server dependencies
