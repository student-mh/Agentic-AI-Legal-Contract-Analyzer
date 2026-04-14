# main.py (updated)
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
import ollama

def check_dpdp_compliance(clause_text):
    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_db = FAISS.load_local("dpdp_nag_checker/embeddings", embedding_model, allow_dangerous_deserialization=True)

    docs = vector_db.similarity_search(clause_text, k=3)
    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are an expert in Indian data privacy law, specifically the Digital Personal Data Protection Act (DPDP) 2023.

Based on the DPDP excerpts below, determine whether the clause complies with the law. Provide a short verdict and a brief explanation citing relevant principles.

Clause:
\"\"\"{clause_text}\"\"\"

Relevant DPDP Context:
\"\"\"{context}\"\"\"
"""

    response = ollama.chat(model='mistral', messages=[{"role": "user", "content": prompt}])
    return response['message']['content']