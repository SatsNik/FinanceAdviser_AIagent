import json
from vector_store import add_documents, get_collection

def load_data_if_needed():
    collection = get_collection("finwise_knowledge_base")
    if collection.count() == 0:
        print("📂 Vector store empty — loading final_knowledge_base.json ...")
        with open("data/final_knowledge_base.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        documents = [" ".join(str(v) for v in item.values() if isinstance(v, str)) for item in data]
        ids = [f"doc_{i}" for i in range(len(documents))]
        add_documents("finwise_knowledge_base", documents, ids)
        print(f"✅ Loaded {len(documents)} documents into the vector store.")
    else:
        print("✅ Vector store already has data.")

if __name__ == "__main__":
    load_data_if_needed()
