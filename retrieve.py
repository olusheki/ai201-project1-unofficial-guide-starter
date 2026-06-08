from sentence_transformers import SentenceTransformer
import chromadb
from ingest import load_and_chunk_documents

CHROMA_DIR = "./chroma_db"
COLLECTION_NAME = "brandeis_housing"
EMBED_MODEL = "all-MiniLM-L6-v2"


def build_vector_store():
    """Embed all chunks and load them into a local ChromaDB collection."""
    print("Loading and chunking documents...")
    chunks = load_and_chunk_documents()

    print(f"\nLoading embedding model: {EMBED_MODEL}")
    model = SentenceTransformer(EMBED_MODEL)

    client = chromadb.PersistentClient(path=CHROMA_DIR)

    # Wipe and recreate so re-runs don't duplicate data
    client.delete_collection(COLLECTION_NAME) if COLLECTION_NAME in [
        c.name for c in client.list_collections()
    ] else None
    collection = client.create_collection(COLLECTION_NAME)

    texts = [chunk.page_content for chunk in chunks]
    embeddings = model.encode(texts, show_progress_bar=True).tolist()

    collection.add(
        ids=[str(i) for i in range(len(chunks))],
        embeddings=embeddings,
        documents=texts,
        metadatas=[
            {"source": chunk.metadata["source"], "index": i}
            for i, chunk in enumerate(chunks)
        ],
    )

    print(f"\nStored {len(chunks)} chunks in ChromaDB at '{CHROMA_DIR}'.")
    return collection, model


def load_vector_store():
    """Load an existing ChromaDB collection without re-embedding."""
    model = SentenceTransformer(EMBED_MODEL)
    client = chromadb.PersistentClient(path=CHROMA_DIR)
    collection = client.get_collection(COLLECTION_NAME)
    return collection, model


def retrieve(query: str, collection, model, k: int = 5) -> list[dict]:
    """
    Embed the query, search ChromaDB, and return the top-k results.

    ChromaDB's query() returns nested lists — one inner list per query.
    Since we always send a single query, we unwrap index [0] from each field.

    Distance scores: ChromaDB uses L2 (squared Euclidean) distance by default.
      - Lower  = more similar  (0.0 would be a perfect match)
      - Higher = less similar  (roughly > 1.5 means weak relevance)
    For your evaluation step you can use the score to judge retrieval quality:
    flag any result with distance > 1.0 as a potential bad retrieval.
    """
    query_embedding = model.encode([query]).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=k,
        include=["documents", "metadatas", "distances"],
    )

    # Unwrap the outer list (index [0]) — ChromaDB wraps results per query
    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    return [
        {
            "text": doc,
            "source": meta["source"],
            "chunk_index": meta["index"],
            "distance": round(dist, 4),
        }
        for doc, meta, dist in zip(documents, metadatas, distances)
    ]


if __name__ == "__main__":
    collection, model = build_vector_store()

    test_query = "Which halls has the best view of campus?"
    print(f"\nTest query: '{test_query}'\n")

    hits = retrieve(test_query, collection, model)
    for rank, hit in enumerate(hits, 1):
        print(f"--- Rank {rank} | source: {hit['source']} | distance: {hit['distance']} ---")
        print(hit["text"][:300])
        print()
