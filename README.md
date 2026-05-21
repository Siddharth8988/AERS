# AERS — Agentic Educational Retrieval System

A fully offline, multi-agent educational retrieval system designed for semantic search, contextual tutoring, and citation-backed question answering on low-end CPU-only hardware.

Built and optimized on a Lenovo ThinkPad T460 using local LLMs, ChromaDB, OCR pipelines, and intelligent retrieval orchestration without any cloud APIs or GPU acceleration.

---

# Overview

AERS (Agentic Educational Retrieval System) is a privacy-focused Retrieval-Augmented Generation (RAG) platform that enables users to query educational documents and receive context-aware answers with exact source citations.

The system uses a modular multi-agent architecture where each agent performs a dedicated responsibility:

- Query routing
- Semantic retrieval
- Relevance reranking
- Educational response generation
- Citation extraction

The entire pipeline runs locally and remains fully functional offline after setup.

---

# System Architecture

```text
User Query
    │
    ▼
[Planner Agent]
    │
    ├── GREET  ──► Instant Response
    │
    └── SEARCH
            │
            ▼
[Retrieval Agent]
            │
            ▼
[ChromaDB Semantic Search]
            │
            ▼
[CrossEncoder Reranker]
            │
            ▼
[Tutor Agent]
            │
            ▼
[Citation Agent]
            │
            ▼
Streaming Response to User
```

---

# Core Features

- Multi-agent AI architecture
- Fully offline execution
- Semantic retrieval using ChromaDB
- CrossEncoder reranking pipeline
- OCR support for scanned PDFs
- Multi-format ingestion:
  - PDF
  - DOCX
  - PPTX
  - TXT
- Streaming ChatGPT-style responses
- Citation-backed answers with page numbers
- Conversational memory support
- Intelligent query routing
- Persistent vector database storage
- CPU-optimized inference pipeline
- Zero API cost

---

# Tech Stack

## AI / LLM Layer

- Ollama
- Qwen2.5:3B
- Gemma2:2B
- LangChain
- langchain-community
- langchain-core
- langchain-ollama

## Retrieval Pipeline

- ChromaDB
- sentence-transformers/all-MiniLM-L6-v2
- BAAI/bge-reranker-base

## OCR & Document Processing

- Tesseract OCR 5.3.4
- pytesseract
- pdf2image
- PyPDF
- python-docx
- python-pptx

## Frontend

- Streamlit
- Custom dark-mode UI
- Streaming responses using `st.write_stream()`

## Backend

- Python 3.12

---

# CPU Optimization Techniques

AERS was engineered specifically for low-resource hardware environments.

Implemented optimizations include:

1. Intelligent query routing
   - Greeting queries bypass vector search entirely to reduce unnecessary CPU usage.

2. Context truncation
   - Retrieval context capped at 4000 characters before LLM generation.

3. Sliding window conversational memory
   - Maintains only the last 3 exchanges to reduce prompt overhead.

4. Persistent local vector storage
   - ChromaDB stored on SSD for faster retrieval performance.

5. Lightweight local inference
   - Optimized to run entirely on a dual-core CPU without GPU acceleration.

---

# Performance Results

Successfully tested on:

- 529-page academic textbook
- 2,833 indexed semantic chunks

System capabilities:

- Accurate semantic retrieval
- Citation-backed educational responses
- OCR extraction from scanned PDFs
- Fully local inference on CPU-only hardware
- Real-time streaming responses

---

# Hardware Used

- Lenovo ThinkPad T460
- Intel i5-6200U
- 2 Cores / 4 Threads
- 16GB RAM
- SSD Storage
- No GPU
- Linux Mint 22.2

---

# Project Structure

```text
AERS/
├── agents/
│   ├── citation_agent.py
│   ├── planner_agent.py
│   ├── reranker.py
│   ├── retrieval_agent.py
│   └── tutor_agent.py
│
├── core/
│   ├── processor.py
│   └── vectorstore.py
│
├── ui/
├── documents/
├── chroma_db/
├── config/
├── logs/
│
├── .streamlit/
│   └── config.toml
│
├── app.py
├── config.py
├── requirements.txt
└── start_aers.sh
```

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/Siddharth8988/AERS.git
cd AERS
```

---

## 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install System Dependencies

```bash
sudo apt update

sudo apt install -y \
tesseract-ocr \
libtesseract-dev \
poppler-utils
```

---

## 4. Install Ollama

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

---

## 5. Pull Local Models

```bash
ollama pull qwen2.5:3b
ollama pull gemma2:2b
```

---

## 6. Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

## 7. Run Application

```bash
chmod +x start_aers.sh
./start_aers.sh
```

Or directly:

```bash
streamlit run app.py
```

---

# Future Improvements

- Hybrid retrieval (BM25 + vector search)
- Docker containerization
- Multi-user authentication
- GPU acceleration support
- Web-based upload dashboard
- Agent monitoring and observability
- Advanced memory systems
- Evaluation benchmark suite

---

# Author

Siddhardha Raju

CSE Student | AI/ML Enthusiast | Linux-Based AI Systems Builder
