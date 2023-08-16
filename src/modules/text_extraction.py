import streamlit as st
from langchain.document_loaders import PyPDFLoader

def extract_texts_from_files(uploaded_files):
    """Extract text from the provided list of uploaded PDF files."""
    all_docs = []

    for file in uploaded_files:
        # Load the content directly into PyPDFLoader without creating temporary files
        try:
            loader = PyPDFLoader(file)
            docs = loader.load()
            all_docs.extend(docs)
        except Exception as e:
            st.warning(f"Error extracting text from {file.name}: {e}")
            continue

    return all_docs
