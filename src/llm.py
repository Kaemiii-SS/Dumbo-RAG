from google import genai


def initialize_llm(api_key: str) -> genai.Client:
    """
    Initialize and return the Gemini client.

    Args:
        api_key: Gemini API key.

    Returns:
        Configured Gemini client.
    """

    return genai.Client(api_key=api_key)


def generate_response(client: genai.Client, prompt: str, model_name: str = "gemini-2.5-flash") -> str:
    """
    Generate a response from Gemini.

    Args:
        client: Initialized Gemini client.
        prompt: Prompt sent to the LLM.
        model_name: Gemini model to use.

    Returns:
        Generated response as text.
    """

    response = client.models.generate_content(
        model=model_name,
        contents=prompt,
    )

    return response.text