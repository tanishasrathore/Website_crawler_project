# Website_crawler_project
# Website-Based Chatbot Using Embeddings

## Overview
This project is a Retrieval-Augmented Generation (RAG) chatbot that answers questions strictly based on a provided website.

## Architecture
1. Crawl website content
2. Clean & normalize text
3. Chunk text with overlap
4. Generate embeddings
5. Store in FAISS vector database
6. Retrieve relevant chunks
7. Generate grounded answers using LLM
8. Streamlit-based UI with chat memory

## Tech Stack
- Streamlit (UI)
- LangChain (RAG pipeline)
- SentenceTransformers (Embeddings)
- FAISS (Vector DB)
- OpenAI GPT-3.5 (LLM)
- BeautifulSoup (Web scraping)

## Why FAISS?
FAISS is lightweight, fast, and ideal for local persistent vector search.

## Why MiniLM Embeddings?
Fast, free, and performs well for semantic search tasks.

## Setup Instructions
```bash
pip install -r requirements.txt
streamlit run app.py
