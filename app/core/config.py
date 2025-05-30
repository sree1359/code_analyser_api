import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

def get_llm():
    load_dotenv()  # Loads from .env automatically
    groq_api_key = os.getenv('GROQ_API_KEY')
    if not groq_api_key:
        raise ValueError(
            "GROQ_API_KEY environment variable is required. Get free key from https://console.groq.com/keys")

    return ChatGroq(
        groq_api_key=groq_api_key,
        model_name="llama3-8b-8192",  # Free models: llama3-8b-8192, mixtral-8x7b-32768, gemma-7b-it
        temperature=0
    )
