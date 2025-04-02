import streamlit as st
from transformers import BartForConditionalGeneration, BartTokenizer

model_path = r"C:\Users\jyoti\Downloads\model2"

# Load the model and tokenizer
model = BartForConditionalGeneration.from_pretrained(model_path)
tokenizer = BartTokenizer.from_pretrained(model_path)

st.title("Text Summarization with BART")

text = st.text_area("Enter text to summarize", "Your long input text here")

if st.button("Summarize"):
    with st.spinner("Generating summary..."):
        inputs = tokenizer(text, return_tensors="pt", max_length=1024, truncation=True)
        summary_ids = model.generate(inputs['input_ids'], max_length=150, min_length=50, length_penalty=2.0, num_beams=4, early_stopping=True)
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    st.subheader("Summary:")
    st.write(summary)
