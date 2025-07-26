# ✈️ Airline Passenger Satisfaction Prediction

## 📌 Introduction  
Air travel is one of the fastest and most premium modes of transportation. However, it involves several formalities — such as passport verification, visa approvals, ticketing, and boarding — which can impact the passenger experience. Due to these complexities, passengers often prefer airlines that provide efficient and comfortable services.

To understand and enhance customer satisfaction, airlines collect feedback from passengers. Analyzing this data helps in improving overall service quality.

---

## 🎯 Project Objective  
The primary goal of this project is to **predict whether a passenger is *Satisfied* or *Dissatisfied*** with their flight experience using a Machine Learning model.

---

## 📊 Key Factors Considered  
- Ticketing and Boarding Services  
- Baggage Handling  
- Seat Comfort and Legroom  
- In-flight Wi-Fi  
- Onboard Services  
- Airport Facilities  

---

## 🤖 How the Model Helps  
- Identifies the major factors influencing passenger satisfaction  
- Predicts satisfaction level based on survey responses  
- Enables airlines to make **data-driven decisions** to enhance customer experience  

---

## 🧠 Machine Learning Workflow  
1. **Data Cleaning and Preprocessing**  
2. **Exploratory Data Analysis (EDA)**  
3. **Feature Selection** using *Recursive Feature Elimination (RFE)*  
4. **Model Training**
   - Logistic Regression  
   - Random Forest  
   - (Other models optional)  
5. **Model Evaluation**
   - Accuracy  
   - F1-score  
   - Confusion Matrix  
6. **Deployment** using *Streamlit*

---

## 🚀 Deployment Note  
The trained ML model is hosted on **Google Drive** due to GitHub's file size limitations. The model file will be **automatically downloaded** when the app starts.

---

## 🛠️ Tech Stack  
- Python  
- Pandas, NumPy  
- Scikit-learn  
- Matplotlib, Seaborn  
- Streamlit  

---
## 📁 Project Structure  
├── app.py # Streamlit web app
├── model.pkl # Trained ML model (downloaded from Google Drive)
├── requirements.txt # Python dependencies
├── dataset.csv # Airline passenger feedback dataset
├── eda.ipynb # EDA and preprocessing notebook
└── README.md # Project documentation
