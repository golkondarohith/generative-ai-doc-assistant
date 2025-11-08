import streamlit as st
from dotenv import load_dotenv
from htmlTemplates import css, bot_template, user_template
from document_reader import get_pdf_text
from text_splitter import get_text_chunks
from embedding_engine import get_vectorstore
from index_store import get_conversation_chain
from retriever import handle_userinput


# ---------- Streamlit App ----------

def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with PDFs", page_icon="📚")
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.header("📚 Chat with your PDFs")
    user_question = st.text_input("Ask a question about your documents")

    if user_question and st.session_state.conversation:
        handle_userinput(user_question)

    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs = st.file_uploader("Upload PDFs and click Process", accept_multiple_files=True)
        if st.button("Process"):
            if pdf_docs:
                with st.spinner("Processing..."):
                    raw_text = get_pdf_text(pdf_docs)
                    # st.write(raw_text)
                    text_chunks = get_text_chunks(raw_text)
                    st.write(text_chunks)
                    vectorstore = get_vectorstore(text_chunks)
                    st.session_state.conversation = get_conversation_chain(vectorstore)
                st.success("✅ Documents processed successfully!")
            else:
                st.warning("Please upload at least one PDF file.")


if __name__ == "__main__":
    main()
