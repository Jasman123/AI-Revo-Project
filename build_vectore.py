from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
import os
from generate_pdf import load_pdf

PDF_PATH = "documents\\big_data_analytics.pdf"
CHROMA_DIR = "chroma_db"
COLLECTION_NAME = "pdf_chunks"


embeddings = OllamaEmbeddings(
    model="mxbai-embed-large",
)

def load_vector_store(embeddings):
    vectore_store = Chroma(
        embedding_function=embeddings,
        persist_directory=CHROMA_DIR,
        collection_name=COLLECTION_NAME,
    )
    return vectore_store

def build_vector_store(documents, embeddings):
    vector_store = Chroma.from_documents(
        documents,
        embedding=embeddings,
        persist_directory=CHROMA_DIR,
        collection_name=COLLECTION_NAME,
    )
    return vector_store

def get_vector_store(embeddings):
    if os.path.exists(CHROMA_DIR):
        return load_vector_store(embeddings)
    
    documnets = load_pdf(PDF_PATH)
    return build_vector_store(documnets, embeddings)
    