import os
from dotenv import load_dotenv
from rag.retriever import retrieve_documents
from google.generativeai.generative_models import GenerativeModel
from google.generativeai.client import configure

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
Google_api_key = os.getenv("GOOGLE_API_KEY")

if not Google_api_key:
    raise ValueError("GOOGLE_API_KEY not found in .env file. Please set it and restart the application.")

configure(api_key=Google_api_key)
llm = GenerativeModel("gemini-2.5-flash")

def generate_response(query):

    results = retrieve_documents(query)


    if results and results['documents']:
        retrieved_docs = results['documents'][0]
    else:
        retrieved_docs = []

    context = "\n".join(retrieved_docs)

    prompt = f"""
    You are a helpful assistant. Use the following context to answer the question:
    Context:
    {context}

    Question: {query}
    Answer: """

    try:
        response = llm.generate_content(prompt)

        if hasattr(response, 'text'):
            return response.text
        return "No response generated"

    except Exception as e:
        print("\nError")
        print(e)

        return f"Error: {str(e)}"