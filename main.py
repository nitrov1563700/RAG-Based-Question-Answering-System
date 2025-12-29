import yaml 
from embeddings.embedding_model import load_embeddings
from llm.llama2_loader import load_llm
from pipelines.retrieval_pipeline import load_retriever
from rag.rag_chain import create_rag_chain

with open("config/config.yaml") as f:
    config = yaml.safe_load(f)

def main():
    embeddings = load_embeddings(config["embedding_model"])
    retriever = load_retriever(
        embeddings,
        config["faiss_path"],
        config["top_k"])
    llm = load_llm(config["llm_model"])
    rag_chain = create_rag_chain(llm, retriever)

    while True:
        query = input("\nAsk a question (type 'exit' to quit):")
        if query.lower() == 'exit':
            break
        result = rag_chain.invoke(query)
        print("\nAnswer:\n", result["result"])
if __name__ == "__main__":
    main() 