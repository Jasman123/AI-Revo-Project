from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
import os
from generate_pdf import load_pdf
from uuid import uuid4

PDF_PATH = "documents\\data_information.pdf"
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
    uuids = [str(uuid4()) for _ in range(len(documents))]
    vector_store = Chroma.add_documents(
        documents,
        ids=uuids,
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
    

# if __name__ == "__main__":
#     vector_store = get_vector_store(embeddings)

#     retriever = vector_store.as_retriever(
#     search_type="mmr", search_kwargs={"k": 2, "lambda_mult": 0.5}
#         )

#     for doc in retriever.invoke("What is the main topic of the document?"):
#         print(doc.page_content)

#     vector_store = Chroma(
#     collection_name="pdf_chunks",
#     persist_directory=CHROMA_DIR,
#     embedding_function=embeddings,
#     )
#     documents = load_pdf(PDF_PATH)
#     uuids = [str(uuid4()) for _ in range(len(documents))]


#     # for doc, uuid in zip(documents, uuids):
#     #     vector_store.add_documents(documents=[doc], ids=[uuid])

#     vector_store.add_documents(documents=documents, ids=uuids)