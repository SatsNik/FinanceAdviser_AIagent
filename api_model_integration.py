# api_model_integration.py

import os
# from dotenv import load_dotenv
from google.generativeai import GenerativeModel, configure
import streamlit as st

api_key = st.secrets["api_keys"]["gemini"]

# Load the .env file
# load_dotenv()
# 
# Get the Gemini API key from environment variables
# Configure the Gemini API
configure(api_key=api_key)
# print("Gemini API Key is:", api_key)

def generate_response(user_query, documents):
    context = "\n".join(documents)

    prompt = f"""
    You are a financial advisor chatbot. Use the following context to answer the user's query.

    Context:
    {context}

    User's question: {user_query}

    Give a helpful and clear answer in a professional tone.
    """

    print("📨 Calling Gemini with prompt:\n", prompt[:300], "...\n")  # Truncate to 300 chars

    model = GenerativeModel(model_name="models/gemini-2.0-flash-lite")
    # response = model.generate_content(prompt)
    # print("✅ Gemini Response Received")
    # return response.text.strip()
    response = model.generate_content(prompt)
    print("Gemini raw response:", response)
    if hasattr(response, "text"):
        return response.text.strip()
    elif hasattr(response, "candidates"):
        return response.candidates[0].content.parts[0].text.strip()
    else:
        return "No valid response found."



