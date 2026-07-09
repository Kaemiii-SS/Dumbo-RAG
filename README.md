# Dumbo-RAG

A Retrieval-Augmented Generation (RAG) application built completely from scratch in Python that answers questions about a PDF document using semantic search and Google Gemini.

Instead of relying on high-level frameworks like LangChain or LlamaIndex, I chose to implement the core RAG pipeline manually to better understand how modern retrieval systems work.

## Features

- PDF text extraction using PyPDF
- Text preprocessing
- Character-based chunking with overlap
- Sentence embeddings using Sentence Transformers
- Cosine similarity retrieval
- Prompt construction
- Answer generation using Google Gemini

---

## Project Structure

```text
Dumbo-RAG/
│
├── app.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
│
├── data/
├── notebooks/
└── src/
    ├── loader.py
    ├── preprocess.py
    ├── embeddings.py
    ├── retriever.py
    ├── prompt.py
    ├── llm.py
    └── pipeline.py
```

---

## Architecture

```text
                app.py
                   │
                   ▼
            run_pipeline()
                   │
     ┌─────────────┼─────────────┐
     ▼             ▼             ▼
 loader      preprocess     embeddings
                                   │
                                   ▼
                              retriever
                                   │
                                   ▼
                                prompt
                                   │
                                   ▼
                                  llm
```

---

## Installation

```bash
git clone https://github.com/Kaemiii-SS/Dumbo-RAG.git

cd Dumbo-RAG

pip install -r requirements.txt
```

Create a `.env` file.

```text
GEMINI_API_KEY=your_api_key
```

---

## Usage

```bash
python app.py
```

Example:

```
Enter PDF path:
Ask a question:
```

---

## Tech Stack

- Python
- PyPDF
- Sentence Transformers
- scikit-learn
- Google Gemini API
- python-dotenv

---

## Current Limitations

- Fixed-size character chunking
- Linear search using cosine similarity
- Single document support
- No reranking
- No vector database

---

### Why I built this

*Honestly, I wanted to understand the basic principle of Retrieval-Augmented-Generation without depending too much on frameworks. The goal was simply to implement each stage like loading, chunking, creating embeddings , etc. from scratch and in the simplest way possible.*

