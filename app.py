import streamlit as st
from google import genai

st.set_page_config(page_title="AI Chatbot (Gemini)")

st.title("🤖 AI Chatbot (Gemini)")
user_input = st.text_input("Apna sawal likho aur AI se jawab lo")

# Gemini client
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

if user_input:
    try:
        response = client.models.generate_content(
            model="gemini-1.5-flash-001",
            contents=user_input
        )

        st.success(response.text)

    except Exception as e:
        st.error("Gemini API error aaya 😥")
        st.code(str(e))

