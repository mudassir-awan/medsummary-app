import streamlit as st
from utils.pdf_reader import extract_text_from_pdf
from utils.summarizer import get_summary

def handle_file_upload():
    uploaded_file = st.file_uploader("Upload a medical report (PDF)", type=["pdf"])
    
    if uploaded_file:
        text = extract_text_from_pdf(uploaded_file)
        if not text.strip():
            st.error("Could not extract text. Try another PDF.")
            return

        with st.spinner("Summarizing..."):
            summary = get_summary(text)
        st.subheader("Summary:")
        st.write(summary)
