> 🚫 **This is a private intellectual project. Unauthorized use, reproduction, or distribution is strictly prohibited.**

# AQUA-INTEL 💧

### AI-Powered Irrigation Recommendation System for Arid Regions (Saudi Arabia Focus)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://aqua-intel.streamlit.app)

👉 **Live Demo:** https://aqua-intel.streamlit.app  
👉 **GitHub Repo:** https://github.com/amir-dev-flux/aqua-intel

---

## 🌍 Project Overview

**AQUA-INTEL** is an end-to-end machine learning system that predicts **daily irrigation water requirements** for arid climates using open-access climate data.  
It transforms raw meteorological data into **actionable irrigation recommendations** through scientifically grounded feature engineering and machine learning.

This project is inspired by real-world sustainability challenges, especially aligned with:

- Saudi Vision 2030
- Water security in arid regions
- Sustainable agriculture
- AI for climate resilience

---

## 🚨 Problem Statement

Saudi Arabia and other arid regions face:

- Extreme water scarcity
- Inefficient irrigation practices
- Limited access to data-driven decision tools

Traditional irrigation often leads to overwatering and resource waste.  
**AQUA-INTEL addresses this by providing AI-powered, data-driven irrigation guidance using only open climate data.**

---

## 🧠 How It Works

Climate Inputs (Temperature, Humidity, Wind, Solar Radiation)
↓
Feature Engineering (ET₀ proxy + temporal lag features)
↓
Machine Learning Models (Linear Regression, RF, GB)
↓
Water Demand Prediction (Evapotranspiration)
↓
Crop-Specific Irrigation Recommendation
↓
Interactive Web App Output (mm/day)

---

## 📊 Data Source

- **NASA POWER Climate Dataset**
- Daily meteorological data for Riyadh, Saudi Arabia
- Variables used:
  - Temperature
  - Relative Humidity
  - Wind Speed
  - Solar Radiation

https://power.larc.nasa.gov/

---

## ⚙️ Methodology

- Constructed a scientifically inspired **Evapotranspiration (ET₀) proxy**
- Added **time-series lag features (1, 3, 7 days)**
- Evaluated multiple models:
  - Linear Regression
  - Random Forest
  - Gradient Boosting
- Used time-aware train/test split (80/20)
- Metrics: MAE, RMSE
- Added explainability (SHAP-style feature analysis)
- Deployed as a public web app using **Streamlit Cloud**

---

## 📈 Model Evaluation Results

| Model             | MAE    | RMSE   |
| ----------------- | ------ | ------ |
| Linear Regression | 0.0061 | 0.0078 |
| Gradient Boosting | 0.0281 | 0.0370 |
| Random Forest     | 0.0376 | 0.0525 |

📌 Linear Regression performed best, indicating strong linear structure in the engineered ET₀ signal — validating both the feature engineering and modeling pipeline.

---

## 🖥️ Live Demo

You can interact with the system here:  
👉 https://aqua-intel.streamlit.app

The web app allows users to:

- Adjust temperature, humidity, wind, solar radiation
- Select crop type (wheat, date palm, vegetables)
- Receive real-time irrigation recommendations

---

## 🧩 Project Structure

aqua-intel/
│
├── app.py # Streamlit web app
├── src/
│ ├── data.py # Data loading
│ ├── features.py # Feature engineering (ET₀ + lags)
│ ├── model.py # ML models and evaluation
│ └── predict.py # Irrigation recommendation logic
│
├── data/ # Climate dataset
├── notebooks/ # Exploratory work
├── test_pipeline.py # Experiments & evaluation
├── plot_results.py # Visualization
├── requirements.txt
└── README.md

---

## 🎯 Why This Project Matters

This is not a toy ML project.

AQUA-INTEL demonstrates:

- Real-world domain relevance (climate + agriculture + sustainability)
- End-to-end ML pipeline (data → features → models → evaluation → deployment)
- Research mindset (model comparison, metrics, interpretability)
- Engineering maturity (modular code, clean repo, deployed app)
- Alignment with global challenges (water security, climate resilience)

---

## 🚀 Future Work

Planned improvements include:

- Integration with real IoT sensor data
- Multi-city Saudi dataset expansion
- Crop-specific modeling
- Deep learning time-series models (LSTM/Transformer)
- Mobile-friendly UI
- Real-world pilot deployment

---

## 👤 Author

**Amir**  
Web developer transitioning into AI/ML  
Focused on impactful AI for sustainability and real-world systems

---

## ⚠️ Usage & Copyright Notice

© 2026 Amir. All rights reserved.

This project is **proprietary and confidential**.  
No part of this repository — including the source code, documentation, models, or design — may be used, copied, modified, distributed, or reused without **explicit written permission from the author**.

If you wish to request permission to use this project for academic, research, or commercial purposes, please contact the author directly.
