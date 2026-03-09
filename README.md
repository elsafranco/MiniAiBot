# AI Document Assistant

## Project Overview
AI Document Assistant is a Streamlit-based mini chatbot that allows users to upload a document and interact with it using AI. The app can answer questions about the uploaded file and generate a short summary of its main ideas. This project demonstrates a simple but meaningful AI task by applying document-based question answering and summarization.

## Features
- Upload a PDF, TXT, or CSV file
- Ask questions about the uploaded document
- Generate a concise summary of the document
- Restrict responses to information found in the uploaded file

## Model Name and Source
This project uses the **Google GenAI API** with the **Gemini model**.

Source: Google Generative AI Python SDK

## Rationale for Model Selection
I selected the Gemini model because it is easy to integrate into a Python and Streamlit application, supports document-based interactions, and can generate both summaries and question-answer responses. It was a practical choice for building a lightweight AI assistant that demonstrates applied AI concepts without requiring a more complex setup.

## API Usage
The application uses the Google GenAI API to process uploaded documents and respond to user prompts. When a user uploads a file, the app sends it to the API and stores a reference to that document. The chatbot then uses that uploaded file together with the user’s question or summarization prompt to generate a response. The app displays the response in a Streamlit chat interface and keeps the conversation history in session state.

## Responsible AI Reflection
This project highlights both the usefulness and limitations of generative AI. While the chatbot can provide fast summaries and answer questions about an uploaded document, it may still misunderstand information or generate incomplete responses. Because of this, users should verify important outputs instead of relying on the model alone. There is also the issue of bias, since AI systems can reflect patterns or limitations from their training data and system design. To encourage more responsible use, this chatbot is instructed to answer only from the uploaded file and to say when information is not available. Even with that safeguard, human judgment is still necessary when interpreting results.


## How to Run the Project
1. Clone or download the project files
2. Install dependencies:
   ```bash
   pip install streamlit google-genai python-dotenv