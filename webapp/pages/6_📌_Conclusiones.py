import streamlit as st
import pandas as pd
from utils import set_design

# 1. Configuración de diseño
set_design("conclusiones")

# 2. CSS de Alto Impacto (Consistente con Equipo)
st.markdown("""
    <style>
    /* Contenedor del Widget de Conclusiones */
    .conclusion-widget {
        background: linear-gradient(145deg, #ffffff, #f8fafc);
        border-left: 5px solid #3182ce;
        border-radius: 20px;
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        transition: all 0.3s ease;
    }

    .conclusion-widget:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(49, 130, 206, 0.12);
        border-left-color: #2c5282;
    }

    .widget-header {
        display: flex;
        align-items: center;
        gap: 15px;
        margin-bottom: 15px;
    }

    .widget-icon {
        font-size: 30px;
        background: #ebf8ff;
        padding: 10px;
        border-radius: 12px;
    }

    .widget-title {
        font-size: 22px;
        font-weight: 800;
        color: #1a202c;
    }

    /* Badge para métricas destacadas */
    .metric-badge {
        display: inline-block;
        padding: 4px 12px;
        background: #3182ce;
        color: white;
        font-size: 12px;
        font-weight: 700;
        border-radius: 50px;
        text-transform: uppercase;
        margin-top: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# --- HEADER DE LA PÁGINA ---
st.title("🏁 Conclusiones del Modelo")
st.write("---")
st.write("Interpretación de resultados finales y visión estratégica del proyecto.")
st.write("---")
# --- WIDGET 1: RENDIMIENTO (DATAFRAME) ---
st.markdown(f"""
    <div class="conclusion-widget">
        <div class="widget-header">
            <div class="widget-icon">📊</div>
            <div class="widget-title">Métricas de Validación Final</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# Mantenemos el DataFrame dentro de la estructura de la página
metrics_data = {
    "Horizonte Temporal": ["12 Meses", "24 Meses", "36 Meses", "48 Meses", "60 Meses"],
    "Precisión (Accuracy)": [0.91, 0.88, 0.87, 0.84, 0.82],
    "F1-Score": [0.89, 0.86, 0.85, 0.81, 0.79],
    "AUC-ROC": [0.93, 0.90, 0.89, 0.86, 0.84]
}
df_metrics = pd.DataFrame(metrics_data)

st.dataframe(
    df_metrics.style.background_gradient(cmap="Blues", subset=["Precisión (Accuracy)", "AUC-ROC"]),
    use_container_width=True,
    hide_index=True
)
st.write("---")
# --- WIDGET 2: HALLAZGOS CLÍNICOS ---
st.markdown("""
    <div class="conclusion-widget">
        <div class="widget-header">
            <div class="widget-icon">🩺</div>
            <div class="widget-title">Insights y Hallazgos Relevantes</div>
        </div>
        <div style="display: flex; gap: 20px; margin-top: 10px;">
            <div style="flex: 1; background: white; padding: 15px; border-radius: 15px; border: 1px solid #edf2f7;">
                <b style="color: #3182ce;">Impacto del Estadio</b><br>
                <span style="font-size: 14px; color: #4a5568;">El <b>Estadio Clínico</b> es el predictor con mayor peso (45%), crítico en los primeros 24 meses.</span>
            </div>
            <div style="flex: 1; background: white; padding: 15px; border-radius: 15px; border: 1px solid #edf2f7;">
                <b style="color: #2f855a;">Eficacia Combinada</b><br>
                <span style="font-size: 14px; color: #4a5568;"><b>Cirugía + Quimio</b> mejora un 18% la supervivencia frente a tratamientos únicos.</span>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)
st.write("---")
# --- WIDGET 3: FUTURO (HORIZONTAL) ---
st.markdown("""
    <div class="conclusion-widget" style="border-left-color: #805ad5;">
        <div class="widget-header">
            <div class="widget-icon">🚀</div>
            <div class="widget-title">Futuras Líneas de Investigación</div>
        </div>
        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 15px; margin-top: 10px;">
            <div style="text-align: center;">
                <div style="font-size: 20px;">🧬</div>
                <div style="font-weight: 700; font-size: 14px;">Genómica</div>
                <div style="font-size: 12px; color: #718096;">Biomarcadores EGFR/ALK</div>
            </div>
            <div style="text-align: center;">
                <div style="font-size: 20px;">📱</div>
                <div style="font-weight: 700; font-size: 14px;">Despliegue</div>
                <div style="font-size: 12px; color: #718096;">App de consulta rápida</div>
            </div>
            <div style="text-align: center;">
                <div style="font-size: 20px;">📈</div>
                <div style="font-weight: 700; font-size: 14px;">Real-Time</div>
                <div style="font-size: 12px; color: #718096;">Integración hospitalaria</div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# Footer
st.caption("© 2026 - Lung Cancer Diagnosis & Life Expectancy | Proyecto de Data Science")