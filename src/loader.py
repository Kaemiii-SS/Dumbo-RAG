from pypdf import PdfReader

def load_pdf(pdf_path:str)->(list[dict]):
    """
        Load the pdf at the given path and extract its text.

        Args:
            pdf_path : Path where the pdf is located.

        Returns:
            A list of dictionary, page-wise containing text of the pdf.
    """
    reader = pypdf.PdfReader(pdf_path)

    pages = []
    for i,page in enumerate(reader.pages):
        pages.append({
            "page_num" : i+1,
            "text" : page.extract_text()
        })
    return pages