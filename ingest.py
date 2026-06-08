import os
import re
from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter

DOCS_DIR = Path(__file__).parent / "documents"
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200


def clean_text(text: str) -> str:
    # Strip HTML tags
    text = re.sub(r"<[^>]+>", "", text)
    # Collapse multiple blank lines into one
    text = re.sub(r"\n{3,}", "\n\n", text)
    # Strip leading/trailing whitespace per line
    text = "\n".join(line.strip() for line in text.splitlines())
    return text.strip()


def source_name(filepath: Path) -> str:
    """Return a clean source label from the filename, e.g. 'a-review-of-life-in-rosie'."""
    return filepath.stem


def load_and_chunk_documents():
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        length_function=len,
    )

    all_chunks = []

    md_files = sorted(DOCS_DIR.glob("*.md"))
    md_files = [f for f in md_files if f.name != ".gitkeep"]

    for filepath in md_files:
        raw = filepath.read_text(encoding="utf-8")
        cleaned = clean_text(raw)

        chunks = splitter.create_documents(
            texts=[cleaned],
            metadatas=[{"source": source_name(filepath)}],
        )
        all_chunks.extend(chunks)
        print(f"  {filepath.name}: {len(chunks)} chunks")

    return all_chunks


if __name__ == "__main__":
    print(f"Loading documents from: {DOCS_DIR}\n")
    chunks = load_and_chunk_documents()
    print(f"\nTotal chunks: {len(chunks)}")

    # Preview the first chunk so you can verify metadata and content
    if chunks:
        sample = chunks[0]
        print(f"\n--- Sample chunk (source: {sample.metadata['source']}) ---")
        print(sample.page_content[:300])
