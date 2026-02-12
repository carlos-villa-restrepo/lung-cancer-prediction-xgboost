import streamlit as st
import pandas as pd
from pathlib import Path
from utils import set_design

st.set_page_config(page_title="EDA", layout="wide")
set_design("eda")

st.title("Exploración de Datos (EDA)")

# SIDEBAR
st.sidebar.header("Configuración de Datos")
uploaded_file = st.sidebar.file_uploader("Sube tu archivo CSV", type=["csv"])

# RUTAS ROBUSTAS
BASE_DIR = Path(__file__).resolve().parents[1]   # /webapp
DATA_PATH = BASE_DIR / "data" / "EDA_FINAL.csv"

df = None

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.info("✅ Dataset cargado desde archivo subido")

elif DATA_PATH.exists():
    df = pd.read_csv(DATA_PATH)
    st.info(f"✅ Dataset cargado desde: {DATA_PATH}")

else:
    st.error("⚠️ No se encontró el archivo EDA_FINAL.csv.")

# 3. MÉTRICAS EN FORMATO DATAFRAME [2026-02-12]
if df is not None:
    st.subheader("📋 Vista General")
    st.dataframe(df.head(10), use_container_width=True)

    st.subheader("📊 Análisis Estadístico")
    # Presentamos el describe() transpuesto para cumplir con tu preferencia de DF
    st.dataframe(df.describe().T, use_container_width=True)

    # Selector de variables y tabla de frecuencias
    col_target = st.selectbox("Selecciona columna:", df.columns)
    conteo = df[col_target].value_counts().reset_index()
    conteo.columns = [col_target, 'Cantidad']
    
    c1, c2 = st.columns([2, 1])
    with c1:
        st.bar_chart(conteo.set_index(col_target))
    with c2:
        st.dataframe(conteo, use_container_width=True, hide_index=True)