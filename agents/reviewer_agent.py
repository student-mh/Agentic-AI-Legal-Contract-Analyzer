def review_outputs(clauses, risks, suggestions, summary, dpdp_result, gdpr_result):
    def score(label, content, min_len):
        if not content or len(content.strip()) < min_len:
            return 2, f"{label} too short"
        elif "no" in content.lower():
            return 3, f"{label} may lack depth"
        return 5, f"{label} looks good"

    results = []

    scores = {
        "Clauses": score("Clauses", clauses, 100),
        "Risks": score("Risks", risks, 50),
        "Suggestions": score("Suggestions", suggestions, 50),
        "Summary": score("Summary", summary, 100),
        "DPDP": score("DPDP", dpdp_result, 30),
        "GDPR": score("GDPR", gdpr_result, 30),
    }

    for k, (s, msg) in scores.items():
        results.append(f"{k}: {s}/5 - {msg}")

    overall = all(s >= 4 for s, _ in scores.values())

    status = "✅ PASS" if overall else "❌ NEEDS IMPROVEMENT"

    return status + "\n\n" + "\n".join(results)