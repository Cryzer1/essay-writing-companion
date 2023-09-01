# To build the File Upload module, let's first create a sample function that will be integrated into main.py later.
# This function will handle the uploading of PDF files using Streamlit's file_uploader and will return the uploaded files.

def file_upload():
    import streamlit as st
    
    uploaded_files = st.file_uploader(
        label="Upload your essay assignment and readings (PDF format)",
        type=["pdf"],
        accept_multiple_files=True
    )
    
    if uploaded_files:
        st.success(f"{len(uploaded_files)} files uploaded.")
    else:
        st.warning("No files uploaded yet.")
        
    return uploaded_files

# This function will be integrated into main.py.
# It uses Streamlit's file_uploader to let the user upload multiple PDF files.
# It returns the list of uploaded files.
