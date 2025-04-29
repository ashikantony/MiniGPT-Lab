# 🧠 MiniGPT Lab

Chat with your personal notes and journals — powered by a mini GPT model!

## 🚀 Features
- Upload your own `.txt` files (journals, notes, tips).
- Finetune a distilled GPT (Tiny-GPT2) on your data.
- Live chat interface with a smart assistant.
- Voice assistant ready (coming soon!).
- Docker-ready, Hugging Face deployable.

## 🛠 Tech Stack
- FastAPI (backend API)
- Streamlit (frontend chat)
- Transformers (Tiny-GPT2 model)
- VS Code + Docker + GitHub Actions

## 📦 How to Run

**Backend API**
```bash
uvicorn main:app --reload
