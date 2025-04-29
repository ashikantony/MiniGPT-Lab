from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import os
from backend.extractor import process_dataset
from backend.trainer import train_model
from backend.chatbot import load_model, generate_response

app = FastAPI()

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "dataset"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Load or initialize model
model = load_model()

@app.post("/upload/")
async def upload(file: UploadFile = File(...)):
    file_location = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_location, "wb") as f:
        f.write(await file.read())
    return {"status": "File uploaded", "filename": file.filename}

@app.post("/process/")
async def process():
    process_dataset(UPLOAD_DIR)
    return {"status": "Dataset processed"}

@app.post("/train/")
async def train():
    global model
    model = train_model("data/processed")
    return {"status": "Training completed"}

@app.get("/chat/")
async def chat(q: str):
    response = generate_response(model, q)
    return {"response": response}
