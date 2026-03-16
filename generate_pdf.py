from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter, RecursiveCharacterTextSplitter

from pathlib import Path

def load_pdf(file_path: str) -> list:
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    loader = PyPDFLoader(str(path))
    docs = loader.load()
    for i in range(len(docs)):
        docs[i].page_content = ' '.join(docs[i].page_content.split())
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )
    pages_splitter = text_splitter.split_documents(docs)
    return pages_splitter

# if __name__ == "__main__":

#     file_path = "documents\\data_information.pdf"
#     pages_splitter = load_pdf(file_path)
#     # print(f"Total chunks: {len(pages_splitter)}")

#     for i, page in enumerate(pages_splitter):
#         print(f"Chunk {i + 1}:\n{page.page_content}\n{'-' * 40}")

