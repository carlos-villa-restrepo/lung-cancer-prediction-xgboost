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
    # Intentamos varias rutas comunes para evitar errores de despliegue
    rutas_posibles = [
        "webapp/data/EDA_FINAL.csv", # Si ejecutas desde la raíz del repo
        "data/EDA_FINAL.csv",        # Si ejecutas desde dentro de /webapp
        "../data/EDA_FINAL.csv"      # Ruta relativa desde /pages
    ]
    
    for ruta in rutas_posibles:
        if os.path.exists(ruta):
            df = pd.read_csv(ruta)
            st.info(f"Cargando dataset predeterminado desde: {ruta}")
            break

    if df is None:
        st.warning("No se encontró el dataset en ninguna de las rutas predefinidas.")

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

