from langchain_community.vectorstores import FAISS

def load_retriever(embeddings,faiss_path , top_k):
    db = FAISS.load_local(
        faiss_path,
        embeddings,
        allow_dangerous_deserialization=True
    )

    return db.as_retriever(search_kwargs = {"k":top_k})