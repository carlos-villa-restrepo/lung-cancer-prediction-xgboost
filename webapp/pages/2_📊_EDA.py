import streamlit as st
import pandas as pd
from pathlib import Path
from utils import set_design

st.set_page_config(page_title="EDA", layout="wide")
set_design("eda")

st.title("Exploración de Datos (EDA)")

# 2. LÓGICA DE RUTAS (Auto-búsqueda en el proyecto)
df = None

# Sidebar para subir archivo manualmente
st.sidebar.header("Configuración de Datos")
uploaded_file = st.sidebar.file_uploader("Sube tu archivo CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

else:
    # Buscar el archivo automáticamente en todo el proyecto
    from pathlib import Path

    PROJECT_ROOT = Path(__file__).resolve().parents[2]

    archivo_encontrado = None
    for path in PROJECT_ROOT.rglob("EDA_FINAL.csv"):
        archivo_encontrado = path
        break

    if archivo_encontrado is not None:
        try:
            df = pd.read_csv(archivo_encontrado)
            st.info(f"✅ Dataset cargado desde: {archivo_encontrado}")
        except Exception:
            pass

    if df is None:
        st.error("⚠️ No se encontró el archivo EDA_FINAL.csv en el proyecto.")

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