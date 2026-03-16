from typing import List
from langgraph.graph import StateGraph, START, END, MessagesState
from langchain_core.prompts import ChatPromptTemplate

from langchain_ollama import OllamaEmbeddings

from build_vectore import get_vector_store
from retriver import create_retriever, similarity_search
from agent import create_llm
from langchain_core.prompts import PromptTemplate

class State(MessagesState):
    documents: List[str]
    similarity_scores: List[float]



def retrieve_documents(state: State) -> State:
    embeddings = OllamaEmbeddings(model="mxbai-embed-large")
    vector_store = get_vector_store(embeddings)

    query = state["messages"][-1].content
    result = similarity_search(vector_store, query)

    document_pages = [doc.page_content for doc, _ in result]
    similarity_scores = [score for _, score in result]

    return {"documents": document_pages,"similarity_scores": similarity_scores}

def generate_answer(state: State) -> State:
    chat = create_llm()
    
    documents = "\n\n".join(state["documents"])
    question = state["messages"][-1].content

    prompt_template = PromptTemplate(
        input_variables=["documents", "question"],
        template="""
Use ONLY the following documents to answer the question.

Documents:
{documents}

Question:
{question}

If the answer is not found in the documents, respond with:
"I don't know."
"""
    )

    prompt = prompt_template.format(
        documents=documents,
        question=question
    )

    response = chat.invoke(prompt)

    return {"messages": state['messages'] + [response], "similarity_scores": state["similarity_scores"], "documents": state["documents"]}

def build_graph():
    graph = StateGraph(State)

    graph.add_node("retrieve_documents", retrieve_documents)
    graph.add_node("generate_answer", generate_answer)

    graph.add_edge(START, "retrieve_documents")
    graph.add_edge("retrieve_documents", "generate_answer")
    graph.add_edge("generate_answer", END)

    return graph.compile()

    