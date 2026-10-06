# Mini RAG Chatbot

A PDF question-answering application built with Python, FastAPI,
Streamlit, FAISS and Groq.

## Overview

The application retrieves relevant passages from a sample PDF and
passes them to an LLM alongside the user's question.

The prompt instructs the model to answer using the retrieved context
and acknowledge when the document does not contain the answer.
This is a prompt instruction, not a guarantee of factual accuracy.

## How It Works

1. Load `data/sample.pdf` using PyPDFLoader.
2. Split the document into chunks of 500 characters with 100-character overlap.
3. Generate embeddings using `sentence-transformers/all-MiniLM-L6-v2`.
4. Create an in-memory FAISS vector index.
5. Retrieve the top three matching chunks for each question.
6. Send the question and retrieved context to Groq.
7. Display the answer in Streamlit.

## Technology Stack

- Python
- FastAPI and Uvicorn
- Streamlit
- LangChain
- Hugging Face sentence embeddings
- FAISS
- Groq

## Project Structure

- `backend/main.py` — FastAPI routes and request model
- `backend/rag.py` — PDF loading, embeddings, retrieval and generation
- `frontend/app.py` — Streamlit interface
- `data/sample.pdf` — document used for question answering
- `requirements.txt` — application dependencies
- `test_groq.py` — manual Groq connection check

## Setup

Run all commands from the repository root.

### 1. Clone the repository

```bash
git clone https://github.com/rohit-dodti/mini-rag-chatbot.git
cd mini-rag-chatbot
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Windows Command Prompt:

```cmd
.venv\Scripts\activate.bat
```

macOS / Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure the API key

Create a `.env` file in the repository root:

```text
GROQ_API_KEY=your_groq_api_key_here
```

Keep this file private. Do not commit API keys.

The code currently requests `openai/gpt-oss-120b` through Groq.
Access depends on the provider's current model availability and account limits.

### 5. Start the backend

```bash
python -m uvicorn backend.main:app --reload
```

API documentation: http://127.0.0.1:8000/docs

On startup, the application loads the PDF and builds the FAISS index.
The first run may download the embedding model.

### 6. Start the frontend

Open a second terminal, activate the same environment, and run:

```bash
python -m streamlit run frontend/app.py
```

Open the URL displayed by Streamlit and ask questions about the PDF.

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | API welcome message |
| GET | `/health` | Basic status response |
| POST | `/ask` | Answer a document question |

Example request body for `/ask`:

```json
{
  "question": "What are the main topics covered in this document?"
}
```

## Current Limitations

- Uses one fixed PDF; document upload is not implemented.
- Rebuilds the vector index when the backend starts.
- Does not return source citations or page references.
- Has no conversation memory.
- API error handling, request timeouts and automated evaluation are not yet implemented.
- The health endpoint does not check Groq connectivity.
- Retrieved document text is sent to an external LLM provider.

## Planned Improvements

- Source citations and page references
- Document upload
- Persistent vector storage
- API error handling and timeouts
- Retrieval and answer-quality evaluation

## Project Status

Learning and portfolio project under active development.
