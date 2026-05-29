import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection(name="my_documents")

def retrieve_documents(query, n_results=3):
    query_embedding = model.encode(query)
    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=n_results,
    )

    return results