import streamlit as st
import pandas as pd
import joblib
import os
import plotly.graph_objects as go
from utils import set_design

# 1. Configuración y Estética
st.set_page_config(page_title="Predicción Individual", layout="wide")
set_design("prediction")


# --- FUNCIONES DE CARGA ---
@st.cache_data
def cargar_referencia():
    try:
        return pd.read_csv("data/referencia_pacientes.csv")
    except:
        return pd.DataFrame()


@st.cache_resource
def cargar_todos_los_modelos():
    cortes = [12, 24, 36, 48, 60]
    modelos = {}
    for m in cortes:
        path = f"model/pipeline_{m}m.pkl"
        if os.path.exists(path):
            modelos[m] = joblib.load(path)
    return modelos


df_ref = cargar_referencia()
dict_modelos = cargar_todos_los_modelos()

# 2. SIDEBAR: Buscador por ID
st.sidebar.header("🔍 Cargar Datos Reales")
id_input = st.sidebar.text_input("Patient ID:", placeholder="Ej: 450")

paciente_data = None
if id_input and not df_ref.empty:
    res = df_ref[df_ref['Patient ID'].astype(str) == id_input]
    if not res.empty:
        paciente_data = res.iloc[0]
        st.sidebar.success(f"✅ Datos de ID {id_input} cargados")
    else:
        st.sidebar.warning("❌ ID no encontrado")

st.title("🔮 Predicción de Supervivencia Individual")

# 3. FORMULARIO DE ENTRADA
with st.expander("📝 Editar Variables del Paciente", expanded=True):
    col1, col2, col3 = st.columns(3)

    with col1:
        sex_opts = ["Male", "Female"]
        idx_sex = sex_opts.index(paciente_data['Sex']) if paciente_data is not None else 0
        sex = st.selectbox("Sexo", sex_opts, index=idx_sex)

        age_opts = [1, 2, 3, 4, 5, 6]
        idx_age = age_opts.index(int(paciente_data['age_group'])) if paciente_data is not None else 0
        age = st.selectbox("Grupo de Edad", age_opts, index=idx_age)

    with col2:
        stage_opts = [1, 2, 3, 4]
        idx_stage = stage_opts.index(int(paciente_data['Stage_Final'])) if paciente_data is not None else 0
        stage = st.selectbox("Estadio Final", stage_opts, index=idx_stage)

        treat_opts = ["C + Q + Rs", "C + nQ + Rnor", "Cn + Q + Rnor", "Cn + nQ + Rs", "Cn + nQ + Rnor"]
        idx_treat = treat_opts.index(paciente_data['tratamiento']) if paciente_data is not None else 0
        tratamiento = st.selectbox("Protocolo de Tratamiento", treat_opts, index=idx_treat)

    with col3:
        tumor_val = int(paciente_data['tumor_category']) if paciente_data is not None else 30
        tumor = st.slider("Tamaño del Tumor (mm)", 0, 100, tumor_val)

        ntum_val = int(
            paciente_data['Total number of in situ/malignant tumors for patient']) if paciente_data is not None else 1
        n_tumores = st.number_input("Cantidad de tumores", 1, 15, value=ntum_val)

# 4. PROCESAMIENTO DE PREDICCIÓN
if st.button("📊 Generar Análisis de Supervivencia", use_container_width=True):
    if not dict_modelos:
        st.error("No se encontraron modelos en la carpeta /model")
    else:
        # Preparamos los datos (incluyendo las fijas del ID o defaults)
        input_row = {
            'Sex': sex,
            'age_group': age,
            'tumor_category': tumor,
            'Stage_Final': stage,
            'tratamiento': tratamiento,
            'Total number of in situ/malignant tumors for patient': n_tumores,
            'income_level': int(paciente_data['income_level']) if paciente_data is not None else 3,
            'grade_clinical': str(paciente_data['grade_clinical']) if paciente_data is not None else "9",
            'histology_type_named': paciente_data[
                'histology_type_named'] if paciente_data is not None else "Adenocarcinoma"
        }
        input_df = pd.DataFrame([input_row])

        # Calculamos probabilidades para cada mes
        tiempos = []
        probabilidades = []

        for m, model in dict_modelos.items():
            prob = model.predict_proba(input_df)[0][1]
            tiempos.append(m)
            probabilidades.append(float(prob) * 100)  # Fix float32

        # Crear DataFrame de resultados (Tu preferencia [2026-01-28])
        df_resultados = pd.DataFrame({
            "Meses": [f"{t} Meses" for t in tiempos],
            "Probabilidad": probabilidades
        })

        # --- VISUALIZACIÓN ---
        st.write("---")
        c1, c2 = st.columns([2, 1])

        with c1:
            st.subheader("📈 Curva de Supervivencia Estimada")
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=tiempos, y=probabilidades,
                mode='lines+markers',
                line=dict(color='#2D5A27', width=3),
                marker=dict(size=10),
                fill='tozeroy'  # Área bajo la curva
            ))
            fig.update_layout(
                xaxis_title="Meses tras el diagnóstico",
                yaxis_title="Probabilidad de estar Vivo (%)",
                yaxis=dict(range=[0, 105]),
                template="plotly_white"
            )
            st.plotly_chart(fig, use_container_width=True)

        with c2:
            st.subheader("📋 Métricas")
            # Tabla en formato DF con estilo
            st.dataframe(
                df_resultados.style.format({"Probabilidad": "{:.2f}%"})
                .background_gradient(cmap="Greens", subset=["Probabilidad"]),
                use_container_width=True,
                hide_index=True
            )

            # Métrica destacada a 60 meses
            p_final = probabilidades[-1]
            st.metric("Supervivencia a 5 años", f"{p_final:.1f}%")

        # Barra de progreso final (Fix float32)
        st.write("**Estado del pronóstico a largo plazo:**")
        st.progress(float(p_final / 100))
