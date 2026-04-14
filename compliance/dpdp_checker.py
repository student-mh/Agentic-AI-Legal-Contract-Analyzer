def check_dpdp_compliance(text):
    if "personal data" in text.lower():
        return "✅ Likely DPDP compliant."
    return "❌ Not DPDP compliant."