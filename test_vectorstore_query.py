from vector_store import query_collection

query = "Best life insurance plans for a 30 year old"
results = query_collection("finwise_knowledge_base", [query], top_k=5)

for i, doc in enumerate(results.get("documents", [[]])[0]):
    print(f"[{i+1}] {doc}")
