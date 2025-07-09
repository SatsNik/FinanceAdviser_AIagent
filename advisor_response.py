# # advisor_response.py

from vector_store import query_collection
from api_model_integration import generate_response

def get_advice(user_query):
    # Step 1: Query from Vector Store
    results = query_collection("finwise_knowledge_base", [user_query], top_k=3)
    documents = results.get("documents", [[]])[0]

    # Step 2: Fallback if no documents found
    if not documents:
        return "Sorry, I couldn't find anything relevant."

    # Check documents for debugging
    print("📑 Documents from Vector Store:", documents)

    # Step 3: Generate response from Gemini
    try:
        print("🚀 Calling Gemini now...")
        response = generate_response(user_query, documents)
        print("✅ Gemini responded")
        return response
    except Exception as e:
        # Fallback to showing raw context
        print("❌ Gemini Error:", str(e))
        fallback = "\n".join(f"- {doc}" for doc in documents)
        return f"Here's what I found:\n{fallback}"


# def get_advice(user_query):
#     # Step 1: Query from Vector Store
#     results = query_collection("finwise_knowledge_base", [user_query], top_k=3)
#     documents = results.get("documents", [[]])[0]

#     # Step 2: Fallback if no documents found
#     if not documents:
#         return "Sorry, I couldn't find anything relevant."

#     # Step 3: Generate response from Gemini
#     try:
#         response = generate_response(user_query, documents)
#         return response
#     except Exception as e:
#         # Fallback to showing raw context
#         fallback = "\n".join(f"- {doc}" for doc in documents)
#         return f"Here's what I found:\n{fallback}"
