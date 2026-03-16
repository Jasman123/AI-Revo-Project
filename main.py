from fastapi import FastAPI
import uvicorn

from graph_model import build_graph
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage, RemoveMessage


app = FastAPI()
@app.post("/ask")
async def ask_question(question: str):  
    graph = build_graph()
    messages = [
        SystemMessage(content="You are a helpful assistant that answers questions based on provided documents."),
        HumanMessage(content=question)
    ]
    response = graph.invoke({"messages": messages})
    
    return {
        "answer": response["messages"][-1].content,
        "retrieved_documents": response["documents"],
        "similarity_scores": response["similarity_scores"],
        "total_tokens": len(' '.join(response["documents"]).split()) + len(question.split())
    }

@app.get("/")
async def root():
    return {"message": "Welcome to the PDF Question Answering API. Use the /ask endpoint to ask questions about the PDF document."} 

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)