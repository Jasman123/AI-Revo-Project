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
    
    for i in response["documents"]:
        print(f"Document: {i}\n with similarity score: {response['similarity_scores'][response['documents'].index(i)]} {"-*40\n"}" )

    print(f"Number of tokens in retrieved documents: {len(' '.join(response['documents']).split())}")
    print(f"Number of tokens in question: {len(user_input.split())}")
    print(f"Total tokens: {len(' '.join(response['documents']).split()) + len(user_input.split())}")
    print(f"Answer: {response['messages'][-1].content}")