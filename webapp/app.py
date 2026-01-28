import streamlit as st
import pandas as pd
import os
import sys
import plotly.express as px
import time
from datetime import timedelta

# --- 1. CONFIGURACIÓN Y ESTILO ---
st.set_page_config(page_title="OncoPredict AI Pro", layout="wide", page_icon="🔬")


def apply_full_design():
    img_url = "https://img.freepik.com/free-vector/network-mesh-wire-digital-technology-background_1017-27428.jpg"
    st.markdown(f"""
        <style>
        [data-testid="stAppViewContainer"] {{
            background-image: url("{img_url}");
            background-size: cover; background-position: center; background-attachment: fixed;
        }}
        [data-testid="stAppViewContainer"]::before {{
            content: ""; position: absolute; top: 0; left: 0; width: 100%; height: 100%;
            background-color: rgba(10, 15, 25, 0.9); z-index: 0;
        }}
        [data-testid="stSidebar"] {{
            background-color: rgba(15, 20, 30, 0.8) !important;
            backdrop-filter: blur(10px); border-right: 1px solid rgba(255, 255, 255, 0.1);
        }}
        [data-testid="stMetric"], .stTabs, [data-testid="stForm"], .stExpander, .stTable, .stDataFrame {{
            background: rgba(255, 255, 255, 0.05) !important;
            backdrop-filter: blur(15px); border: 1px solid rgba(255, 255, 255, 0.1) !important;
            border-radius: 15px !important;
        }}
        h1, h2, h3 {{ color: #00d4ff !important; text-shadow: 0px 0px 10px rgba(0, 212, 255, 0.3); }}
        p, label, span {{ color: #e0e0e0 !important; }}
        </style>
    """, unsafe_allow_html=True)


apply_full_design()

# --- 2. INICIALIZACIÓN DE SESIÓN ---
if 'historico_pacientes' not in st.session_state:
    st.session_state['historico_pacientes'] = pd.DataFrame()
if 'ultimo_resultado' not in st.session_state:
    st.session_state['ultimo_resultado'] = pd.DataFrame()


# --- 3. FUNCIONES DE APOYO ---
def formatear_tiempo_humano(segundos):
    return f"{segundos:.2f}s" if segundos < 60 else f"{int(segundos // 60)}m {int(segundos % 60)}s"


# --- 4. SIDEBAR ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2103/2103633.png", width=70)
    st.title("Panel de Control")
    metodo = st.radio("Método de Entrada:", ["Manual Individual", "Carga Masiva (CSV)"])
    st.divider()
    num_manual = st.number_input("Filas a procesar (Dataset):", min_value=1, value=10)

    if st.button("♻️ Reiniciar Investigación"):
        st.session_state['historico_pacientes'] = pd.DataFrame()
        st.session_state['ultimo_resultado'] = pd.DataFrame()
        st.rerun()

# --- 5. CARGA DEL MOTOR ---
ruta_raiz = os.path.dirname(os.path.abspath(__file__))
if ruta_raiz not in sys.path: sys.path.append(ruta_raiz)
from src.procesar_pacientes import procesar_lista_pacientes

# --- 6. GESTIÓN DE ENTRADA ---
st.title("🔬 OncoPredict AI: Soporte de Decisión")
pacientes_data = []

if metodo == "Manual Individual":
    with st.form("form_paciente"):
        col1, col2 = st.columns(2)
        with col1:
            age = st.number_input("Edad", 18, 100, 60)
            stage = st.select_slider("Etapa (Stage)", options=[1, 2, 3, 4], value=3)
        with col2:
            grade = st.selectbox("Grado Histológico", [1, 2, 3, 4])
            tumor = st.number_input("Tamaño Tumor (mm)", 1, 150, 45)

        if st.form_submit_button("⚡ Analizar Paciente"):
            pacientes_data = [
                {'Age_Numeric': age, 'Stage_Rank': stage, 'Grade_Numeric': grade, 'Tumor_Size_Clean': tumor}]
            st.session_state['ejecutar'] = True

else:
    file = st.file_uploader("Subir dataset oncológico (.csv)", type=["csv"])
    if file:
        df_subido = pd.read_csv(file)
        st.info(f"📂 Archivo con {len(df_subido)} registros detectado.")
        num_final = min(num_manual, len(df_subido))

        if st.button(f"🚀 Procesar {num_final} registros"):
            pacientes_data = df_subido.head(num_final).to_dict(orient='records')
            st.session_state['ejecutar'] = True

# --- 7. PROCESAMIENTO ---
if pacientes_data and st.session_state.get('ejecutar', False):
    t_inicio = time.time()
    with st.spinner("🧠 Computando modelos de supervivencia y tratamiento..."):
        df_res = procesar_lista_pacientes(pacientes_data)
        st.session_state['ultimo_resultado'] = df_res
        st.session_state['historico_pacientes'] = pd.concat([st.session_state['historico_pacientes'], df_res],
                                                            ignore_index=True).drop_duplicates()
        st.session_state['tiempo_ultimo'] = time.time() - t_inicio
    st.session_state['ejecutar'] = False

