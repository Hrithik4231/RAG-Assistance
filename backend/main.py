from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

import shutil
import os

from rag.vector_store import store_embeddings
from rag.rag_pipeline import generate_response

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.get("/")
def home():
    return {"message": "RAG Backend Running"}

@app.post("/upload")
async def upload_pdf(file : UploadFile = File(...)):
    filename = file.filename or "uploaded_file"
    filename = os.path.basename(filename)
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Store embeddings for the uploaded PDF
    store_embeddings()

    return {
        "message": f"{file.filename} uploaded successfully"
        }

@app.get("/chat")
def chat(query: str):
    answer = generate_response(query)
    return {
        "query": query,
        "answer": answer
    }
