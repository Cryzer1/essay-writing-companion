from langchain.vectorstores import Chroma

def store_embeddings_in_chroma(chunk_embeddings):
    """Store provided embeddings in ChromaDB."""
    
    # Convert chunk embeddings to ChromaDB format
    documents = [{'text': chunk['text'], 'vector': embedding} for chunk, embedding in chunk_embeddings]
    
    # Initialize ChromaDB and store embeddings
    chroma_db = Chroma.from_pre_embedded_documents(documents)
    
    return chroma_db