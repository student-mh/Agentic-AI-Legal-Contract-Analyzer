def check_gdpr_compliance(text):
    if "consent" in text.lower():
        return "✅ GDPR compliant."
    return "❌ GDPR violation risk."