import streamlit as st
from dotenv import load_dotenv
from pypdf import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_openai import ChatOpenAI
from htmlTemplates import css, bot_template, user_template
import io
from PIL import Image
from practice3 import extract_text


# ---------- Helper Functions ----------

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

def get_text_chunks(text):
    """Split text into overlapping chunks."""
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    return text_splitter.split_text(text)


