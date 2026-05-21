import streamlit as st
import os
from core.processor import process_document
from core.vectorstore import get_vectorstore
from agents.retrieval_agent import RetrievalAgent
from agents.citation_agent import CitationAgent
from agents.planner_agent import PlannerAgent
from langchain_ollama import OllamaLLM
import config

st.set_page_config(page_title="AERS AI Tutor", layout="wide")

def truncate_context(context, max_chars=4000):
    """Prevent oversized prompts killing CPU performance"""
    return context[:4000] if len(context) > 4000 else context

@st.cache_resource
def initialize_system():
    llm = OllamaLLM(model=config.LLM_MODEL)
    retriever = RetrievalAgent()
    citer = CitationAgent()
    planner = PlannerAgent(llm)
    vectorstore = get_vectorstore()
    return llm, retriever, citer, planner, vectorstore

llm, retriever, citer, planner, vectorstore = initialize_system()

if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

with st.sidebar:
    st.title("📚 Document Center")
    uploaded_files = st.file_uploader(
        "Upload PDFs",
        type=['pdf', 'docx', 'pptx', 'txt'],
        accept_multiple_files=True
    )

    if st.button("Index Documents"):
        if uploaded_files:
            with st.spinner("Processing & Embedding..."):
                all_chunks = []
                for uploaded_file in uploaded_files:
                    file_path = os.path.join(config.DOC_DIR, uploaded_file.name)
                    with open(file_path, "wb") as f:
                        f.write(uploaded_file.getbuffer())
                    chunks = process_document(file_path)
                    all_chunks.extend(chunks)
                vectorstore.add_documents(all_chunks)
                st.success(f"Indexed {len(all_chunks)} chunks!")
        else:
            st.warning("Please upload files first.")

    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.session_state.chat_history = []
        st.success("Memory cleared!")

st.title("🎓 Agentic Educational Retrieval System")
st.markdown(f"Running on **{config.LLM_MODEL}** (Local & Offline)")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if "citations" in message:
            with st.expander("Sources"):
                st.json(message["citations"])

if prompt := st.chat_input("Ask a question about your syllabus..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        route = planner.route_query(prompt)

        if route == "GREET":
            response = "Hello! I'm your AERS AI Tutor. Ask me anything about your uploaded documents!"
            citations = []
            st.markdown(response)

        else:
            relevant_docs = retriever.search(prompt)
            context = truncate_context(retriever.get_context_string(relevant_docs))
            citations = citer.format_citations(relevant_docs)

            history_text = ""
            last_3 = st.session_state.chat_history[-3:]
            for exchange in last_3:
                history_text += f"Student: {exchange['human']}\nProfessor: {exchange['assistant']}\n\n"

            full_prompt = f"""You are an expert professor. Use the context and conversation history to answer.

CONVERSATION HISTORY:
{history_text}

CONTEXT FROM DOCUMENTS:
{context}

STUDENT QUESTION: {prompt}
PROFESSOR RESPONSE:"""

            # STREAMING — text appears word by word like ChatGPT
            response = st.write_stream(llm.stream(full_prompt))

        if citations:
            with st.expander("Verified Sources"):
                for c in citations:
                    st.write(f"🔹 **{c['source']}** (Page {c['page']})")

        st.session_state.chat_history.append({
            "human": prompt,
            "assistant": response
        })

        st.session_state.messages.append({
            "role": "assistant",
            "content": response,
            "citations": citations
        })
