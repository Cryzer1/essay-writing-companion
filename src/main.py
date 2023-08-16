import streamlit as st
import os
from modules.structured_display import display_ui

st.set_page_config(page_title="Essay Writing Companion", page_icon="📝")
st.title("📝 Essay Writing Companion")
os.environ['OPENAI_API_KEY'] = st.sidebar.text_input("OpenAI API Key:", type="password")
uploaded_files = st.file_uploader(
        label="Upload your essay assignment and readings (PDF format)",
        type=["pdf"],
        accept_multiple_files=True,
    )
# Validate the uploaded files
if not uploaded_files:
        st.info("Please upload your documents in PDF format to proceed.")
display_ui(uploaded_files)

