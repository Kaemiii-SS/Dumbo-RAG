import os
from dotenv import load_dotenv
from src.pipeline import run_pipeline

def main():
    load_dotenv()

    api_key = os.getenv("GEMINI_API_KEY")
    if api_key is None:
        raise ValueError(
            "GEMINI_API_KEY not found. Please configure your .env file."
        )

    pdf_path = input("Enter PDF path: ")
    query = input("Ask a question: ")

    embedding_model = input("Embedding model [all-MiniLM-L6-v2]: ") or "all-MiniLM-L6-v2"

    chunk_size = int(input("Chunk size [500]: ") or 500)

    overlap = int(input("Overlap [100]: ") or 100)

    top_k = int(input("Top K [3]: ") or 3)

    answer = run_pipeline(
        pdf_path=pdf_path,
        query=query,
        api_key=api_key,
        embedding_model=embedding_model,
        chunk_size=chunk_size,
        overlap=overlap,
        top_k=top_k,
    )

    print("\nAnswer:\n")
    print(answer)


if __name__ == "__main__":
    main()