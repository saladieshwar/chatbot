import streamlit as st
from chatbot import chat_with_ollama

st.set_page_config(page_title='ChatBot')

st.title("Hello, User 🌍")
st.write("Welcome to Chatbot!")

message = st.text_input("Enter your message: ")

if message:
    messages = [
        {"role": "system", "content": "You are a helpful AI assistant."},
        {"role": "user", "content": message}
    ]
    with st.spinner("Thinking..."):
        reply = chat_with_ollama(messages)
    st.write("You: ", message)
    st.write("Assistant: ", reply)