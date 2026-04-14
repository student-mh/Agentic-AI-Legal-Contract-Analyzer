main.py
from utils.pdf_reader import extract_text_from_pdf
from agents.clause_extractor import extract_clauses
from agents.risk_detector import detect_risks
from agents.suggestion_agent import suggest_edits
from agents.summary_agent import summarize_contract

def run_contract_analysis(pdf_path):
    print("🔍 Extracting text...")
    text = extract_text_from_pdf(pdf_path)

    print("\n📌 Extracting clauses...")
    clauses = extract_clauses(text)
    print(clauses)

    print("\n⚠️ Detecting risks...")
    risks = detect_risks(text)
    print(risks)

    print("\n🛠 Suggesting edits...")
    suggestions = suggest_edits(text)
    print(suggestions)

    print("\n📝 Summarizing contract...")
    summary = summarize_contract(text)
    print(summary)

if __name__ == "__main__":
    run_contract_analysis("data/ArmstrongFlooringInc_20190107_8-K_EX-10.2_11471795_EX-10.2_Intellectual Property Agreement.pdf")
