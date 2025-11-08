from docx import Document

def extract_text_from_docx(docx_path):
    """Extract plain text from a .docx file."""
    doc = Document(docx_path)
    text = []
    for para in doc.paragraphs:
        if para.text.strip():  # Avoid empty lines
            text.append(para.text.strip())
    return "\n".join(text)


text = extract_text_from_docx("Week 10 Assesment Asingment.docx")
print(text)
