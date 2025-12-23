import streamlit as st
from google.genai import Client

st.set_page_config(page_title="🤖 AI Chatbot (Gemini)")
st.title("🤖 AI Chatbot (Gemini)")

user_input = st.text_input("Apna sawal likho aur AI se jawab lo")

# ✅ NEW SDK client
client = Client(api_key=st.secrets["GEMINI_API_KEY"])

if user_input:
    try:
        response = client.models.generate_content(
            model="models/gemini-flash-latest",
            contents=user_input
        )
        st.success(response.text)

    except Exception as e:
        st.error("Gemini API error aaya 😥")
        st.exception(e)
