# For Error Handling, let's create a function that will handle various types of errors such as file type issues,
# API key issues, and text extraction failures. This function will display appropriate warnings via Streamlit.

def handle_errors(uploaded_files=None, api_key=None, extraction_errors=None, assignment_description=None):
    import streamlit as st
    
    if not uploaded_files:
        st.warning("Please upload PDF files to proceed.")
    
    if api_key and len(api_key.strip()) == 0:
        st.warning("Please enter a valid OpenAI API key.")
    
    if extraction_errors:
        for error in extraction_errors:
            st.warning(error)

    if not assignment_description:
        st.warning("Please enter the assignment description.")

# This function takes three parameters: uploaded_files, api_key, and extraction_errors.
# It checks each one and displays an appropriate warning message via Streamlit if needed.
