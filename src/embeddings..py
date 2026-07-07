def load_embedding_model(model_name: str = "all-MiniLM-L6-v2")-> SentenceTransformer:
    """
        Loads desired embeddings model
    """
    return SentenceTransformer(model_name)


def generate_embeddings(chunks: list[dict], model: SentenceTransformer)-> list[dict]:
    """
        Generate vector embeddings for each text chunk using a Sentence Transformer model.

        Args:
            chunks: List of dictionaries, Chunk-wise.
            model: Selected Sentence Transformer model

        Returns:
            List of dictionaries, with an added key of vector embeddings
    """
    for chunk in chunks:
        text = chunk["text"]
        embedding = model.encode(text)

        chunk["embedding"] = embedding

    return chunks