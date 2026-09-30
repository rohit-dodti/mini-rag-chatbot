from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

print("API key loaded:", groq_api_key is not None)

llm = ChatGroq(
model="openai/gpt-oss-120b",
    temperature=0.2,
    api_key=groq_api_key
)

response = llm.invoke(
    "What is RAG? Explain in 2 sentences."
)

print(response.content)