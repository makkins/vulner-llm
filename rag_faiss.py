# rag_faiss.py
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

EMBED_MODEL = "all-MiniLM-L6-v2"  # sentence-transformers

class SimpleFaissIndex:
    def __init__(self, dim=384):
        self.embed = SentenceTransformer(EMBED_MODEL)
        self.index = faiss.IndexFlatL2(dim)
        self.docs = []

    def add_documents(self, docs: list[str]):
        embs = self.embed.encode(docs, convert_to_numpy=True)
        self.index.add(embs.astype('float32'))
        self.docs.extend(docs)

    def query(self, text: str, top_k: int = 3):
        q = self.embed.encode([text], convert_to_numpy=True).astype('float32')
        D, I = self.index.search(q, top_k)
        return [self.docs[i] for i in I[0] if i != -1]

# Usage: create index, add docs (some could be "malicious"), then query and feed retrieved docs into chain