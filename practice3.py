from pypdf import PdfReader
from PIL import Image
import pytesseract
import io

def extract_text(image: Image.Image):
    text = pytesseract.image_to_string(image)
    return text.strip()

def extract_text_from_image(pdf_path):
    reader = PdfReader(pdf_path)
    for page in reader.pages:
        for image_file_object in page.images:
            image = Image.open(io.BytesIO(image_file_object.data)).convert("RGB")


            # Step 1
            text_content = extract_text(image)
            print("Extracted Text:\n")
            print(text_content if text_content else "(No text found)")




pdf_path = "html2pdfx_Report_sample.pdf"
extract_text_from_image(pdf_path)