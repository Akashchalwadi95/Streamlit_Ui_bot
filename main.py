import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("API_KEY"))

# Load Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

def chatbot():
    print("Gemini Chatbot ready! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        response = model.generate_content(user_input)
        print("Bot:", response.text)

chatbot()
