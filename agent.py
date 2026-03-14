from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

def create_llm():
    llm = ChatOllama(
        model="llama3.2",
    )
    return llm