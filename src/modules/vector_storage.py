import os
import streamlit as st
from langchain.vectorstores import Chroma

def store_embeddings_in_chroma(chunk_embeddings):
    """Store provided embeddings in ChromaDB."""
    
    # Assuming chunk_embeddings is a list of (chunk_text, embedding_vector) pairs
    documents = [{'text': chunk_text, 'vector': embedding_vector} 
                 for chunk_text, embedding_vector in chunk_embeddings]

    # Store in ChromaDB
    db = Chroma.from_pre_embedded_documents(documents)
    
    return db