import json
from vector_store import add_documents

# Load your JSON
with open("data/final_knowledge_base.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Extract the meaningful text values
documents = []
for item in data:
    # You can pick the right fields here
    # Example: take all values and join them
    doc_text = " ".join(str(v) for v in item.values() if isinstance(v, str))
    documents.append(doc_text)

# Generate unique IDs
ids = [f"doc_{i}" for i in range(len(documents))]

# Add to vector DB
add_documents("finwise_knowledge_base", documents, ids)

print(f"✅ Loaded {len(documents)} documents into the vector store.")
