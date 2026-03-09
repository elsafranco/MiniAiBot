import streamlit as st
from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

# pip install -U google-genai
# pip install python-dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

st.title("AI Document Assistant")

if "client" not in st.session_state:
    st.session_state.client = genai.Client(api_key=api_key)

with st.sidebar:
    st.header("Setup")
    uploaded_file_ui = st.file_uploader("Upload a file", type=["pdf", "txt", "csv"])

    if uploaded_file_ui and "doc_ref" not in st.session_state:
        with st.spinner("Uploading your document..."):

            # here we need to check file type again
            mime_type = uploaded_file_ui.type

            # writing the bytes to temp file
            with open("temp doc", "wb") as f:
                f.write(uploaded_file_ui.getbuffer())

            doc_ref = st.session_state.client.files.upload(
                file="temp doc",
                config={'mime_type': mime_type}
            )
            st.session_state.doc_ref = doc_ref

            st.session_state.chat = st.session_state.client.chats.create(
                model="gemini-3-flash-preview",
                config=types.GenerateContentConfig(
                    system_instruction="You are a document expert. "
                                       "Answer questions ONLY using uploaded file. "
                                       "If the answer isn't there, say you don't know."
                )
            )
        st.success("Document uploaded successfully!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# summarize button
if "chat" in st.session_state and "doc_ref" in st.session_state:
    if st.button("Summarize Document"):
        summary_prompt = "Summarize the main ideas of this document in 3-5 clear sentences. Only use information from the uploaded file."

        st.session_state.messages.append({
            "role": "user",
            "content": "Summarize this document."
        })

        with st.chat_message("user", avatar="💁‍♀️"):
            st.markdown("Summarize this document.")

        with st.chat_message("assistant"):
            response = st.session_state.chat.send_message(
                message=[st.session_state.doc_ref, summary_prompt]
            )
            st.markdown(response.text)

        st.session_state.messages.append({
            "role": "assistant",
            "content": response.text
        })

prompt = st.chat_input("Ask a question about the uploaded document:")

if prompt:
    if "chat" not in st.session_state:
        st.error("Please upload a document first!")
    else:
        st.session_state.messages.append({
            "role": "user",
            "content": prompt
        })

        with st.chat_message("user", avatar="💁‍♀️"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            response = st.session_state.chat.send_message(
                message=[st.session_state.doc_ref, prompt]
            )
            st.markdown(response.text)

        st.session_state.messages.append({
            "role": "assistant",
            "content": response.text
        })