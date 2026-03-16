from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
import os
from generate_pdf import load_pdf
from uuid import uuid4
from langchain_core.documents import Document

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

def add_documents_to_vector_store(vector_store, str):
    document = Document(page_content=str)
    uuid = str(uuid4())
    vector_store.add_documents(documents=[document], ids=[uuid])

def build_vector_store(documents, embeddings):
    uuids = [str(uuid4()) for _ in range(len(documents))]
    vector_store = Chroma(
        embedding_function=embeddings,
        persist_directory=CHROMA_DIR,
        collection_name=COLLECTION_NAME,
    )
    for doc, uuid in zip(documents, uuids):
        vector_store.add_documents(documents=[doc], ids=[uuid])
    return vector_store

def get_vector_store(embeddings):
    if os.path.exists(CHROMA_DIR):
        return load_vector_store(embeddings)
    
    documnets = load_pdf(PDF_PATH)
    return build_vector_store(documnets, embeddings)
    

# if __name__ == "__main__":
#     vector_store = get_vector_store(embeddings)

#     query = "What is the main topic of the document?"

#     retriever = vector_store.as_retriever(
#     search_type="mmr", search_kwargs={"k": 2, "lambda_mult": 0.5}
#         )

#     for doc in retriever.invoke("What is the main topic of the document?"):
#         print(f"Document: {doc.page_content}")
#         print(f"Number of tokens: {len(doc.page_content.split())} \n{'-' * 40}")


    # result = vector_store.similarity_search_with_score(
    #     query, k=3)

    # for doc, score in result:
    #     print(f"Document: {doc.page_content}")
    #     print(f"Number of tokens: {len(doc.page_content.split())} \n{'-' * 40}")
    #     print(f"score: {score}\n{'=' * 40}")

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