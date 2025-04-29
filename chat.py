# 📁 File: backend/chatbot.py

from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer

MODEL_NAME = "sshleifer/tiny-gpt2"

def load_model():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
    return pipeline("text-generation", model=model, tokenizer=tokenizer)

def generate_response(model, prompt):
    responses = model(prompt, max_length=100, do_sample=True)
    return responses[0]["generated_text"]
