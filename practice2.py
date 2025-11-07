from pypdf import PdfReader
from PIL import Image
import io

def extract_image_features(pdf_path):
    reader = PdfReader(pdf_path)
    for page in reader.pages:
        for image_index, image_file_object in enumerate(page.images):
            image = Image.open(io.BytesIO(image_file_object.data)) #Convert PDF image data to a Pillow image


            #Extract features
            width, height = image.size
            mode = image.mode
            format = image.format
            histogram = image.histogram()


            print(f"width: {image_index,width}\n")
            print(f"mode: {image_index, mode}\n")
            print(f"format: {image_index, format}\n")
            print(f"histogram: {len(histogram)}\n")


# pdf_path = "html2pdfx_Report_sample.pdf"
extract_image_features("html2pdfx_Report_sample.pdf")

