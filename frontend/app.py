import streamlit as st
import requests

st.title("Mini RAG Chatbot")

st.write("Ask questions about your document.")

question = st.text_input("Enter your question")

if st.button("Ask"):

    if question:

        response = requests.post(
            "http://127.0.0.1:8000/ask",
            json={"question": question}
        )

        data = response.json()

        st.write("Answer:")
        st.success(data["answer"])