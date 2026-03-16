from fastapi import FastAPI
import uvicorn
from datetime import datetime
import tempfile
import os
from uuid import uuid4
import logging

from graph_model import build_graph
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage, RemoveMessage


REQUEST_TIMEOUT_SECONDS = 60
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)


logging.basicConfig(
    filename=os.path.join(LOG_DIR, f"error_{datetime.now().strftime('%Y-%m-%d')}.txt"),
    level=logging.ERROR,
    format="%(asctime)s | %(levelname)s | %(message)s",
)


app = FastAPI()
@app.post("/ask")
async def ask_question(question: str):  
    graph = build_graph()
    messages = [
        SystemMessage(content="You are a helpful assistant that answers questions based on provided documents."),
        HumanMessage(content=question)
    ]

    try :
        response = graph.invoke({"messages": messages})

    except TimeoutError as e:
                  
        logging.error(
            f"TimeoutError: {str(e)}",
            exc_info=True
        )
        return {"message": "⏱️ Request timed out. The model took too long to respond. Please try again."}   

    except Exception as e:
        error_text = str(e)
        logging.error(
            f"Error message :  {error_text}",
            exc_info=True
        )
        return {"message": " ❌ An error occurred while processing your request. Please try again later."}  
    
    return {
        "question": question,
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