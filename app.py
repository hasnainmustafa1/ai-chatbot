import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="🤖 AI Chatbot (Gemini)")

st.title("🤖 AI Chatbot (Gemini)")
user_input = st.text_input("Apna sawal likho aur AI se jawab lo")

# Configure Gemini
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")

if user_input:
    try:
        response = model.generate_content(user_input)
        st.success(response.text)
    except Exception as e:
        st.error("Gemini API error aaya 😥")
        st.exception(e)
