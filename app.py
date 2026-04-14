import streamlit as st
import fitz  # PyMuPDF
from agents.clause_extractor import extract_clauses
from agents.risk_detector import detect_risks
from agents.suggestion_agent import suggest_edits
from agents.summary_agent import summarize_contract
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import tempfile
import textwrap
import os
from dpdp_checker import check_dpdp_compliance

def generate_pdf_report(clauses, risks, suggestions, summary):
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    c = canvas.Canvas(temp_file.name, pagesize=letter)
    width, height = letter
    margin = 40
    line_height = 14
    max_width = width - 2 * margin

    text_object = c.beginText(margin, height - margin)
    text_object.setFont("Helvetica", 11)

    def add_wrapped_text(text, indent=0):
        nonlocal text_object
        wrapper = textwrap.TextWrapper(width=95)  # Adjust based on font size
        for line in text.split('\n'):
            wrapped = wrapper.wrap(line)
            for wrap_line in wrapped:
                if text_object.getY() < margin:
                    c.drawText(text_object)
                    c.showPage()
                    text_object = c.beginText(margin, height - margin)
                    text_object.setFont("Helvetica", 11)
                text_object.textLine(" " * indent + wrap_line)
            text_object.textLine("")  # Add spacing

    sections = {
        "📌 Clauses": clauses,
        "⚠️ Risks": risks,
        "🛠 Suggestions": suggestions,
        "🧾 Summary": summary,
    }

    for title, content in sections.items():
        text_object.textLine(title)
        text_object.textLine("-" * 70)
        add_wrapped_text(content)

    c.drawText(text_object)
    c.save()
    return temp_file.name
st.title("📄 Contract Analyzer AI")

uploaded_file = st.file_uploader("Drag and drop a PDF contract", type=["pdf"])

if uploaded_file:
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    full_text = "\n".join([page.get_text() for page in doc])

    st.subheader("🔍 Contract Text Preview")
    st.text_area("Contract Text", full_text, height=300)

    if st.button("Run Analysis"):
        with st.spinner("Extracting clauses..."):
            st.session_state.clauses = extract_clauses(full_text)
        with st.spinner("Detecting risks..."):
            st.session_state.risks = detect_risks(full_text)
        with st.spinner("Generating suggestions..."):
            st.session_state.suggestions = suggest_edits(full_text)
        with st.spinner("Summarizing..."):
            st.session_state.summary = summarize_contract(full_text)

    if "clauses" in st.session_state:
        st.subheader("📌 Clauses")
        st.write(st.session_state.clauses)

        st.subheader("⚠️ Risks")
        st.write(st.session_state.risks)

        st.subheader("🛠 Suggestions")
        st.write(st.session_state.suggestions)

        st.subheader("🧾 Summary")
        st.write(st.session_state.summary)

        if st.button("🔐 Check DPDP Compliance"):
            with st.spinner("Running DPDP compliance check..."):
                dpdp_result = check_dpdp_compliance(st.session_state.summary)
            st.subheader("📋 DPDP Compliance Result")
            st.markdown(dpdp_result)

        
        if st.button("📄 Generate PDF Report"):
            pdf_path = generate_pdf_report(
                st.session_state.clauses,
                st.session_state.risks,
                st.session_state.suggestions,
                st.session_state.summary
            )
            with open(pdf_path, "rb") as f:
                st.download_button("⬇️ Download Contract Report", f, file_name="contract_analysis_report.pdf", mime="application/pdf")
