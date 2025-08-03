import streamlit as st
from main import handle_file_upload

st.set_page_config(page_title="Medical Report Summarizer", layout="centered")
st.title("🩺 Medical Report Summarizer")

handle_file_upload()
