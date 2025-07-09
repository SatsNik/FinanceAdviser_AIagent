# vector_store.py
import chromadb
from chromadb.utils import embedding_functions

# ------------------- Initialize Persistent Chroma Client -------------------
client = chromadb.PersistentClient(path="./chroma_db")

# ------------------- HuggingFace SentenceTransformer Model -------------------
hf_embed_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# ------------------- Create / Get Collection -------------------
def get_collection(name="finwise_knowledge_base"):
    return client.get_or_create_collection(
        name=name,
        embedding_function=hf_embed_fn
    )

# ------------------- Add Documents -------------------
def add_documents(collection_name, documents, ids, metadatas=None):
    collection = get_collection(collection_name)
    collection.add(
        documents=documents,
        ids=ids,
        metadatas=metadatas
    )
    print(f"[✔] Added {len(documents)} documents to '{collection_name}' collection.")

# ------------------- Query Collection -------------------
def query_collection(collection_name, query_texts, top_k=5):
    collection = get_collection(collection_name)
    results = collection.query(
        query_texts=query_texts,
        n_results=top_k
    )
    return results

# ------------------- Example Test -------------------
if __name__ == "__main__":
    # Example data
    docs = ["Life insurance covers financial risks in case of death."]
    ids = ["life1"]
    metas = [{"category": "insurance", "subcategory": "life_insurance"}]

    # Add documents
    add_documents("finwise_insurance", docs, ids, metas)

    # Example query
    query = "Tell me about life insurance."
    response = query_collection("finwise_insurance", [query], top_k=2)

    print("[✔] Query Results:")
    print(response)
