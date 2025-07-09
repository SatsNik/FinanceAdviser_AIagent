from vector_store import query_collection

def get_relevant_documents(query, top_k=5):
    results = query_collection(collection_name="finwise_knowledge_base", query_texts=[query], top_k=top_k)
    documents = results.get('documents', [[]])[0]
    return documents

# Example test
if __name__ == "__main__":
    docs = get_relevant_documents("best life insurance plans", top_k=3)
    for i, doc in enumerate(docs, 1):
        print(f"{i}. {doc}")
