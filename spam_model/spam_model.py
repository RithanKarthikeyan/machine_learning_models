import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# 1. Load labeled data
df = pd.read_csv("spam.csv")

X = df["text"]      # raw email text (no format needed)
y = df["label"]     # human decision: 1 spam, 0 not spam

# 2. Convert text → numbers
vectorizer = TfidfVectorizer(stop_words="english")
X_vec = vectorizer.fit_transform(X)

# 3. Train model
model = LogisticRegression()
model.fit(X_vec, y)

# 4. Save model + vectorizer
joblib.dump(model, "spam_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Model and vectorizer saved successfully")
