import streamlit as st
import pandas as pd
import os
from utils import set_design

# CONFIGURACIÓN ÚNICA
st.set_page_config(page_title="Análisis de Datos - EDA", layout="wide")
set_design("eda")

st.title("Exploración de Datos (EDA)")

# Carga de datos
st.sidebar.header("Configuración de Datos")
uploaded_file = st.sidebar.file_uploader("Sube tu archivo CSV", type=["csv"])

df = None
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("Archivo subido con éxito.")
else:
    ruta_default = "../webapp/data/EDA_FINAL.csv"
    if os.path.exists(ruta_default):
        df = pd.read_csv(ruta_default)
        st.info("Cargando dataset predeterminado.")
    else:
        st.warning("No se encontró el dataset.")

# Mostrar información en DataFrames [2026-01-28]
if df is not None:
    st.subheader("Vista general del Dataset")
    st.dataframe(df.head(10), use_container_width=True)

    st.subheader("Análisis Estadístico")
    st.dataframe(df.describe().T, use_container_width=True)

    st.subheader("Distribución de variables")
    col_target = st.selectbox("Selecciona columna para graficar:", df.columns)

    conteo = df[col_target].value_counts().reset_index()
    conteo.columns = [col_target, 'Cantidad']

    st.bar_chart(conteo.set_index(col_target))
    st.dataframe(conteo, use_container_width=True)

