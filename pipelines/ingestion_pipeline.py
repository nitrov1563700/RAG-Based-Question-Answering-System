import sys
import os
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

import yaml 
from utils.pdf_loader import load_pdf
from utils.text_splitter import split_text
from embeddings.embedding_model import load_embeddings
from vector_store.build_index import build_faiss_index

with open("config/config.yaml") as f:
    config = yaml.safe_load(f)
   
   
def run_ingestion():   
  texts = load_pdf(config["data_path"])
  documents = split_text(
      texts,
      config["chunk_size"],
      config["chunk_overlap"]
  )

  embeddings = load_embeddings(config["embedding_model"])
  build_faiss_index(
      documents,
      embeddings,
      config["faiss_path"]
  )

  print("Ingestion completed successfully.")

if __name__ == "__main__":
    run_ingestion()