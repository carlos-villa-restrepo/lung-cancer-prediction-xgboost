# 🏥 Lung Cancer Diagnosis & Life Expectancy: A Multi-Milestone ML Approach

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![XGBoost](https://img.shields.io/badge/Model-XGBoost-green.svg)](https://xgboost.readthedocs.io/)
[![Conventional Commits](https://img.shields.io/badge/Commits-Conventional-fb7063.svg)](https://www.conventionalcommits.org/)

> **Dynamic Survival Analysis system for lung cancer patients.** This project moves beyond static predictions to estimate survival probabilities across five-year milestones using a high-fidelity Gradient Boosting framework.

---

## 🎯 Executive Summary
Lung cancer prognosis traditionally overlooks socioeconomic barriers. This solution integrates **clinical oncology data** with **socioeconomic determinants** (Household Income) to quantify how treatment decisions and social status dynamically alter a patient's survival probability over a 60-month horizon.

---

## 🚀 Key Features & Methodology

### 🧠 Multi-Milestone Architecture
Unlike a single regression, I developed **5 independent XGBoost models**, each optimized for specific intervals (12, 24, 36, 48, and 60 months). 

* **Data Source:** SEER Dataset (500,000+ records, 2012-2022).
* **Feature Engineering:** Consolidated complex cancer stages and mapped treatment combinations with surgical intervention and income as primary predictors.
* **Monotonic Logic:** Implemented a post-processing layer to ensure survival curves maintain clinical coherence (consistently decreasing over time).

### 📈 Model Performance
* **Short-term (12 months):** 79% Accuracy.
* **Long-term (60 months):** **88% Accuracy**, providing high confidence for clinical planning.
* **Reliability:** Precision of 0.82 for early survivors, increasing as the timeline progresses.

---

## 📁 Project Structure & Navigation

The repository is organized following professional data engineering standards:

```text
.
├── 📁 assets/             # Visual resources and clinical context
├── 📁 data/               # Processed SEER datasets
├── 📁 models/             # Serialized XGBoost pipelines (.pkl)
├── 📁 notebooks/          # Core Development Flow:
│   ├── 01_eda_and_feature_engineering.ipynb
│   ├── 02_model_training_xgboost.ipynb
│   └── 03_evaluation_metrics.ipynb
├── 📁 webapp/             # Streamlit Deployment source code
├── 📄 Home.py             # App Entry point
└── 📄 requirements.txt    # Project dependencies

```
---

## 💻 Installation & Usage

To run this project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/carlos-villa-restrepo/lung-cancer-prediction-xgboost.git](https://github.com/carlos-villa-restrepo/lung-cancer-prediction-xgboost.git)
   cd lung-cancer-prediction-xgboost
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
3. **Run the Streamlit application:**
   ```bash
   streamlit run Home.py

---

## 📱 App Preview
![Lung Cancer Diagnosis Home](assets/home-page-streamlit.png)

*Vista principal de la plataforma de análisis de supervivencia.*

---

