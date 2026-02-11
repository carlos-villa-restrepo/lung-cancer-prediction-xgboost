import streamlit as st
import pandas as pd
import os
from utils import set_design

# CONFIGURACIÓN
st.set_page_config(page_title="Análisis de Datos - EDA", layout="wide")
set_design("eda")

st.title("Exploración de Datos (EDA)")

# --- LÓGICA DE CARGA DE DATOS ---
df = None

# 1. Intentar carga por el uploader
st.sidebar.header("Configuración de Datos")
uploaded_file = st.sidebar.file_uploader("Sube tu archivo CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("Archivo subido con éxito.")
else:
    # 2. Búsqueda automática del archivo en el servidor
    # Obtenemos la ruta de la carpeta donde está este archivo (webapp/pages/)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Subimos un nivel para llegar a 'webapp' y luego a 'data'
    ruta_auto = os.path.join(current_dir, "..", "data", "EDA_FINAL.csv")
    
    # Lista de rutas posibles para máxima compatibilidad
    rutas_posibles = [
        ruta_auto,
        "webapp/data/EDA_FINAL.csv",
        "data/EDA_FINAL.csv",
        "/mount/src/sp-ml-20-final-project-g1/webapp/data/EDA_FINAL.csv"
    ]
    
    for ruta in rutas_posibles:
        if os.path.exists(ruta):
            df = pd.read_csv(ruta)
            st.info(f"Dataset cargado automáticamente.")
            break

    if df is None:
        st.error("⚠️ No se encontró el dataset 'EDA_FINAL.csv' en el servidor.")
        # Bloque de ayuda para depuración (solo se ve si falla)
        with st.expander("Ver diagnóstico de rutas (Depuración)"):
            st.write(f"Directorio actual: {current_dir}")
            st.write("Archivos en la raíz detectados:", os.listdir("."))

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