import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("API_KEY"))

model = genai.GenerativeModel(
    "gemini-1.5-flash",
    system_instruction="your name is gemma, you are a travel assistant"
)

st.title("Gemini Chatbot")
st.write("Ask travel questions!")

# Initialize chat session and message history
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**Gemma:** {msg['content']}")

# Placing the text_input inside a form to clear it after submission
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("You:")
    submitted = st.form_submit_button("Send")

if submitted:
    if user_input:
        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": user_input})
        # bot response
        response = st.session_state.chat.send_message(user_input)
        st.session_state.messages.append({"role": "bot", "content": response.text})
        st.rerun()
    else:
        st.warning("Please enter a message.")
