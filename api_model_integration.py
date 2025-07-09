# api_model_integration.py

import os
from dotenv import load_dotenv
from google.generativeai import GenerativeModel, configure

# Load the .env file
load_dotenv()

# Get the Gemini API key from environment variables
api_key = os.getenv("GEMINI_API_KEY")

# Configure the Gemini API
configure(api_key=api_key)
print("Gemini API Key is:", api_key)

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






# # list_gemini_models.py
# from dotenv import load_dotenv
# import os
# import google.generativeai as genai  # Or use google_genai

# load_dotenv()
# genai.configure(api_key=os.getenv("GEMINI_API_KEY"), transport="grpc")

# def list_models():
#     for m in genai.list_models():
#         if "generateContent" in getattr(m, "supported_generation_methods", []):
#             print(f"- {m.name}  |  {m.description}")

# if __name__ == "__main__":
#     list_models()





# api_model_integration.py

# import os
# import openai
# from dotenv import load_dotenv

# load_dotenv()

# # Load OpenAI API Key
# openai.api_key = os.getenv("OPENAI_API_KEY")
# print("OpenAI API Key is:", openai.api_key)  # Just for testing, remove later.

# models = openai.Model.list()
# for model in models.data:
#     print(model.id)

# def generate_response(user_query, documents):
#     context = "\n".join(documents)

#     prompt = f"""
#     You are a financial advisor chatbot. Use the following context to answer the user's query.

#     Context:
#     {context}

#     User's question: {user_query}

#     Give a helpful and clear answer in a professional tone.
#     """

#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",  # or "gpt-3.5-turbo"
#         messages=[
#             {"role": "system", "content": "You are a helpful financial advisor."},
#             {"role": "user", "content": prompt}
#         ]
#     )

#     return response["choices"][0]["message"]["content"].strip()
