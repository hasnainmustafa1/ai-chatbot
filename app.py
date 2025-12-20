import streamlit as st
from google.genai import Client

# Gemini Client
client = Client(api_key="PASTE_YOUR_API_KEY_HERE")

# Page title
st.set_page_config(page_title="AI Chatbot", page_icon="🤖")

st.title("🤖 AI Chatbot (Gemini)")
st.write("Apna sawal likho aur AI se jawab lo")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show old messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# User input
user_input = st.chat_input("Yahan apna sawal likhein...")

if user_input:
    # Show user message
    st.chat_message("user").write(user_input)
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    # Gemini response
    response = client.models.generate_content(
        model="models/gemini-pro-latest",
        contents=user_input
    )

    bot_reply = response.text

    # Show bot reply
    st.chat_message("assistant").write(bot_reply)
    st.session_state.messages.append(
        {"role": "assistant", "content": bot_reply}
    )
