import PyPDF2

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = "\n".join(page.extract_text() for page in reader.pages if page.extract_text())
    return text
