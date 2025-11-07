from pypdf import PdfReader

def extract_images_from_pdf():
    reader = PdfReader("sample_with_images.pdf")
    page = reader.pages[0]

    for count, image_file_object in enumerate(page.images):
        with open(str(count) + image_file_object.name, "wb") as fp:
            fp.write(image_file_object.data)
        

extract_images_from_pdf()