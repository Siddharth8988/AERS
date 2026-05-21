import os

# CPU-Specific Settings
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
RERANKER_MODEL = "BAAI/bge-reranker-base"
LLM_MODEL = "qwen2.5:3b"
CHROMA_PATH = "./chroma_db"
DOC_PATH = "./documents"

# Chunking Strategy for Technical Content
CHUNK_SIZE = 600
CHUNK_OVERLAP = 120
DOC_DIR = "./documents"
