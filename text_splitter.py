from langchain.text_splitter import CharacterTextSplitter


def get_text_chunks(text):
    """Split text into overlapping chunks."""
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    return text_splitter.split_text(text)