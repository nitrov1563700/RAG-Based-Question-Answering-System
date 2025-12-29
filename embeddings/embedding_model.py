from langchain_community.embeddings import HuggingFaceEmbeddings    

def load_embeddings(model_name):
    return HuggingFaceEmbeddings(model_name=model_name)