# --- 8. VISUALIZACIÓN DE RESULTADOS ACTUALES ---
if not st.session_state['ultimo_resultado'].empty:
    df_act = st.session_state['ultimo_resultado']
    st.divider()
    st.subheader("📋 Resultados del Análisis Actual")

    # Métricas en formato DF (DF Format solicitado)
    res_df = pd.DataFrame({
        "Indicador": ["Tiempo de Proceso", "Supervivencia Media", "Beneficio por Tratamiento", "N° Casos"],
        "Valor": [formatear_tiempo_humano(st.session_state['tiempo_ultimo']),
                  f"{df_act['expectativa_total_meses'].mean():.1f} meses",
                  f"+{df_act['ganancia_meses'].mean():.1f} meses",
                  len(df_act)]
    })
    st.table(res_df)

    # SESIÓN DE LISTA DE VARIABLES (RECUPERADA)
    with st.expander("🔍 Ver Lista Detallada de Pacientes y Variables", expanded=True):
        # Límite de 1000 filas para el coloreado por rendimiento
        if len(df_act) <= 1000:
            st.dataframe(
                df_act.style.background_gradient(subset=['expectativa_total_meses'], cmap='Blues')
                .background_gradient(subset=['ganancia_meses'], cmap='RdYlGn'),
                use_container_width=True
            )
        else:
            st.warning("⚠️ Dataset muy grande. Se muestra sin colores para mayor fluidez.")
            st.dataframe(df_act, use_container_width=True)

# --- 9. MÉTRICAS GLOBALES DE INVESTIGACIÓN ---
st.divider()
st.header("🌎 Panel de Investigación Acumulada")

if not st.session_state['historico_pacientes'].empty:
    hist = st.session_state['historico_pacientes']

    # Tabla Global
    metrics_inv = pd.DataFrame({
        "Estadística de Investigación": ["Pacientes Totales", "Media Supervivencia", "Impacto Quimio (Máx)",
                                         "Tasa Recomendación"],
        "Valor Acumulado": [len(hist), f"{hist['expectativa_total_meses'].mean():.1f} m",
                            f"{hist['ganancia_meses'].max():.1f} m",
                            f"{(len(hist[hist['recomendacion'] == 'SUGERIR_QUIMIO']) / len(hist)) * 100:.1f}%"]
    })
    st.table(metrics_inv)

    # --- 8. MÉTRICAS DE INVESTIGACIÓN ACUMULADA ---
    if not st.session_state['historico_pacientes'].empty:
        st.divider()
        st.header("📊 Panel de Investigación Acumulada")
        hist = st.session_state['historico_pacientes']

        c1, c2 = st.columns([1, 2])
        with c1:
            st.table(pd.DataFrame({
                "Investigación": ["Pacientes Totales", "Tasa Recomendación"],
                "Valor": [len(hist), f"{(len(hist[hist['ganancia_meses'] > 10]) / len(hist)) * 100:.1f}%"]
            }))
            fig_pie = px.pie(hist, names='recomendacion', hole=0.4, title="Mix de Tratamiento",
                             color_discrete_sequence=['#00fbff', '#ff4b4b'])
            st.plotly_chart(fig_pie, use_container_width=True)
            # DESCRIPCIÓN DINÁMICA
            tasa_quimio = (len(hist[hist['recomendacion'] == 'SUGERIR_QUIMIO']) / len(hist)) * 100
            st.markdown(f"""
                    <div class="interpretacion-caja">
                    <strong>💡 Interpretación del Mix:</strong><br>
                    Este gráfico muestra la proporción de pacientes que se beneficiarían significativamente de quimioterapia. 
                    En la muestra actual, el <b>{tasa_quimio:.1f}%</b> de los pacientes presentan un perfil de alto beneficio terapéutico 
                    basado en el modelo de riesgos de Cox.
                    </div>
                    """, unsafe_allow_html=True)

        with c2:
            # Mejora visual del Box Plot (Jittering para evitar amontonamiento a la izquierda)
            fig_box = px.box(hist, y="expectativa_total_meses", points="all", notched=True,
                             title="Dispersión de Supervivencia Global")
            fig_box.update_traces(jitter=0.7, pointpos=-1.5, marker=dict(color='#00d4ff', opacity=0.5))
            st.plotly_chart(fig_box, use_container_width=True)
            # DESCRIPCIÓN DINÁMICA
            mediana = hist['expectativa_total_meses'].median()
            st.markdown(f"""
                    <div class="interpretacion-caja">
                    <strong>🔍 Análisis de Dispersión:</strong><br>
                    La caja central contiene el 50% de tus pacientes. La línea media indica una supervivencia mediana de <b>{mediana:.1f} meses</b>. 
                    Los puntos desplazados a la izquierda permiten observar casos atípicos (outliers) y la densidad de la muestra sin ocultar 
                    la tendencia estadística principal.
                    </div>
                    """, unsafe_allow_html=True)

    st.download_button("📥 Descargar Base de Investigación (CSV)", hist.to_csv(index=False), "investigacion_onco.csv")
else:
    st.info("La base de datos de investigación está vacía. Inicia un análisis para ver los acumulados.")