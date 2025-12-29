from langchain_community.vectorstores import FAISS

def build_faiss_index(documents, embeddings,save_path):
    db = FAISS.from_documents(documents, embeddings)
    db.save_local(save_path)
    return db