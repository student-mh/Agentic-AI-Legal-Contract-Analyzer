from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader

def create_dpdp_index():
    loader = PyPDFLoader("data/dpdp.pdf")  # Ensure this PDF is the full DPDP Act 2023
    documents = loader.load()
    
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(documents)

    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_db = FAISS.from_documents(chunks, embedding_model)
    
    vector_db.save_local("dpdp_embeddings")  # Use "dpdp_embeddings" to match main.py
    print("[+] DPDP FAISS index saved successfully.")

if __name__ == "__main__":
    create_dpdp_index()