from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_text(texts,chunk_size,chunk_overlap):
    splitter= RecursiveCharacterTextSplitter(
    chunk_size = chunk_size,
    chunk_overlap = chunk_overlap
    )
    return splitter.create_documents(texts)