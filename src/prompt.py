def build_prompt(context: str, query: str)-> str:

    prompt = f"""
    You are a Helpful AI Assistant

    Answer the query provided by the user only using the provided context.

    If the answer is not present in the provided document, answer "I don't know the answer based on the provided document."

    Context: {context}
    Query: {query}
    Answer:
"""
    return prompt
