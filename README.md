# 📧✨ Email Spam Detector – Chrome Extension

![Python](https://img.shields.io/badge/Python-ML-blue)
![scikit-learn](https://img.shields.io/badge/scikit--learn-Model-orange)
![Chrome Extension](https://img.shields.io/badge/Chrome-Extension-green)
![Status](https://img.shields.io/badge/Status-Working-success)

---

## 🔍 Overview

This project is an **Email Spam Detection system** that uses a **Machine Learning model** to classify emails as **Spam** or **Safe**, and integrates the model into a **Chrome Extension** for real-time usage.

Simply activate the extension, open an email, and get instant spam detection results 🚀

---

## 🧠 How It Works

🟢 The **ML model** is trained using labeled email data  
🟢 Text features are extracted and classified using **scikit-learn**  
🟢 The trained model is connected to a **Chrome Extension**  
🟢 When an email is opened, the extension predicts:
- ✅ Safe  
- 🚫 Spam
- 💲Promotional

---

## 📂 Project Structure
machine_learning_models/
├── spam_model/ # Machine Learning model (training & prediction)
└── spam_chrome_extension/ # Chrome extension file

