import streamlit as st
from dotenv import load_dotenv

def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with PDF's", page_icon=":books:")
    st.header("Chat with PDF's :books:")
    st.text_input("Ask a question about your documents")

    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs = st.file_uploader("Upload your pdfs here and Click on process", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing"):
                #get the pdf


                #get the text chunks


                #create vector store


if __name__ == '__main__':
    main()