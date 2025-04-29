import streamlit as st
import requests

st.set_page_config(page_title="MiniGPT Lab", layout="wide")
st.title("🧠 MiniGPT Lab - Chat with Your Mind!")

BACKEND = "http://localhost:8000"

# Sidebar: Upload & Train
st.sidebar.header("Upload Files & Fine-tune Model")
uploaded_file = st.sidebar.file_uploader("Upload a .txt file", type=["txt"])

if uploaded_file:
    files = {"file": (uploaded_file.name, uploaded_file, "text/plain")}
    response = requests.post(f"{BACKEND}/upload/", files=files)
    if response.status_code == 200:
        st.sidebar.success("File uploaded successfully!")

if st.sidebar.button("Process Dataset"):
    res = requests.post(f"{BACKEND}/process/")
    st.sidebar.success(res.json()["status"])

if st.sidebar.button("Fine-Tune Model"):
    res = requests.post(f"{BACKEND}/train/")
    st.sidebar.info(res.json()["status"])

# Main Chat
st.header("💬 Chatbot")
question = st.text_input("Ask something...")

if st.button("Send"):
    if question:
        res = requests.get(f"{BACKEND}/chat/", params={"q": question})
        st.markdown(f"**Bot:** {res.json()['response']}")
