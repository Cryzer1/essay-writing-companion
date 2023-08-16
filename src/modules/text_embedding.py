import streamlit as st
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings

def generate_document_embeddings(extracted_texts):
    """Generate embeddings for the provided texts."""
    
    # Split texts into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100, length_function = len,
    add_start_index = True)
    chunks = text_splitter.split_documents(extracted_texts)

    # Generate embeddings for the chunks
    embeddings_model = OpenAIEmbeddings()
    chunk_embeddings = embeddings_model.embed(chunks)
    
    return chunk_embeddings

# Assuming the 'extracted_texts' variable is available from the Text Extraction Module
if extracted_texts:
    chunk_embeddings = generate_document_embeddings(extracted_texts)
    
    # Displaying a confirmation for the MVP
    st.write(f"{len(chunk_embeddings)} document chunks have been successfully embedded!")
