import os
import tempfile
import streamlit as st
from langchain.document_loaders import PyPDFLoader

def extract_texts_from_files(uploaded_files):
    """Extract text from the provided list of uploaded PDF files."""
    extracted_texts = []

    for file in uploaded_files:
        # Create a temporary file to work with the PyPDFLoader
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            temp_file.write(file.getvalue())
        
        # Use PyPDFLoader to extract text
        try:
            loader = PyPDFLoader(temp_file.name)
            doc_texts = loader.load()
            extracted_texts.extend(doc_texts)
        except Exception as e:
            st.warning(f"Error extracting text from {file.name}: {e}")
            continue  # Move on to the next file
        
        # Cleanup temporary file
        os.remove(temp_file.name)

    return extracted_texts

# Assuming the 'uploaded_files' variable is available from the File Upload Module
if uploaded_files:
    extracted_texts = extract_texts_from_files(uploaded_files)
    
    # Displaying the extracted text (for MVP purposes)
    for idx, text in enumerate(extracted_texts):
        st.write(f"Extracted Text from Document {idx + 1}:\n{text[:500]}...")  # Displaying the first 500 characters for brevity
