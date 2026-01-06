from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib

# Load model & vectorizer
model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

app = FastAPI(
    title="Email Classification API",
    version="1.0"
)

# CORS for Chrome extension
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class EmailInput(BaseModel):
    text: str

class PredictionOutput(BaseModel):
    label: str
    confidence: float

# Promotion keywords (RULE-BASED LAYER)
PROMO_KEYWORDS = [
    "shop", "save", "deal", "offer",
    "sale", "new", "exclusive", "gift",
    "discount", "limited", "upgrade", "free"
]

@app.get("/")
def root():
    return {"status": "API is running"}

@app.post("/predict", response_model=PredictionOutput)
def predict_email(data: EmailInput):
    text = data.text.lower()

    # 🔹 RULE 1: Promotion override
    if any(word in text for word in PROMO_KEYWORDS):
        return {
            "label": "promotion",
            "confidence": 90.0
        }

    # 🔹 RULE 2: ML prediction
    email_vector = vectorizer.transform([data.text])
    prediction = model.predict(email_vector)[0]
    probabilities = model.predict_proba(email_vector)[0]

    label_map = {
        0: "not_spam",
        1: "spam",
        2: "promotion"
    }

    return {
        "label": label_map[prediction],
        "confidence": round(max(probabilities) * 100, 2)
    }
