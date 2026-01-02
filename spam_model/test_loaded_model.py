import joblib

model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

email = "Shop for what you’ve wanted all season"
email_vec = vectorizer.transform([email])
prediction = model.predict(email_vec)

print("Spam " if prediction[0] == 1 else "Not Spam ")
