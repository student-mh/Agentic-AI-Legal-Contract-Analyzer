from haystack.nodes import TransformersDocumentClassifier

def classify_text(text):
    # Placeholder for a real classifier
    classifier = TransformersDocumentClassifier(model_name_or_path="distilbert-base-uncased")
    result = classifier.run(documents=[{"content": text}])
    return result