import streamlit as st
import pandas as pd
import os
from utils import set_design

st.set_page_config(page_title="EDA", layout="wide")
set_design("eda")

# --- FUNCIÓN DE BÚSQUEDA AGRESIVA ---
def buscar_archivo(nombre_archivo):
    # 1. Intentar rutas directas conocidas
    rutas_directas = [
        os.path.join("data", "processed", nombre_archivo),
        os.path.join("webapp", "data", nombre_archivo),
        nombre_archivo
    ]
    
    for r in rutas_directas:
        if os.path.exists(r):
            return r
            
    # 2. Búsqueda recursiva en todo el proyecto
    for raiz, dirs, archivos in os.walk("."):
        if nombre_archivo in archivos:
            return os.path.join(raiz, nombre_archivo)
    return None

st.title("Exploración de Datos (EDA)")

# Ejecutamos la búsqueda
archivo_encontrado = buscar_archivo("EDA_FINAL.csv")

if archivo_encontrado:
    df = pd.read_csv(archivo_encontrado)
    st.success(f"✅ Archivo encontrado en: {archivo_encontrado}")
    
    # --- MÉTRICAS EN FORMATO DATAFRAME [2026-02-12] ---
    st.subheader("📋 Métricas Descriptivas")
    st.dataframe(df.describe().T, use_container_width=True)
    
    st.subheader("👀 Vista Previa")
    st.dataframe(df.head(10), use_container_width=True)
else:
    st.error("❌ El servidor no encuentra 'EDA_FINAL.csv' por ninguna parte.")
    
    # ESTO NOS DARÁ LA RESPUESTA DEFINITIVA
    with st.expander("🔍 Mapa de archivos del servidor (Haz click aquí)"):
        for raiz, dirs, archivos in os.walk("."):
            # Ignoramos carpetas ocultas de sistema
            if ".git" in raiz or ".venv" in raiz: continue
            st.code(f"📁 {raiz}")
            for f in archivos:
                st.write(f"--- 📄 {f}")