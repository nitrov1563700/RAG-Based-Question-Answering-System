from pypdf import PdfReader
import os

def load_pdf(folder_path):
    documents = []
    for file in os.listdir(folder_path):
        if file.endswith('.pdf'):
            file_path = os.path.join(folder_path, file)
            try:
                reader = PdfReader(file_path)
                for page in reader.pages:
                    text = page.extract_text()
                    if text.strip():  # Only add non-empty text
                        documents.append(text)
            except Exception as e:
                print(f"Warning: Could not read {file}: {e}")
                continue
    return documents
