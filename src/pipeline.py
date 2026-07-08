from .loader import load_pdf
from .preprocess import clean_text, chunk_pages
from .embeddings import load_embedding_model, generate_embeddings
from .retriever import generate_query_embedding, retrieve_chunks, build_context
from .prompt import build_prompt
from .llm import initialize_llm, generate_response

def run_pipeline(pdf_path:str, query:str, api_key: str, embedding_model: str = "all-MiniLM-L6-v2", llm_model: str = "gemini-2.5-flash", chunk_size: int = 500, overlap: int = 100, top_k: int = 3)-> str:
    """
    Execute the complete Retrieval-Augmented Generation (RAG) pipeline from PDF loading to final answer generation.

    Args:
        pdf_path: Path to the PDF document.
        query: User's question.
        api_key: Gemini API key.
        embedding_model: Sentence Transformer model name.
        llm_model: Gemini model name.
        chunk_size: Maximum characters per chunk.
        overlap: Number of overlapping characters.
        top_k: Number of chunks to retrieve.

    Returns:
        Generated answer from the LLM.
    """
    
    pages = load_pdf(pdf_path)

    pages = clean_text(pages)

    chunks = chunk_pages(pages,chunk_size,overlap)

    model = load_embedding_model(embedding_model)

    chunks = generate_embeddings(chunks, model)

    query_embedding = generate_query_embedding(query, model)

    top_chunks = retrieve_chunks(chunks, query_embedding, top_k)

    client = initialize_llm(api_key)

    context = build_context(top_chunks)

    prompt = build_prompt(context, query) 

    output = generate_response(client, prompt, llm_model)

    return output