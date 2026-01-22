import streamlit as st
import pandas as pd
import joblib
import os
import matplotlib.pyplot as plt

# 1. CONFIGURACIÓN Y DISEÑO (FONDO Y ESTILOS)
st.set_page_config(page_title="Estimador de Supervivencia - Comparativa", layout="wide")


def apply_custom_design():
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(rgba(10, 20, 40, 0.85), rgba(10, 20, 40, 0.85)), 
                        url("https://images.unsplash.com/photo-1576086213369-97a306d36557?q=80&w=2080&auto=format&fit=crop");
            background-size: cover; background-attachment: fixed;
        }
        .main .block-container {
            background-color: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(15px); border-radius: 15px; padding: 3rem;
            border: 1px solid rgba(0, 150, 255, 0.2);
        }
        [data-testid="stSidebar"] { background-color: rgba(5, 15, 30, 0.95) !important; }
        h1, h2, h3, p, label { color: #e0e0e0 !important; }
        .stMetricValue { color: #00d4ff !important; font-weight: bold; }
        </style>
        """,
        unsafe_allow_html=True
    )


apply_custom_design()


# 2. CARGA DINÁMICA DE MODELOS
@st.cache_resource
def load_selected_model(model_file):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(current_dir, '..', 'models', model_file)
    return joblib.load(model_path)


# 3. INTERFAZ LATERAL (CONFIGURACIÓN + GLOSARIO)
st.sidebar.header("⚙️ Configuración")

# Selector de Modelo
model_choice = st.sidebar.selectbox(
    "Modelo Predictivo:",
    ["Random Forest (MAE: 16.28)", "XGBoost (MAE: 17.90)"]
)

model_file = "survival_random_forest.pkl" if "Random Forest" in model_choice else "survival_xgboost_final.pkl"
model = load_selected_model(model_file)

st.sidebar.markdown("---")
st.sidebar.header("📋 Datos del Paciente")
sur_val = st.sidebar.radio("¿Cirugía Realizada?", ["No", "Sí"])
stg_val = st.sidebar.selectbox("Etapa del Cáncer", ["Localized", "Regional", "Distant"])
inc_val = st.sidebar.selectbox("Nivel de Ingresos", ["menor_a_$40,000", "70,000_-_74,999", "120,000plus"])

# GLOSARIO EN LA BARRA LATERAL
st.sidebar.markdown("---")
with st.sidebar.expander("📖 Glosario de Variables"):
    st.write("**Has_Surgery:** Intervención quirúrgica del tumor primario.")
    st.write("**Stage:** Extensión anatómica (Localized: un órgano, Regional: ganglios, Distant: metástasis).")
    st.write("**Income:** Nivel socioeconómico del área de residencia.")

# Mapeo de datos
data = {col: 0 for col in model.feature_names_in_}
if "Has_Surgery" in data: data["Has_Surgery"] = 1 if sur_val == "Sí" else 0
for col in data.keys():
    if stg_val in col: data[col] = 1
    if inc_val in col: data[col] = 1
input_df = pd.DataFrame([data])

# 4. PANTALLA PRINCIPAL
st.title("🎗️ Estimador de Supervivencia")
st.subheader(f"Análisis mediante: {model_choice.split('(')[0]}")

if st.button("Realizar Pronóstico"):
    prediction = model.predict(input_df)[0]

    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("Resultado")
        st.metric("Vida Estimada", f"{prediction:.1f} meses")
        st.write("---")
        st.write("**Resumen del Perfil:**")
        st.write(f"- Etapa: **{stg_val}**")
        st.write(f"- Cirugía: **{sur_val}**")

    with col2:
        st.subheader("Importancia de Factores")

        # Extraer importancias del modelo seleccionado
        importancias = model.feature_importances_
        df_imp = pd.DataFrame({'Variable': model.feature_names_in_, 'Imp': importancias})

        # Filtrar variables activas + cirugía (para que siempre se vea)
        df_plot = df_imp[(input_df.iloc[0].values > 0) | (df_imp['Variable'] == "Has_Surgery")].copy()

        # Limpieza de nombres para el gráfico
        df_plot['Variable'] = df_plot['Variable'].str.replace("Stage_Consolidated_", "").str.replace("Income_Level_",
                                                                                                     "")
        df_plot = df_plot.sort_values('Imp', ascending=True)

        # Gráfico
        fig, ax = plt.subplots(figsize=(10, 5))
        plt.style.use('dark_background')
        fig.patch.set_alpha(0)
        ax.set_facecolor("none")

        max_val = max(df_plot['Imp'].max(), 0.1)
        ax.barh(df_plot['Variable'], df_plot['Imp'], color='#00d4ff', edgecolor='white')
        ax.set_xlim(0, max_val + 0.05)

        st.pyplot(fig)

        st.markdown("---")  # Una línea divisoria para separar
        with st.expander("🔬 Nota técnica: ¿Por qué la Cirugía marca 0.0000?"):
            st.info("""
                    **Explicación para la defensa del proyecto:**

                    1. **Dominancia de la Etapa:** La variable 'Stage' es un predictor tan potente en este modelo que absorbe estadísticamente la importancia de la cirugía.
                    2. **Desbalance de Datos:** Al revisar `value_counts()` en el dataset, se observa que la gran mayoría de los pacientes no tienen cirugía registrada, lo que reduce su peso en el entrenamiento.
                    3. **Filtro de Ruido:** El algoritmo XGBoost prioriza variables con mayor varianza para evitar el sobreajuste (overfitting).
                    """)

        # EXPLICACIÓN TÉCNICA
        with st.expander("🔬 Nota sobre la importancia y el modelo"):
            if "Random Forest" in model_choice:
                st.write("El **Random Forest** es el modelo más preciso del proyecto (MAE: 16.28).")
            else:
                st.write("El **XGBoost** (MAE: 17.90) muestra una mayor sensibilidad a la Etapa Clínica.")

            if df_plot[df_plot['Variable'] == 'Has_Surgery']['Imp'].values[0] <= 0.001:
                st.info(
                    "La cirugía muestra importancia marginal debido al desbalance en el dataset original (`value_counts`), donde la Etapa Clínica domina la varianza estadística.")