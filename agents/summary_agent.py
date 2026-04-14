from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM  # ← Updated import
from langchain_core.runnables import RunnableSequence  # For chaining prompt | llm

def get_summary_agent():
    prompt = PromptTemplate.from_template(
        "Summarize the following legal contract in plain language:\n\n{contract}"
    )
    llm = OllamaLLM(model="mistral")  # ← Local Mistral via Ollama
    return prompt | llm  # New chaining method

def summarize_contract(text):
    chain = get_summary_agent()
    return chain.invoke({"contract": text})  # ← Updated from .run()