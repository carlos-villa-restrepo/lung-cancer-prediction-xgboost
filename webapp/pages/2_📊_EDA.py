import streamlit as st
import pandas as pd
import os
from utils import set_design

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Análisis de Datos - EDA", layout="wide")
set_design("eda")

st.title("Exploración de Datos (EDA)")

# 2. INICIALIZACIÓN DE VARIABLES (Evita NameError)
df = None

# 3. COMPONENTE DE CARGA EN SIDEBAR
st.sidebar.header("Configuración de Datos")
uploaded_file = st.sidebar.file_uploader("Sube tu archivo CSV", type=["csv"])

# 4. LÓGICA DE CARGA (Primero el archivo subido, luego el default)
if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("✅ Archivo subido con éxito.")
    except Exception as e:
        st.error(f"Error al leer el archivo subido: {e}")
else:
    # Rutas basadas en tu estructura de archivos detectada
    rutas_a_probar = [
        "data/EDA_FINAL.csv",           # Carpeta data en la raíz
        "webapp/data/EDA_FINAL.csv",    # Carpeta data dentro de webapp
        "../data/EDA_FINAL.csv"         # Relativa desde pages
    ]
    
    for ruta in rutas_a_probar:
        if os.path.exists(ruta):
            try:
                df = pd.read_csv(ruta)
                st.info(f"📊 Cargando dataset predeterminado.")
                break
            except Exception as e:
                continue

    if df is None:
        st.warning("⚠️ No se encontró el dataset 'EDA_FINAL.csv'. Por favor, cárgalo manualmente.")

# 5. VISUALIZACIÓN DE MÉTRICAS EN DATAFRAME [2026-02-12]
# Solo ejecutamos si el DataFrame se cargó correctamente
if df is not None:
    st.subheader("📋 Vista General del Dataset")
    # Mostramos los datos en formato interactivo
    st.dataframe(df.head(10), use_container_width=True)

    st.subheader("📈 Análisis Estadístico (Métricas)")
    # Transponemos para que las métricas (mean, std, etc.) sean filas, cumpliendo tu preferencia de DF
    st.dataframe(df.describe().T, use_container_width=True)

    st.subheader("🔍 Distribución por Variable")
    col_target = st.selectbox("Selecciona columna para analizar:", df.columns)
    
    # Tabla de frecuencias en formato DF
    conteo = df[col_target].value_counts().reset_index()
    conteo.columns = [col_target, 'Cantidad']
    
    col_graf, col_tabla = st.columns([2, 1])
    with col_graf:
        st.bar_chart(conteo.set_index(col_target))
    with col_tabla:
        # Tabla de conteo específica en formato DF
        st.dataframe(conteo, use_container_width=True, hide_index=True)