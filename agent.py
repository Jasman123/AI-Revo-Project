from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

llm = ChatOllama(
    model="llama3.2",
    temperature=0,
)

template = """What year did the first man land on the moon?"""
prompt = PromptTemplate.from_template(template) 

chain = prompt | llm
response = chain.invoke({})
print(response)