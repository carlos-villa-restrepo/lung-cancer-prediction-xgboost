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

# Inicializamos df como None para evitar NameError
df = None

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("Archivo subido con éxito.")
else:
    # LÓGICA DE RUTAS ROBUSTA
    # 1. Intentamos ruta relativa simple (la más común en Streamlit Cloud)
    # 2. Intentamos ruta absoluta desde el archivo actual
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    rutas_a_probar = [
        "webapp/data/EDA_FINAL.csv",         # Ruta desde la raíz del repo
        "data/EDA_FINAL.csv",                # Ruta si ya está en webapp
        os.path.join(BASE_DIR, "data", "EDA_FINAL.csv") # Ruta absoluta calculada
    ]
    
    for ruta in rutas_a_probar:
        if os.path.exists(ruta):
            df = pd.read_csv(ruta)
            st.info(f"Dataset cargado desde: {ruta}")
            break

    if df is None:
        st.error("⚠️ No se encontró el dataset en el servidor. Por favor, sube el archivo manualmente en el panel lateral.")

# Mostrar información en DataFrames [2026-01-28]
if df is not None:
    st.subheader("Vista general del Dataset")
    # Usamos st.dataframe para cumplir con tu preferencia de métricas
    st.dataframe(df.head(10), use_container_width=True)

    st.subheader("Análisis Estadístico")
    # Transponemos para que las métricas se vean mejor en formato tabla
    st.dataframe(df.describe().T, use_container_width=True)

    st.subheader("Distribución de variables")
    col_target = st.selectbox("Selecciona columna para graficar:", df.columns)

    # Preparar DF de conteo para visualización
    conteo = df[col_target].value_counts().reset_index()
    conteo.columns = [col_target, 'Cantidad']

    # Gráfico y Tabla lado a lado
    c1, c2 = st.columns([2, 1])
    with c1:
        st.bar_chart(conteo.set_index(col_target))
    with c2:
        st.dataframe(conteo, use_container_width=True)