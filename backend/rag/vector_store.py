import chromadb
from rag.pdf_processor import extract_text_from_pdfs, chunk_text
from rag.embeddings import embed_documents

chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection(name="my_documents")

def store_embeddings():
    text = extract_text_from_pdfs()
    chunks = chunk_text(text)
    print(f"Total chunks created: {len(chunks)}")
    chunk_embeddings = embed_documents(chunks)

    for i, (chunk, embedding) in enumerate(zip(chunks, chunk_embeddings)):
        collection.add(
            ids=[str(i)],
            documents=[chunk],
            embeddings=[embedding],
            metadatas = [{"source": "demo"}]
        )

    print("Embeddings stored succesfully")
