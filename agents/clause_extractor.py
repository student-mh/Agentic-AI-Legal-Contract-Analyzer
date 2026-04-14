from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM  # ✅ New correct import
from langchain_core.runnables import RunnableSequence

def get_clause_extractor_chain():
    prompt = PromptTemplate.from_template(
        "Extract the following clauses from the contract: indemnity, arbitration, termination.\n\nText:\n{contract}"
    )
    llm = OllamaLLM(model="mistral")  # ✅ New class
    chain = prompt | llm  # ✅ RunnableSequence
    return chain

def extract_clauses(text):
    chain = get_clause_extractor_chain()
    return chain.invoke({"contract": text})