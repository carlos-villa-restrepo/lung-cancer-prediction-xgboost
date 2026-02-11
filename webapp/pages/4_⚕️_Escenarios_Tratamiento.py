import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import joblib
import pandas as pd
import os
from utils import set_design

# 1. Configuración de página y diseño
st.set_page_config(page_title="Simulación de Estrategias", layout="wide")
set_design("scenarios")

if 'df_res' not in st.session_state:
    st.session_state.df_res = None


@st.cache_resource
def cargar_modelos():
    cortes = [12, 24, 36, 48, 60]
    modelos = {}
    for m in cortes:
        path = f"model/pipeline_{m}m.pkl"
        if os.path.exists(path):
            modelos[m] = joblib.load(path)
    return modelos


@st.cache_data
def cargar_referencia():
    if os.path.exists("data/referencia_pacientes.csv"):
        return pd.read_csv("data/referencia_pacientes.csv")
    return pd.DataFrame()


modelos = cargar_modelos()
df_ref = cargar_referencia()

# --- MAPEO DE RECHAZO (Tu lógica de simulación) ---
mapeo_rechazo = {
    'C + Q + Rnor': ['C + Q + Rnor', 'Cr + Q + Rnor'],
    'Cn + Q + Rs': ['Cn + Q + Rs', 'Cn + Q + Rr'],
    'C + nQ + Rnor': ['C + nQ + Rnor', 'Cr + nQ + Rnor'],
    'Cn + nQ + Rnor': ['Cn + nQ + Rnor'],
    'Cn + nQ + Rs': ['Cn + nQ + Rs', 'Cn + nQ + Rr'],
    'C + Q + Rs': ['C + Q + Rs', 'Cr + Q + Rs', 'C + Q + Rr', 'Cr + Q + Rr'],
    'C + nQ + Rr': ['C + nQ + Rr', 'Cr + nQ + Rr', 'C + nQ + Rs', 'Cr + nQ + Rs'],
    'Cr + nQ + Rs': ['Cr + nQ + Rs', 'C + nQ + Rs', 'C + nQ + Rr', 'Cr + nQ + Rr']
}

st.title("🔬 Simulación de Escenarios Terapéuticos")

# 2. Buscador por ID (Sidebar)
st.sidebar.header("🔍 Cargar Paciente")
id_input = st.sidebar.text_input("Ingrese Patient ID:")
paciente_data = None
if id_input and not df_ref.empty:
    res = df_ref[df_ref['Patient ID'].astype(str) == id_input]
    if not res.empty:
        paciente_data = res.iloc[0]
        st.sidebar.success(f"Paciente {id_input} cargado")

# 3. Formulario de Datos (Variables Fijas)
with st.expander("👤 Configurar Perfil del Paciente", expanded=True):
    col1, col2, col3 = st.columns(3)
    with col1:
        sex = st.selectbox("Sexo", ["Male", "Female"],
                           index=0 if paciente_data is None else (0 if paciente_data['Sex'] == 'Male' else 1))
        age_group = st.selectbox("Grupo de Edad", [1, 2, 3, 4, 5, 6],
                                 index=int(paciente_data['age_group']) - 1 if paciente_data is not None else 2)

    with col2:
        tumor_category = st.slider("Tamaño Tumor (Categoría)", 0, 100,
                                   int(paciente_data['tumor_category']) if paciente_data is not None else 30)
        grade = st.selectbox("Grado Clínico", [1, 2, 3, 4, 9],
                             index=2 if paciente_data is None else 0)  # Ajustar según tus datos
        tumors = st.number_input("Nro. de Tumores", 1, 10, value=int(
            paciente_data['Total number of in situ/malignant tumors for patient']) if paciente_data is not None else 1)

    with col3:
        stage = st.selectbox("Estadio Final (Stage)", [1, 2, 3, 4],
                             index=int(paciente_data['Stage_Final']) - 1 if paciente_data is not None else 0)
        histology = st.selectbox("Histología", ["Adenocarcinoma", "Squamous cell carcinoma", "Other"],
                                 index=0 if paciente_data is None else 0)
        # Selección del tratamiento base para disparar el mapeo
        trat_actual = st.selectbox("Tratamiento Base (Simulación de Rechazo)", list(mapeo_rechazo.keys()),
                                   index=list(mapeo_rechazo.keys()).index(
                                       paciente_data['tratamiento']) if paciente_data is not None and paciente_data[
                                       'tratamiento'] in mapeo_rechazo else 0)

# 4. Lógica de Simulación
if st.button("🔄 Ejecutar Simulación de Escenarios", use_container_width=True):
    if not modelos:
        st.error("No se encontraron modelos.")
    else:
        resultados = []
        lista_trats = mapeo_rechazo.get(trat_actual, [trat_actual])

        for t_cod in lista_trats:
            datos_paciente = {
                'age_group': age_group, 'tumor_category': tumor_category, 'grade_clinical': str(grade),
                'income_level': paciente_data['income_level'] if paciente_data is not None else 3,
                'Total number of in situ/malignant tumors for patient': tumors,
                'tratamiento': t_cod, 'Stage_Final': stage, 'histology_type_named': histology, 'Sex': sex
            }

            df_input = pd.DataFrame([datos_paciente])
            probs_por_mes = {}
            ultima_p = 100.0

            # Ordenamos los modelos para asegurar la curva descendente
            for m in sorted(modelos.keys()):
                prob = float(modelos[m].predict_proba(df_input)[0][1]) * 100
                if prob > ultima_p: prob = ultima_p
                probs_por_mes[f"{m}m"] = prob
                ultima_p = prob

            resultados.append({"Estrategia": t_cod, **probs_por_mes})

        st.session_state.df_res = pd.DataFrame(resultados)

# 5. Visualización (Mini-Gráficos + Tabla)
if st.session_state.df_res is not None:
    df_res = st.session_state.df_res
    st.write("---")

    # --- FILA DE MINI-GRÁFICOS (Lógica de rechazo solicitada) ---
    st.subheader("📉 Curvas de Supervivencia por Alternativa")
    cols_graf = st.columns(len(df_res))
    meses_eje = [0, 12, 24, 36, 48, 60]

    for idx, (i, row) in enumerate(df_res.iterrows()):
        with cols_graf[idx]:
            # Construir puntos de la curva (empezando en 100%)
            y_vals = [100.0] + [row[f"{m}m"] for m in [12, 24, 36, 48, 60]]

            fig_mini = go.Figure()
            fig_mini.add_trace(go.Scatter(
                x=meses_eje, y=y_vals, fill='tozeroy',
                line=dict(color='#2D5A27' if row['Estrategia'] == trat_actual else '#1f77b4', width=3)
            ))
            fig_mini.update_layout(
                title=f"<b>{row['Estrategia']}</b>", height=230,
                margin=dict(l=20, r=20, t=40, b=20),
                xaxis_visible=False, yaxis_range=[0, 105], template="plotly_white"
            )
            st.plotly_chart(fig_mini, use_container_width=True)
            st.metric("A 5 años", f"{row['60m']:.1f}%")

    # --- TABLA DETALLADA (Tu preferencia DF) ---
    st.write("### 📋 Tabla de Métricas Comparativas")
    columnas_meses = [c for c in df_res.columns if "m" in c]
    st.dataframe(
        df_res.style.format({col: "{:.2f}%" for col in columnas_meses})
        .background_gradient(cmap="YlGn", subset=columnas_meses),
        use_container_width=True, hide_index=True
    )