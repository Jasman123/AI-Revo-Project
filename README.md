# 🤖 Insight AI

An intelligent, document-aware AI assistant powered by Retrieval-Augmented Generation (RAG) using local LLM models (llama3.2). Insight AI lets you upload documents, build a searchable vector knowledge base, and have natural language conversations grounded in your own data — all wrapped in a clean Streamlit interface.

---

## ✨ Features

- 📄 **Document Ingestion** — Load and process documents from the `documents/` folder
- 🧠 **Vector Search** — Supports both **ChromaDB** (local) as vector stores
- 🔗 **Graph-based Reasoning** — Uses a LangGraph-powered pipeline (`graph_model.py`) for structured, multi-step LLM reasoning
- 📑 **PDF Report Generation** — Export insights and responses as PDF documents
- 🐳 **embeddings** — tokenazation words

---

## 🗂️ Project Structure

```
Insight_AI/
├── main.py                     # Main application entry point
├── llm.py                      # LLM setup and configuration
├── retriever.py                # RAG retriever logic
├── graph_model.py              # LangGraph reasoning pipeline
├── build_vectore.py            # Build ChromaDB vector store
├── generate_pdf.py             # PDF export functionality
├── chroma_db/                  # Local ChromaDB vector store
├── documents/                  # Source documents for ingestion
├── logs/                       # Application logs
├── requirements.txt            # Python dependencies
├── .gitignore                  # ignorance of files
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- An OpenAI API key (or compatible LLM provider)
- Ollama model (llama3.2 & mxbai-embed-large)

### 1. Clone the Repository

```bash
git clone https://github.com/Jasman123/AI-Revo-Project
cd AI-Revo-Project
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Add Your Documents

Place your source documents (PDFs, text files, etc.) inside the `documents/` folder.

### 4. Build the Vector Store

**Using ChromaDB (local):**
```bash
python build_vectore.py
```
### 5. Run the App

```bash
fastapi dev main.py  
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| backened | [FastApi](https://fastapi.tiangolo.com/) |
| LLM Orchestration | [LangChain](https://www.langchain.com/) + [LangGraph](https://langchain-ai.github.io/langgraph/) |
| Vector Store | [ChromaDB](https://www.trychroma.com/) |
| LLM | Ollama |

---

## 📄 License

This project is open source. Feel free to use, modify, and distribute.

---

## 🙋‍♂️ Author

**Jasman** — [GitHub](https://github.com/Jasman123)
