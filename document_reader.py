from pypdf import PdfReader
from PIL import Image
from practice3 import extract_text
import io

def get_pdf_text(pdf_docs):
    """Extract raw text from uploaded PDF files."""
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            content = page.extract_text()
            if content:
                text += content.strip() + "\n"

            if hasattr(page, "images"):
                for image_file_object in page.images:
                    image = Image.open(io.BytesIO(image_file_object.data)).convert("RGB")
                    image_text = extract_text(image)
                    if image_text:
                        text += image_text.strip()
    return text