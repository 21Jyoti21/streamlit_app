import streamlit as st
from langchain_community.llms import OpenAI

st.title('🦜🔗 Quickstart App')

openai_api_key = st.sidebar.text_input('OpenAI API Key', type="password")

def generate_response(input_text):
    if not openai_api_key.startswith("sk-"):
        st.error("Please enter a valid OpenAI API key!")
        return
    try:
        llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
        st.info(llm(input_text))
    except Exception as e:
        st.error(f"Error: {e}")

with st.form('my_form'):
    text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
    submitted = st.form_submit_button('Submit')
    if submitted:
        generate_response(text)
