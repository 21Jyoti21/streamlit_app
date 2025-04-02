import streamlit as st
from transformers import pipeline

# Specify the local directory where you downloaded the model
model_path = r"C:\Users\jyoti\Downloads\lk"

# Load the summarization pipeline
summarizer = pipeline("summarization", model=model_path)

# Streamlit app
st.set_page_config(page_title='📝 Local Summarizer')
st.title("📝 Local Text Summarization")

# Text input
text = st.text_area("Enter text for summarization:", height=200)

if st.button("Summarize"):
    if text.strip():
        max_len = max(10, len(text.split()) - 2)  # Ensure reasonable max_length
        summary = summarizer(text, max_length=max_len, min_length=5, do_sample=False)
        st.subheader("Summary:")
        st.write(summary[0]['summary_text'])
    else:
        st.warning("Please enter some text to summarize.")