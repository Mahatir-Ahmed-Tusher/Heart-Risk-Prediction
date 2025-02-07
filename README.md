![logo](https://github.com/user-attachments/assets/13e7daa8-14fc-4056-97e9-351abdd808d9)


# EarlyMed Heart Risk Prediction  

This project is a **Heart Disease Risk Prediction Web App** developed as part of the **EarlyMed Initiative**, a student-driven project by students of **Vellore Institute of Technology (VIT-AP)**. EarlyMed aims to leverage **machine learning** and **data science** for the early detection and prevention of chronic diseases.

## 🔥 Live Deployment
👉 **Check out the live app here:** [EarlyMed Heart Risk Prediction](https://earlymed-heart-risk-predictionn.onrender.com/)

## 📂 Repository Structure
```
├── /myenv
│   ├── /Lib/site-packages
│   ├── /Scripts
│   ├── .gitignore
│   ├── pyenv.cfg
├── /templates
│   ├── index.html
├── .gitignore
├── app.py
├── model.pkl
├── requirements.txt
├── Heart_Risk_Prediction.ipynb
```

## 📊 Overview of the Dataset
This project uses a **custom-built synthetic dataset** to predict the risk of heart disease based on symptoms, lifestyle factors, and medical history.

- 📌 **Dataset Download Link:** [Kaggle](https://www.kaggle.com/datasets/mahatiratusher/heart-disease-risk-prediction-dataset)
- 🏥 **Total Samples:** 70,000
- 🔬 **Features:** Binary indicators (Yes/No) for symptoms, along with a computed risk label.
- 🚀 **Goal:** Train ML models for **predictive modeling in cardiovascular health**.
- 🏫 **Developed by:** Students from **Vellore Institute of Technology (VIT-AP)** as part of the **EarlyMed initiative**.

## 🚀 Web App Capabilities
- The web app allows users to enter their **symptoms and lifestyle factors**.
- Features are input in **binary format (1 for Yes, 0 for No)** except for **weight**.
- Based on inputs, the app **predicts if the user is at risk of heart disease**.
- Powered by a **Random Forest Regressor Model** with high accuracy.

## 📌 Model Features
The model takes the following **10 features** as input:
1. `pain_arms_jaw_back`
2. `age`
3. `cold_sweats_nausea`
4. `chest_pain`
5. `fatigue`
6. `dizziness`
7. `swelling`
8. `shortness_of_breath`
9. `palpitations`
10. `sedentary_lifestyle`

## 🎯 Model Performance
✅ **Final R² Score:** 0.9541  
✅ **Mean Absolute Error:** 0.0594  
✅ **Mean Squared Error:** 0.0459  
✅ **Root Mean Squared Error:** 0.2143  

## 🛠 Setup & Installation
**Step 1:** Clone the repository:
```bash
git clone https://github.com/Mahatir-Ahmed-Tusher/Heart-Risk-Prediction.git
cd Heart-Risk-Prediction
```

**Step 2:** Create a virtual environment:
```bash
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate
```

**Step 3:** Install dependencies:
```bash
pip install -r requirements.txt
```

**Step 4:** Run the Flask app:
```bash
python app.py
```

App should now be running at `http://127.0.0.1:5000/` 🎉

## 🖥 Deployment on Render
The project is **deployed on Render** for easy access and scalability.

## 👨‍💻 Contribution
This project is **open for contributions!** If you'd like to improve the model, UI, or add new features:
- Fork the repository.
- Create a feature branch (`git checkout -b feature-name`).
- Commit your changes (`git commit -m "Added feature"`).
- Push to the branch (`git push origin feature-name`).
- Create a pull request!

## 📧 Contact
Developed by **Mahatir Ahmed Tusher**. Feel free to reach out!
- 📩 **Email:** mahatirtusher@gmail.com
- 🌍 **GitHub:** [Mahatir-Ahmed-Tusher](https://github.com/Mahatir-Ahmed-Tusher)

---
### ⚡ EarlyMed: Empowering Health Through AI & Data Science
**"Detect Early, Prevent Early!"**
