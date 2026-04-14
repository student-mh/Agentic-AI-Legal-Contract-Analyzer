from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM  # ← Use new supported Ollama interface
from langchain_core.runnables import RunnableSequence  # Future-proof chaining

def get_suggestion_agent():
    prompt = PromptTemplate.from_template(
        "Based on best practices, suggest edits for this contract:\n\n{contract}"
    )
    llm = OllamaLLM(model="mistral")  # 🧠 Local Mistral model via Ollama
    return prompt | llm  # Use RunnableSequence

def suggest_edits(text):
    chain = get_suggestion_agent()
    return chain.invoke({"contract": text})