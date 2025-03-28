from fastapi import Body, Depends, FastAPI, HTTPException
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from openai import OpenAI
from langchain_openai import OpenAIEmbeddings
import os
from fastapi.middleware.cors import CORSMiddleware
import chromadb
from models import Logs
from database import get_db
from sqlalchemy.orm import Session
from database import engine
import models
from models import ChatRequest

app= FastAPI()
models.Base.metadata.create_all(engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

load_dotenv()
openai_key=os.getenv("OPENAI_AI_KEY")

chroma_client = chromadb.PersistentClient(path="./knowledge_base")
collection_name = "FAQs"
collection = chroma_client.get_or_create_collection(collection_name)


def retriever(query):
    embedding_model = OpenAIEmbeddings(api_key=openai_key)
    query_embedding = embedding_model.embed_query(query)
    results= collection.query(
        query_embeddings=query_embedding,
        n_results=3
    )
    return results

past_conversation = []
@app.post("/chat-completions")
def chat_completions(request: ChatRequest,db: Session = Depends(get_db)):
    client = OpenAI(api_key=openai_key)
    try:
        retrieved_results = retriever(request.query)
        context = "\n".join(retrieved_results["documents"][0])
        formatted_history = []
        if past_conversation:
            for msg in past_conversation[-5:]:  
                formatted_history.append({"role": msg["role"], "content": msg["text"]})

        formatted_history.append({"role": "user", "content": request.query})
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a customer support agent. Answer the user queries with given knowledge base and implement a feedback mecchanism if user queries answercd is not available in the knowledge base"},
                {"role": "system", "content": f"Context: {context}"},
                *formatted_history
            ],
            temperature=0.5,
        )
        answer = response.choices[0].message.content
        
        if answer:
            log = Logs(query=request.query, response=answer)
            db.add(log)
            db.commit()
            db.refresh(log)
        return answer
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
