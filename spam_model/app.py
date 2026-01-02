from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib

model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

app = FastAPI(title="Spam Email Classifier")

# ✅ ADD THIS CORS CONFIG
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all (for local dev)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class EmailInput(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "Spam Classifier API is running"}

@app.post("/predict")
def predict_spam(data: EmailInput):
    email_vec = vectorizer.transform([data.text])
    prediction = model.predict(email_vec)

    return {
        "prediction": "spam" if prediction[0] == 1 else "not spam"
    }
