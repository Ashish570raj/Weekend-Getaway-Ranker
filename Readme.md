
## 🏖️ Weekend Getaway Ranker

A **machine-learning powered recommendation system** that suggests the best weekend travel destinations based on **distance, popularity, and user ratings**.  
The project is built using **Python, Pandas, Scikit-learn**, and deployed as an interactive **Streamlit web app**.

---

## 🚀 Live Demo
https://weekend-getaway-ranker-bf7pwufcmmnjswgspvxfcq.streamlit.app/

---

## 📌 Problem Statement

Planning a short weekend trip can be challenging due to multiple factors like:
- How far the destination is
- How popular it is
- How well it is rated by visitors

This project solves the problem by **ranking tourist destinations dynamically** based on the user’s source city and recommending the **best weekend getaways**.
---

## 🧠 Solution Approach

The system uses a **ranking-based machine learning approach**:

- ⭐ **Google Review Rating** → quality of destination  
- 🔥 **Number of Google Reviews** → popularity  
- 📏 **Distance from source city** → travel feasibility (penalty)

A weighted scoring model combines these factors to generate personalized recommendations.

---

## ⚙️ Features

- Select **source city**
- Choose **number of recommendations**
- Dynamic distance calculation using **Haversine formula**
- Personalized ranking for each city
- Clean, user-friendly Streamlit interface
- Deployed on Streamlit Cloud

---

## 🛠️ Tech Stack

- **Language:** Python  
- **Data Processing:** Pandas, NumPy  
- **Machine Learning:** Scikit-learn  
- **Model Persistence:** Joblib  
- **Visualization & UI:** Streamlit  

---

## 📂 Project Structure

weekend-getaway-ranker/
│
├── app.py                          # Streamlit application
├── weekend_getaway_ranker_model.pkl # Trained ranking model
├── scaler.pkl                      # Feature scaler
├── city_coordinates.csv            # City latitude & longitude
├── Top Indian Places to Visit.csv  # Dataset
├── weekend_getaway_ranker.ipynb    # Notebook (EDA + Model)
├── requirements.txt                # Dependencies
└── README.md

```

## 🧪 Model Details

- **Type:** Weighted ranking model (not classification/regression)
- **Scoring Logic:**

  Final Score =(0.4 × Rating)* (0.3 × Popularity)− (0.3 × Distance)

- Features are normalized using **MinMaxScaler**
- Distance is calculated dynamically per user input

---

## ▶️ How to Run Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/weekend-getaway-ranker.git
cd weekend-getaway-ranker
````

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run Streamlit App

```bash
streamlit run app.py
```

---

## 🌍 Deployment

The application is deployed on **Streamlit Cloud** and can be accessed via a public URL.
All paths are relative, making the app cloud-compatible.

---

## 📊 Sample Output

* Ranked list of destinations
* Distance from source city (km)
* Google rating
* Popularity (review count)

Internal ML scores are hidden to improve user experience.

---

## 📈 Future Enhancements (Optional)

* Max distance filter
* Budget-based filtering
* Interactive map view
* MLflow experiment tracking
* City-level clustering

---

## 👤 Author

**Ashish Raj**
B.Tech CSE (Data Science)
---


