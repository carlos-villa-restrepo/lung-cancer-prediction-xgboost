import streamlit as st
import pandas as pd
import plotly.express as px
from utils import set_design

# Configuración inicial
set_design("metodologia")

# Título principal con un estilo más limpio
st.title("🔬 Metodología de Investigación y Modelado")
st.write("---")

# 1. MÉTRICAS CLAVE (Resumen ejecutivo)
# Esto reemplaza el texto plano del "Objetivo" por impacto visual
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="🎯 Objetivo", value="Supervivencia", delta="Pulmonar")
with col2:
    st.metric(label="📊 Dataset", value="SEER Program", delta="USA Data")
with col3:
    st.metric(label="🤖 Algoritmo", value="XGBoost", delta="Gradient Boosting")

# 2. EL PROCESO EN PASOS INTERACTIVOS (Uso de Tabs)
tab1, tab2, tab3 = st.tabs(["🛠 Preparación de Datos", "🧠 Modelado y Entrenamiento", "📈 Validación"])

with tab1:
    st.subheader("Fase 1: Curación y ETL")
    col_left, col_right = st.columns(2)
    with col_left:
        st.markdown("""
        **Proceso de limpieza:**
        - Eliminación de outliers en la variable edad.
        - Manejo de valores nulos en estadios clínicos.
        - **Feature Engineering:** Agrupación de tipos histológicos.
        """)
    with col_right:
        # Mini gráfico de ejemplo del EDA
        df_eda = pd.DataFrame({"Fase": ["Crudos", "Limpios", "Finales"], "Registros": [200, 180, 155]})
        fig_eda = px.bar(df_eda, x="Fase", y="Registros", title="Refinamiento de Datos (K)", height=200)
        st.plotly_chart(fig_eda, use_container_width=True)

with tab2:
    st.subheader("Fase 2: Arquitectura del Modelo")
    st.write("Se desarrollaron modelos específicos para 12, 24, 36, 48 y 60 meses.")

    # Diagrama de flujo simplificado con Markdown
    st.info("🔄 **Pipeline de Entrenamiento:** Datos ➡️ One-Hot Encoding ➡️ XGBoost ➡️ Optimización Bayesiana")

with tab3:
    st.subheader("Fase 3: Importancia de las Variables")
    st.write("¿Qué factores determinan la predicción? (Feature Importance)")

    # Gráfico de importancia de variables (Dataframe format como pediste [2026-01-28])
    imp_data = pd.DataFrame({
        "Variable": ["Estadio (Stage)", "Tratamiento", "Histología", "Edad"],
        "Peso": [0.45, 0.30, 0.15, 0.10]
    }).sort_values(by="Peso", ascending=True)

    fig_imp = px.bar(imp_data, x="Peso", y="Variable", orientation='h', color="Peso", color_continuous_scale="Blues")
    fig_imp.update_layout(height=250, margin=dict(l=0, r=0, t=30, b=0))
    st.plotly_chart(fig_imp, use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

# 3. SECCIÓN DE VARIABLES (Uso de Expander para no saturar)
with st.expander("📋 Detalle de Variables Utilizadas"):
    st.write("A continuación se detallan las columnas del dataset final utilizado para el entrenamiento:")
    vars_df = pd.DataFrame({
        "Variable": ["Age Group", "Stage Final", "Primary Site", "Histology", "Treatment"],
        "Tipo": ["Numérica", "Ordinal", "Categórica", "Categórica", "Categórica"],
        "Descripción": ["Rango de edad decenal", "Estadio AJCC (0-IV)", "Ubicación anatómica", "Tipo de célula",
                        "Protocolo aplicado"]
    })
    st.table(vars_df)  # Usamos st.table para una vista estática limpia