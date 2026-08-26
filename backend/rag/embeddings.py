import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

if not HF_TOKEN:
    raise ValueError(
        "HF_TOKEN not found in .env file. Get a free token from "
        "https://huggingface.co/settings/tokens (Read access is enough) "
        "and add it to your .env file."
    )

EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"
BATCH_SIZE = 32  # keep request payloads small for the free inference tier

# BGE models are trained so the QUERY side gets an instruction prefix but the
# document/passage side does not. Skipping this on the query hurts retrieval
# quality noticeably, so don't drop it.
QUERY_PREFIX = "Represent this sentence for searching relevant passages: "

client = InferenceClient(
    model=EMBEDDING_MODEL,
    provider="hf-inference",  # HF's own serverless inference, not a 3rd party provider
    token=HF_TOKEN,
)


def embed_documents(texts: list[str]) -> list[list[float]]:
    """Embed a list of document chunks (no instruction prefix) via the HF Inference API."""
    embeddings = []
    for i in range(0, len(texts), BATCH_SIZE):
        batch = texts[i:i + BATCH_SIZE]
        batch_embeddings = client.feature_extraction(batch)
        embeddings.extend(batch_embeddings.tolist())
    return embeddings


def embed_query(text: str) -> list[float]:
    """Embed a single search query (with BGE retrieval instruction prefix)."""
    embedding = client.feature_extraction(QUERY_PREFIX + text)
    return embedding.tolist()
