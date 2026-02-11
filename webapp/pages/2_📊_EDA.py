import streamlit as st
import pandas as pd
import os
from utils import set_design

# CONFIGURACIÓN
st.set_page_config(page_title="Análisis de Datos - EDA", layout="wide")
set_design("eda")

st.title("Exploración de Datos (EDA)")

# --- LÓGICA DE CARGA DE DATOS CORREGIDA ---
df = None

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    # Ruta basada en tu diagnóstico: la carpeta 'data' está en la raíz
    # El archivo EDA_FINAL.csv debe estar dentro de esa carpeta 'data'
    rutas_a_probar = [
        "data/EDA_FINAL.csv",           # Opción 1: Carpeta data en la raíz
        "webapp/data/EDA_FINAL.csv",    # Opción 2: Carpeta data dentro de webapp
        "../data/EDA_FINAL.csv"         # Opción 3: Relativa desde pages
    ]
    
    for ruta in rutas_a_probar:
        if os.path.exists(ruta):
            df = pd.read_csv(ruta)
            st.info(f"✅ Dataset cargado desde: {ruta}")
            break

    if df is None:
        st.error("⚠️ No se encontró 'EDA_FINAL.csv'.")
        st.write("Archivos dentro de la carpeta 'data' detectada:")
        try:
            st.json(os.listdir("data")) # Esto nos dirá si el archivo está ahí
        except:
            st.write("No se pudo leer la carpeta 'data'")

# --- VISUALIZACIÓN EN DATAFRAMES [2026-01-28] ---
if df is not None:
    st.subheader("Vista general del Dataset")
    st.dataframe(df.head(10), use_container_width=True)

    st.subheader("Métricas Estadísticas")
    # Presentamos las métricas en formato DF como solicitaste
    st.dataframe(df.describe().T, use_container_width=True)

    st.subheader("Distribución de variables")
    col_target = st.selectbox("Selecciona columna para graficar:", df.columns)
    
    # Tabla de frecuencias en formato DF
    conteo = df[col_target].value_counts().reset_index()
    conteo.columns = [col_target, 'Cantidad']
    
    col_graf, col_tabla = st.columns([2, 1])
    with col_graf:
        st.bar_chart(conteo.set_index(col_target))
    with col_tabla:
        st.dataframe(conteo, use_container_width=True)