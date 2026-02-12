from pathlib import Path
import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parents[2]

st.subheader("DEBUG SISTEMA DE ARCHIVOS")

st.write("📂 PROJECT_ROOT:", PROJECT_ROOT)
st.write("📂 Existe root:", PROJECT_ROOT.exists())

st.write("📁 Carpetas en root:")
for p in PROJECT_ROOT.iterdir():
    st.write(" -", p)

st.write("🔍 Buscando EDA_FINAL.csv...")
encontrados = list(PROJECT_ROOT.rglob("EDA_FINAL.csv"))

if encontrados:
    st.success("Encontrados:")
    for f in encontrados:
        st.write(f)
else:
    st.error("NO existe en el deploy")
