# 📊 PCOS Prediction Web App

A machine learning web app that predicts the likelihood of Polycystic Ovary Syndrome (PCOS) based on user-input health parameters. Built using **Streamlit**, powered by a **Support Vector Classifier (SVC)** model, and deployed for public use.

### 🚀 Live Demo  
🔗 [[Click to try]](https://pcospredictionwebapp-mtvgekxpx3z36y8eappj5r.streamlit.app/)

---

## 🔧 Features
- Real-time PCOS prediction based on health metrics
- User-friendly web interface using Streamlit
- Built-in visual feedback for better understanding
- Hosted online for accessible use

---

## 🛠️ Tech Stack
- **Frontend & Deployment**: Streamlit
- **Machine Learning**: Scikit-learn (SVC)
- **Data Handling**: Pandas, NumPy
- **Visualization**: Matplotlib
- **Deployment**: Streamlit Cloud

---

## 📁 Project Structure
```
├── implementation.py # Streamlit application code
├── pcod_model (1).sav # Trained SVC model
├── scaler.sav # Scaler used during preprocessing
├── requirements.txt # Python dependencies
├── LICENSE # Project license (MIT)
└── README.md # Project documentation
```

---

## 🧪 Dataset
- **Source**: [Kaggle PCOS Dataset](https://www.kaggle.com/datasets)
- **Features**: BMI, insulin, hormone levels, cycle length, etc.
- **Label**: PCOS diagnosis (yes/no)

---

## 🧠 How It Works
1. User inputs health data (BMI, insulin, FSH, LH, etc.)
2. Input is passed to a trained SVC model
3. The model outputs a prediction score
4. Streamlit displays the result with helpful visuals

---

## 📈 Model Performance
- The Support Vector Classifier (SVC) achieved:
  - **Training Accuracy**: 90.95%
  - **Test Accuracy**: 96.29%

---

## 💻 Run Locally
```bash
git clone https://github.com/roopashreerangaswamy/pcospredictionwebapp.git
cd pcospredictionwebapp
pip install -r requirements.txt
streamlit run pcospredict.py
```

---

## 💡 Future Enhancements
- Add classification models (e.g., Random Forest, Decision Tree)
- Upload patient history from Excel/CSV
- Downloadable prediction report
- Secure login for doctor/admin view

---

## 📄 License
MIT License – feel free to fork, modify, and use for educational purposes.

---

## 🙋‍♀️ Author
**Roopashree R.**  
💼 2026 CSE Undergrad  
🌐 [GitHub](https://github.com/roopashreerangaswamy) | 🔗 [LinkedIn](https://www.linkedin.com/in/roopashree-rangaswamy)
