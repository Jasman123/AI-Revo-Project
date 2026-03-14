import os
from graph_model import build_graph
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage, RemoveMessage

messages = [
    SystemMessage(content="You are a helpful assistant that answers questions based on provided documents.")
]

if __name__ == "__main__":
    graph = build_graph()
    user_input = input("Enter your question: ")
    messages.append(HumanMessage(content=user_input))
    response = graph.invoke({"messages": messages})
    print(response)