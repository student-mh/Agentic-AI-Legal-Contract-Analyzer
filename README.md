📄 Agentic AI Legal Contract Analyzer

An Agentic AI-powered legal contract analysis system that automatically extracts clauses, detects risks, generates improvement suggestions, summarizes contracts, and verifies compliance with DPDP (India) regulations using a Retrieval-Augmented Generation (RAG) pipeline.

Built using LangChain, Mistral (via Ollama), FAISS, HuggingFace embeddings, and Streamlit.


🚀 Features
✅ Upload PDF contracts
✅ Extract key legal clauses automatically
✅ Detect risky or vague contract terms
✅ Generate improvement suggestions
✅ Summarize contracts in plain English
✅ Check DPDP compliance using RAG
✅ Generate downloadable structured PDF reports
✅ Run LLM locally using Mistral via Ollama (privacy-preserving)

🧩 How RAG Works in This Project

The system checks compliance using a Retrieval-Augmented Generation pipeline:

Convert contract clauses into embeddings
Retrieve relevant DPDP/GDPR law sections from FAISS
Inject retrieved context into LLM prompt
Generate compliance verdict using Mistral

This ensures legally grounded responses instead of generic LLM predictions.
