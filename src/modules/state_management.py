# For State Management, we'll create a function that will store the state of uploaded files and 'pages' objects.
# Streamlit doesn't have native support for session state, so we'll use a workaround to manage state.

def manage_state(uploaded_files=None, all_docs=None, assignment_description=None, chunk_embeddings=None, chroma_db=None):
    """Manage the state of uploaded files and 'pages' objects."""
    import streamlit as st

    if 'uploaded_files' not in st.session_state:
        st.session_state.uploaded_files = uploaded_files if uploaded_files else []
    else:
        if uploaded_files:
            st.session_state.uploaded_files = uploaded_files

    if 'all_docs' not in st.session_state:
        st.session_state.all_docs = all_docs if all_docs else []
    else:
        if all_docs:
            st.session_state.all_docs = all_docs

    if 'assignment_description' not in st.session_state:
        st.session_state.assignment_description = assignment_description if assignment_description else ""
    else:
        if assignment_description:
            st.session_state.assignment_description = assignment_description
            
    if 'chunk_embeddings' not in st.session_state:
        st.session_state.chunk_embeddings = chunk_embeddings if chunk_embeddings else []
    else:
        if chunk_embeddings:
            st.session_state.chunk_embeddings = chunk_embeddings
            
    if 'chroma_db' not in st.session_state:
        st.session_state.chroma_db = chroma_db if chroma_db else None
    else:
        if chroma_db:
            st.session_state.chroma_db = chroma_db

# This function checks if 'uploaded_files' and 'all_docs' keys are present in Streamlit's session_state.
# If not, it initializes them. If already present, it updates them with new values if provided.
