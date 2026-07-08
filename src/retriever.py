from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def generate_query_embedding(query: str,model: SentenceTransformer):
    """
    Generate an embedding for the user's query.

    Args:
        query: User's input question.
        model: Loaded Sentence Transformer model.

    Returns:
        Query embedding vector.
    """

    return model.encode(query)

def retrieve_chunks(chunks: list[dict], query_embedding: np.ndarray, top_k: int = 3) -> list[dict]:
    """
    Retrieves the top K chunks depending on the user's query.

    Args:
        chunks: List of Dictionaries, separated chunk-wise.
        query_embedding: Embedding vector generated from the user's query.
        top_k:  List of the top-k most relevant chunks sorted by cosine similarity.

    Returns:
        top k chunks based upon the User's Query.
    """

    results = []
    for chunk in chunks:
        embedding = chunk["embedding"] 
        score=cosine_similarity([query_embedding],[embedding])[0][0]
        results.append({
            "score" : score,
            "chunk" : chunk
            })

    top_chunks = sorted(results, key=lambda x: x["score"] ,reverse=True)[:top_k]
    return top_chunks

def build_context(top_chunks: list[dict])-> str:
    """
        builds context in string from the top k retrieved chunks

        Args:
            top_chunks: The retrieved top K chunks through cosine similarity

        Returns:
            A string of context extracted from the retrieved chunks
    """
    context = []
    for x in top_chunks:
        text = x["chunk"]["text"] 
        context.append(text)

    context = "\n\n".join(context)

    return context