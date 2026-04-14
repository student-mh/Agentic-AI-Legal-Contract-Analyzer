from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM
from langchain_core.runnables import RunnableSequence

def get_risk_detector_chain():
    prompt = PromptTemplate.from_template(
        "Analyze the following contract for vague, missing, or risky clauses and explain the issues:\n\nText:\n{contract}"
    )
    llm = OllamaLLM(model="mistral")
    chain = prompt | llm
    return chain

def detect_risks(text):
    chain = get_risk_detector_chain()
    return chain.invoke({"contract": text})