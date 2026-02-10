import plotly.express as px
import streamlit as st
import joblib
import pandas as pd
from utils import set_design

# 1. Configuración (Solo debe haber un set_page_config y debe ser lo primero)
st.set_page_config(page_title="Simulación de Estrategias", layout="wide")
set_design("scenarios")

# --- NUEVO: INICIALIZACIÓN DEL ESTADO DE SESIÓN ---
if 'df_res' not in st.session_state:
    st.session_state.df_res = None
    st.session_state.mejor_t = None

st.title("🔬 Simulación de Tratamientos")

# 2. Carga del Modelo
meses = st.selectbox("Horizonte temporal (Meses)", [12, 24, 36, 48, 60])
try:
    modelo = joblib.load(f"model/pipeline_{meses}m.pkl")
except:
    st.error("No se encuentra el modelo.")
    st.stop()

# 3. Datos del Paciente (Formulario)
col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("Datos Básicos")
    age_group = st.selectbox("Grupo edad", [1, 2, 3, 4, 5, 6])
    income = st.selectbox("Nivel ingreso", [1, 2, 3, 4])

with col2:
    st.subheader("Perfil Tumoral")
    tumor_category = st.selectbox("Categoría tumor", [1, 2, 3, 4])
    grade = st.selectbox("Grado clínico", [1, 2, 3, 4])
    tumors = st.number_input("Número tumores", 0, 10, value=1)

with col3:
    st.subheader("Ubicación y Tipo")
    primary_site = st.selectbox("Sitio primario (Ubicación)", [
        "C34.0-Main bronchus", "C34.1-Upper lobe, lung",
        "C34.2-Middle lobe, lung", "C34.3-Lower lobe, lung"
    ])
    st.image("assets/referencia_anatomica.png")
    stage = st.selectbox("Estadio (Stage)", [0, 1, 2, 3, 4])
    histology = st.selectbox("Histología",
                             ["Adenocarcinoma", "Squamous cell carcinoma", "Large cell carcinoma", "Other"])

# 4. Simulación
tratamientos = ["S + Q + SR", "S + Q + UN", "N + Q + SR", "N + nQ + UN", "R + Q + SR"]

if st.button("🔄 Ejecutar Simulación"):
    resultados_lista = []

    for t in tratamientos:
        row = {
            'age_group': age_group, 'tumor_category': tumor_category,
            'grade_clinical': grade, 'income_level': income,
            'Total number of in situ/malignant tumors for patient': tumors,
            'tratamiento': t, 'Primary Site': primary_site,
            'Stage_Final': stage, 'histology_type_named': histology
        }
        prob = modelo.predict_proba(pd.DataFrame([row]))[0][1]
        resultados_lista.append({
            "Estrategia": t,
            "Prob. Supervivencia": (1 - prob) * 100

        })

    # GUARDAR EN SESSION STATE
    st.session_state.df_res = pd.DataFrame(resultados_lista)
    st.session_state.mejor_t = st.session_state.df_res.loc[
        st.session_state.df_res['Prob. Supervivencia'].idxmax(), 'Estrategia']

# --- 5. MOSTRAR RESULTADOS (Fuera del botón, pero condicionado a que existan datos) ---
if st.session_state.df_res is not None:
    df_res = st.session_state.df_res

    st.write("---")
    st.subheader(f"📊 Comparativa de Supervivencia ({meses} meses)")

    # Gráfico Plotly
    fig = px.bar(df_res, x="Prob. Supervivencia", y="Estrategia", orientation='h',
                 title=f"Probabilidad de Supervivencia a {meses} meses",
                 text="Prob. Supervivencia", color="Prob. Supervivencia",
                 color_continuous_scale="Viridis")
    fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
    fig.update_layout(yaxis={'categoryorder': 'total ascending'}, xaxis_range=[0, 110], height=400)
    st.plotly_chart(fig, use_container_width=True)

    # Tabla de detalles (Tu preferencia [2026-01-28])
    st.write("### 📋 Tabla de Detalles")
    st.dataframe(
        df_res.style.format({"Prob. Supervivencia": "{:.2f}%"})
        .highlight_max(subset=["Prob. Supervivencia"], color="#d4edda"),
        use_container_width=True, hide_index=True
    )
    st.info(f"💡 Estrategia recomendada: **{st.session_state.mejor_t}**")

# --- 6. GLOSARIO UNIFICADO ---
st.write("---")
with st.expander("📖 Glosario Completo"):
    data_glosario = {
        "Categoría": [
            # Estrategias (Basadas en tus siglas)
            "Estrategia", "Estrategia", "Estrategia", "Estrategia", "Estrategia",
            # Histología (Completo)
            "Histología", "Histología", "Histología", "Histología",
            # Sitio Primario (Completo)
            "Sitio Primario", "Sitio Primario", "Sitio Primario", "Sitio Primario"
        ],
        "Término": [
            "S + Q + SR", "S + Q + UN", "N + Q + SR", "N + nQ + UN", "R + Q + SR",
            "Adenocarcinoma", "Squamous cell carcinoma", "Large cell carcinoma", "Other",
            "C34.0-Main bronchus", "C34.1-Upper lobe, lung", "C34.2-Middle lobe, lung", "C34.3-Lower lobe, lung"
        ],
        "Definición": [
            "Cirugía + Quimioterapia + Radiación Estándar.",
            "Cirugía + Quimioterapia + Radiación Desconocida.",
            "Sin Cirugía + Quimioterapia + Radiación Estándar.",
            "Sin Cirugía + Sin Quimioterapia + Radiación Desconocida.",
            "Radiación + Quimioterapia + Radiación Estándar.",
            "Cáncer que se origina en las células glandulares (más común en no fumadores).",
            "Cáncer que empieza en las células escamosas del pulmón (relacionado al tabaco).",
            "Cáncer de células grandes, puede aparecer en cualquier parte del pulmón.",
            "Otros tipos histológicos menos comunes o no especificados.",
            "Localizado en el bronquio principal (punto donde la tráquea se divide).",
            "Ubicación en el lóbulo superior (parte más alta del pulmón).",
            "Ubicación en el lóbulo medio (solo presente en el pulmón derecho).",
            "Ubicación en el lóbulo inferior (base de los pulmones)."
        ]
    }
    df_glosario = pd.DataFrame(data_glosario)

    busqueda = st.text_input("🔍 Buscar en el glosario...", key="search_glosario")

    if busqueda:
        # Filtro que busca en Categoría, Término o Definición
        mask = df_glosario.apply(lambda row: row.astype(str).str.contains(busqueda, case=False).any(), axis=1)
        df_mostrar = df_glosario[mask]
    else:
        df_mostrar = df_glosario

    st.dataframe(df_mostrar, use_container_width=True, hide_index=True)