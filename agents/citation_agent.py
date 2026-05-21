class CitationAgent:
    def __init__(self):
        pass

    def format_citations(self, docs):
        citations = []
        for i, doc in enumerate(docs):
            source = doc.metadata.get("source", "Unknown")
            filename = source.split("/")[-1]
            page = doc.metadata.get("page", "N/A")
            
            citation_info = {
                "id": i + 1,
                "content": doc.page_content[:200] + "...",
                "source": filename,
                "page": page
            }
            citations.append(citation_info)
        return citations

    def verify_answer(self, answer, docs):
        if "I don't know" in answer or "not in the context" in answer:
            return False
        return True
