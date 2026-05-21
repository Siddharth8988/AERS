# Note: For absolute beginners, we use a Cross-Encoder approach
from sentence_transformers import CrossEncoder

def rerank_documents(query, documents):
    model = CrossEncoder('BAAI/bge-reranker-base')
    pairs = [[query, doc.page_content] for doc in documents]
    scores = model.predict(pairs)
    
    # Sort by score and return top 3
    for i, doc in enumerate(documents):
        doc.metadata['rerank_score'] = scores[i]
    
    sorted_docs = sorted(documents, key=lambda x: x.metadata['rerank_score'], reverse=True)
    return sorted_docs[:3]
