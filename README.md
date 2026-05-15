# LLM-Powered RAG Chatbot System

An end-to-end Retrieval-Augmented Generation (RAG) chatbot system built with FastAPI, Streamlit, LangChain, HuggingFace embeddings, and ChromaDB.

This project enables users to upload and query PDF documents using semantic search and Large Language Models (LLMs). The system retrieves the most relevant document chunks from a vector database and generates context-aware responses.

---

# Project Overview

The chatbot uses a Retrieval-Augmented Generation (RAG) architecture to improve response quality by grounding answers in external documents.

The pipeline includes:

1. PDF ingestion and preprocessing
2. Text chunking and embedding generation
3. Vector database storage using ChromaDB
4. Semantic retrieval
5. LLM-powered response generation
6. FastAPI backend API
7. Streamlit frontend interface
8. Dockerized deployment

---

# Features

- PDF document ingestion
- Semantic search with vector embeddings
- Context-aware question answering
- FastAPI REST API
- Streamlit web interface
- ChromaDB vector storage
- HuggingFace embedding models
- Modular production-ready project structure
- Docker support for deployment

---

# Tech Stack

## Backend
- Python
- FastAPI
- LangChain

## Frontend
- Streamlit

## Vector Database
- ChromaDB

## Embeddings
- HuggingFace Sentence Transformers

## LLM Integration
- Transformers Pipeline
- OpenAI Compatible Architecture

## Deployment
- Docker
- Docker Compose

---

# Project Structure

```bash
rag_chatbot_system/
│
├── src/
│   ├── api/
│   ├── ingestion/
│   ├── retrieval/
│   ├── llm/
│   ├── frontend/
│   └── utils/
│
├── data/
│   └── raw/
│
├── artifacts/
│   └── chroma_db/
│
├── tests/
│
├── run_ingestion.py
├── run_frontend.py
├── test_retrieval.py
├── test_rag.py
│
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/Esostar/rag_chatbot_system.git
```

```bash
cd rag_chatbot_system
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
```

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Project

## Step 1 — Add PDF Documents

Place PDF files inside:

```bash
data/raw/
```

---

## Step 2 — Run Document Ingestion

```bash
python run_ingestion.py
```

This will:
- load PDFs
- split text into chunks
- generate embeddings
- store vectors in ChromaDB

---

## Step 3 — Test Semantic Retrieval

```bash
python test_retrieval.py
```

---

## Step 4 — Run RAG Chatbot

```bash
python test_rag.py
```

---

# Run FastAPI Backend

```bash
uvicorn src.api.main:app --reload
```

API available at:

```bash
http://127.0.0.1:8000
```

Swagger documentation:

```bash
http://127.0.0.1:8000/docs
```

---

# Run Streamlit Frontend

```bash
streamlit run run_frontend.py
```

---

# Docker Deployment

## Build and Run

```bash
docker compose up --build
```

---

# Example Questions

- What is attention mechanism?
- Explain BERT architecture
- What are transformers in NLP?
- Summarize the uploaded document
- What is semantic search?

---

# Future Improvements

- Conversational memory
- Multi-document reasoning
- Hybrid search (BM25 + vector search)
- Authentication and user management
- Cloud deployment
- GPU acceleration
- Multi-agent workflows
- Citation-aware answers

---

# Screenshots

Add screenshots here after running the application.

Example:
- Streamlit UI
- Swagger API Docs
- Retrieval results
- Chat responses

---

# Author

Ajali Augustine Esosa

Data Scientist | Machine Learning Engineer | AI Engineer