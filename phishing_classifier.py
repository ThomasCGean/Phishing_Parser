# phishing_classifier.py

import torch
from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification
from config import MODEL_DIR, CONFIDENCE_THRESHOLD

class PhishingEmailClassifier:
    def __init__(self, model_dir: str = MODEL_DIR, threshold: float = CONFIDENCE_THRESHOLD):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = DistilBertTokenizerFast.from_pretrained(model_dir)
        self.model = DistilBertForSequenceClassification.from_pretrained(model_dir)
        self.model.to(self.device)
        self.model.eval()
        self.threshold = threshold

    def predict(self, subject: str, body: str) -> dict:
        """
        Returns prediction result for a given email.
        Expects raw subject and body text (cleaning handled externally).
        """
        from preprocessing import clean_subject_and_body  # Lazy import to avoid circular dependency
        cleaned_text = clean_subject_and_body(subject, body)

        # Tokenize
        inputs = self.tokenizer(
            cleaned_text,
            return_tensors="pt",
            truncation=True,
            padding=True,
            max_length=256
        )
        inputs = {k: v.to(self.device) for k, v in inputs.items()}

        # Predict
        with torch.no_grad():
            outputs = self.model(**inputs)
            logits = outputs.logits
            probs = torch.softmax(logits, dim=1).cpu().numpy()[0]

        pred_label = int(probs[1] >= self.threshold)
        confidence = float(probs[pred_label])

        return {
            "label": "phishing" if pred_label == 1 else "legitimate",
            "confidence": confidence,
            "probabilities": {
                "legitimate": float(probs[0]),
                "phishing": float(probs[1])
            }
        }
