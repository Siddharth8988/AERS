from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
import config

def get_vectorstore():
    # Runs entirely on CPU
    embeddings = HuggingFaceEmbeddings(model_name=config.EMBEDDING_MODEL)
    return Chroma(
        persist_directory=config.CHROMA_PATH,
        embedding_function=embeddings
    )
