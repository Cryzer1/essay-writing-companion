import streamlit as st
import os
from modules.structured_display import display_ui

st.set_page_config(page_title="Essay Writing Companion", page_icon="📝")
st.title("📝 Essay Writing Companion")
os.environ['OPENAI_API_KEY'] = st.sidebar.text_input("OpenAI API Key:", type="password")
display_ui()

