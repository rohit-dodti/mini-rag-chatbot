from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq

from dotenv import load_dotenv
import os


# -------------------------
# 1. Environment
# -------------------------

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")


# -------------------------
# 2. Load PDF
# -------------------------

loader = PyPDFLoader("data/sample.pdf")
documents = loader.load()


# -------------------------
# 3. Split document
# -------------------------

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = text_splitter.split_documents(documents)


# -------------------------
# 4. Embeddings
# -------------------------

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# -------------------------
# 5. Vector store
# -------------------------

vectorstore = FAISS.from_documents(
    chunks,
    embeddings
)


# -------------------------
# 6. Groq LLM
# -------------------------

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.2,
    api_key=groq_api_key
)


# -------------------------
# 7. RAG function
# -------------------------

def ask_rag(question: str):

    # Retrieve relevant chunks
    results = vectorstore.similarity_search(
        question,
        k=3
    )

    # Combine chunks
    context = "\n\n".join(
        doc.page_content for doc in results
    )

    # Create prompt
    prompt = f"""
You are a document question-answering assistant.

Answer the user's question using only the context provided below.

If the answer cannot be found in the context, say:
"I could not find that information in the document."

Context:
{context}

Question:
{question}

Answer:
"""

    # Ask Groq
    response = llm.invoke(prompt)

    return response.content