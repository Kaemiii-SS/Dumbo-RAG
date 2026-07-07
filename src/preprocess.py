def clean_text(pages: list[dict])-> list[dict]:
    """
        Clean extracted page text by replacing newline characters with spaces and removing extra whitespace.

        Args:
            pages : List of dictionaries containing page number and extracted text.

        Returns:
            Returns:
            List of dictionaries with cleaned page text.
    """

    for page in pages:
        content = page["text"]

        content = content.replace("\n", " ")
        content = " ".join(content.split())

        page["text"] = content

    return pages

