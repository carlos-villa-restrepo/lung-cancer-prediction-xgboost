import streamlit as st
import pandas as pd
from utils import set_design

st.set_page_config(page_title="Rendimiento de Modelos", layout="wide")
set_design("rendimiento") # <--- Aquí activamos el fondo

st.title("Dashboard de Rendimiento de Modelos")
st.write("---")
data = {
    "Horizonte (meses)": [12, 24, 36, 48, 60],
    "AUC": [0.82, 0.85, 0.87, 0.86, 0.88],
    "Precisión": [0.78, 0.80, 0.82, 0.81, 0.83],
    "Sensibilidad": [0.75, 0.77, 0.80, 0.79, 0.81]
}

df = pd.DataFrame(data)
st.dataframe(df, use_container_width=True) # Tu preferencia en formato DF

st.subheader("Comparación de rendimiento")
st.line_chart(df.set_index("Horizonte (meses)"))