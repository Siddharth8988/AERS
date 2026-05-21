from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
import config

class RetrievalAgent:
    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(model_name=config.EMBEDDING_MODEL)
        self.vectorstore = Chroma(
            persist_directory=config.CHROMA_PATH,
            embedding_function=self.embeddings
        )

    def search(self, query, k=5):
        docs = self.vectorstore.similarity_search(query, k=k)
        
        if not docs:
            return "No relevant information found in the uploaded syllabus documents."
        
        return docs

    def get_context_string(self, docs):
        return "\n\n".join([doc.page_content for doc in docs])
