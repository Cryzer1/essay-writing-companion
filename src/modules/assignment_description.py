import streamlit as st

def get_assignment_description():
    """Get assignment description from the user."""
    
    assignment_description = st.text_area("Enter your essay assignment description:", "")
    
    if assignment_description:
        st.success("Assignment description saved.")
    else:
        st.warning("Please enter the assignment description.")
    
    return assignment_description