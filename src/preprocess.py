def clean_text(pages: list[dict])-> list[dict]:
    """
        Clean extracted page text by replacing newline characters with spaces and removing extra whitespace.

        Args:
            pages : List of dictionaries containing page number and extracted text.

        Returns:
            List of dictionaries with cleaned page text.
    """

    for page in pages:
        content = page["text"]

        content = content.replace("\n", " ")
        content = " ".join(content.split())

        page["text"] = content

    return pages

def chunk_pages(pages: list[dict], chunk_size: int, overlap: int)-> list[dict]:
    """
        Split cleaned page text into overlapping character-based chunks of respective Chunk_id with provided Chunk size on the basis of fixed-size chunks with overlap.

        Args:
            pages : List of dictionaries with cleaned page text.
            chunk_size : desired chunk size
            overlap : desired overlapping
        
        Returns:
            List of dictionaries, divided into chunks of desired chunk size
    """
    chunks = []

    for page in pages:
        text = page["text"]
        page_no = page["page_num"]

        start = 0
        chunk_id = 1

        while start<len(text):
            end = start + chunk_size
            chunk_text = text[start:end]

            chunked_text.append({
                "page_num" : page_no,
                "chunk_id" : chunk_id,
                "text" : chunk_text
            })

            start += chunk_size - overlap
            chunk_id += 1

    return chunks