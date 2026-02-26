import streamlit as st
from chatbot import chat_with_ollama

st.set_page_config(page_title='ChatBot')

st.title("Hello World 🌍")
st.write("Welcome to Streamlit!")

message = st.text_input("Enter your message: ")
if message:
    messages = [{"role": "user", "content": message}]
    reply = chat_with_ollama(messages)
    st.success(reply)