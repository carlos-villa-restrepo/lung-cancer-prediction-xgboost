import streamlit as st
import pandas as pd
import joblib
from utils import set_design

set_design("prediction")

@st.cache_resource
def load_models():
    modelos = {}
    for m in [12,24,36,48,60]:
        modelos[m] = joblib.load(f"model/pipeline_{m}m.pkl")
    return modelos

modelos = load_models()

with st.container():
    st.title("Predicción de Supervivencia")
    st.write("---")
mes = st.selectbox("Horizonte temporal", [12,24,36,48,60])

age_group = st.selectbox("Grupo edad", [1,2,3,4])
tumor_category = st.selectbox("Categoría tumor", [1,2,3,4])
grade = st.selectbox("Grado clínico", [1,2,3,4])
income = st.selectbox("Nivel ingreso", [1,2,3,4])
tumors = st.number_input("Número tumores", 1,10)

tratamiento = st.selectbox("Tratamiento", [
    "S + Q + SR",
    "N + nQ + UN",
    "R + Q + SR"
])

site = st.selectbox("Primary Site", ["Upper lobe","Lower lobe"])
stage = st.selectbox("Stage", [1,2,3,4])

histology = st.selectbox(
    "Tipo histológico",
    [
        "Adenocarcinoma",
        "Squamous cell carcinoma",
        "Small cell carcinoma",
        "Large cell carcinoma"
    ]
)
if st.button("Calcular probabilidad"):
    X = pd.DataFrame([{
        "age_group": age_group,
        "tumor_category": tumor_category,
        "grade_clinical": grade,
        "income_level": income,
        "Total number of in situ/malignant tumors for patient": tumors,
        "tratamiento": tratamiento,
        "Primary Site": site,
        "Stage_Final": stage,
        "histology_type_named": histology
    }])

    prob = modelos[mes].predict_proba(X)[0][1]
    st.metric("Probabilidad de mortalidad", f"{prob:.2%}")

st.markdown('</div>', unsafe_allow_html=True)
