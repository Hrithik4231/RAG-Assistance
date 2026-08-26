import chromadb
from rag.embeddings import embed_query

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection(name="my_documents")

def retrieve_documents(query, n_results=3):
    query_embedding = embed_query(query)
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results,
    )

    return results
