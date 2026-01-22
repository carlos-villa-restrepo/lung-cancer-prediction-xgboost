# Machine Learning Final Project: Lung Cancer Survival Prediction

This is the final project of our Machine Learning bootcamp, where we demonstrate the skills and knowledge acquired throughout our studies. We have developed an end-to-end solution to predict survival months in lung cancer patients, integrating clinical data with socioeconomic determinants.

> *"Hard work always beats talent when talent doesn't work hard"* - Tim Notke

## 👥 Credits

**Team Members:**
> - [Betania Medina](https://github.com/Betaniammc)
> - [Carlos Restrepo](https://github.com/carlos-villa-restrepo) 
> - [Elius Trujillo](https://github.com/elius123ef)

**Academy:** > - [4Geeks Academy](https://4geeksacademy.com/us/index) 
> - **Bootcamp:** Spain-DS-20 
> - **Mentor:** [Ing. Héctor Chocobar Torrejón](https://github.com/hchocobar/)
> - **Teacher Assitant:** [Beatriz Solana Ros](https://github.com/mezcolantriz)

## 🎯 Project Goal

The goal of this project is to develop a complete Machine Learning solution to:
- Process and clean complex oncological datasets (SEER).
- Perform a deep Exploratory Data Analysis (EDA) to find correlations between income and survival.
- Train and optimize a Gradient Boosting model (XGBoost) to predict survival time.
- Provide a tool for clinical and social insight through ML techniques.

## 🚀 Project Overview

### Problem Statement
Lung cancer prognosis is typically driven by clinical stages, but socioeconomic factors often play a hidden role in treatment access and outcomes. We aimed to build a model that quantifies how variables like **Income Level** and **Surgical History** impact a patient's life expectancy in months.

### Dataset
We utilized the **SEER (Surveillance, Epidemiology, and End Results)** dataset, focusing on Lung and Bronchus cancer cases (1975-2021).
- **Instances:** 60,000+ records.
- **Predictors:** 20+ variables including Stage, Age, Sex, Surgery History, and Median Household Income.

### Methodology
We implemented a regression pipeline comparing **Random Forest** and **XGBoost**. The process included Feature Engineering to consolidate cancer stages and cleaning categorical socioeconomic data to handle non-linear relationships.

### Results
The final **XGBoost** model achieved:
- **MAE (Mean Absolute Error):** 16.27 months.
- **R² Score:** 0.30.
- **Key Insight:** Surgical intervention and income level are top predictors, showing a survival gap of over 50 months between the most and least favorable scenarios.

## 📝 Project Phases

### Step 1: Problem Definition
The project addresses the need for personalized prognosis. We transformed raw clinical records into a supervised regression problem where the target is `Survival months`.

### Step 2: Acquiring and Loading
Data was sourced from the SEER database, processed into a structured format, and loaded using Pandas for initial cleaning.

### Step 3: Store the Information
The processed data was handled through a structured pipeline. We utilized SQL-based logic to filter relevant oncological events and ensure data integrity before the EDA phase.

### Step 4: Descriptive Analysis
We analyzed the distribution of survival times, finding a significant skew towards shorter durations in advanced stages. Statistical measures confirmed that 'Income Level' follows a multimodal distribution across different geographic regions in the dataset.

### Step 5: Full EDA
We performed a comprehensive EDA, identifying that:
- **Surgery** is a critical "pivot" variable.
- **Income** correlates with earlier detection (Localized stage).
- We split the data into **80% training** and **20% testing** sets.

### Step 6: Build the Model and Optimize It
We optimized an **XGBoost Regressor** using hyperparameter tuning. By refining `learning_rate` and `max_depth`, we improved the initial Random Forest baseline by reducing the MAE from 17.97 to 16.27 months.

### Step 7: Deploy the Model
*The model is prepared for deployment as a web service where users can input patient profiles to receive a survival estimation.*

## 📁 Project Structure

ml-project-repo/

├── 📁 data/

│ ├── 📁 interim/ # Intermediate transformed data 

│ ├── 📁 processed/ # Final data used for modeling

│ └── 📁 raw/ # Raw data without processing 

├── 📁 database/ # SQL scripts and database configs 

├── 📁 docs/

│ ├── 📁 Figures/ # Feature Importance and Scenario plots 

│ ├── Dic.md # Data dictionary 

│ └── Reporte final EDA.md # Final clinical findings report 

├── 📁 models/

│ └── survival_xgboost_final.pkl # Trained XGBoost model

├── 📁 notebooks/

│ ├── 01_eda_elius.ipynb # Phase 1: Exploratory Data Analysis

│ └── 02_ML_elius.ipynb # Phase 2: Machine Learning Modeling 

├── 📁 src/

│ └── predict_survival.py # Prediction engine script 

├── 📁 webapp/ # Deployment application (Streamlit/Flask)  


## 🛠️ Technologies Used
- **Python:** Primary language.
- **Pandas & Numpy:** Data manipulation.
- **XGBoost & Scikit-Learn:** Machine Learning modeling.
- **Matplotlib & Seaborn:** Data visualization.
- **Joblib:** Model serialization.

## 📊 Results Summary
The analysis of scenarios demonstrated the model's consistency:
- **Ideal Scenario:** ~67.64 months (Localized + Surgery + High Income).
- **Critical Scenario:** ~14.76 months (Distant + No Surgery + Low Income).

## 🌐 Live Demo
*[Link to be added upon deployment]*