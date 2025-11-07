from pypdf import PdfReader
from PIL import Image
import pytesseract
import io

def extract_text(image: Image.Image):
    text = pytesseract.image_to_string(image)
    return text.strip()

def extract_text_from_image(pdf_path):
    reader = PdfReader(pdf_path)
    for page_number, page in enumerate(reader.pages, start=1):
        for image_number, image_file_object in enumerate(page.images, start=1):
            image = Image.open(io.BytesIO(image_file_object.data)).convert("RGB")


            # Step 1
            text_content = extract_text(image)
            print(f"Page Number {page_number}")
            print(f"Image Number {image_number}")
            print("Extracted Text:\n")
            print(text_content if text_content else "(No text found)\n")




pdf_path = "Software process workflows and Iteration workflows.pdf"
extract_text_from_image(pdf_path)