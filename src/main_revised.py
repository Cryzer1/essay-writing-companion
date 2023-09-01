
import streamlit as st
import os
from modules.file_upload import file_upload
from modules.text_extraction import extract_texts_from_files
from modules.state_management import manage_state
from modules.error_handling import handle_errors
from modules.assignment_description import get_assignment_description
from modules.text_embedding import generate_document_embeddings
from modules.vector_storage import store_embeddings_in_chroma

st.set_page_config(page_title="Essay Writing Companion", page_icon="📝")
st.title("📝 Essay Writing Companion")

# Gets OpenAI API key from user
openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")
if not openai_api_key:
    st.info("Please add your OpenAI API key to continue.")
    st.stop()
os.environ['OPENAI_API_KEY'] = openai_api_key

# User assignment description input
assignment_description = get_assignment_description()

# File Upload
uploaded_files = file_upload()

# Text Extraction
all_docs, extraction_errors = extract_texts_from_files(uploaded_files) if uploaded_files else ([], [])

# Text embedding in chunks
chunk_embeddings = generate_document_embeddings(all_docs)

# Store embeddings in VectorDB
chroma_db = store_embeddings_in_chroma(chunk_embeddings)

# State Management
manage_state(uploaded_files, all_docs)

# Error Handling
handle_errors(uploaded_files, api_key, extraction_errors)

# For demonstration purposes, showing the number of uploaded files and extracted documents.
if uploaded_files:
    st.write(f"{len(uploaded_files)} files uploaded.")
if all_docs:
    st.write(f"{len(all_docs)} documents extracted.")
