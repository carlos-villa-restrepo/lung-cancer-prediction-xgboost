import streamlit as st
from utils import set_design

st.set_page_config(page_title="Lung Cancer Diagnosis & Life Expectancy", layout="wide")
set_design("home")

# ===== HERO =====
with st.container():


    st.title("🧬 Lung Cancer Diagnosis & Life Expectancy")
    st.write("---")
    st.write("""
    Sistema de apoyo clínico basado en Machine Learning para estimar
    la probabilidad de supervivencia en pacientes con cáncer de pulmón.
    """)

    st.markdown('</div>', unsafe_allow_html=True)
    st.write("---")
st.markdown("### 🧭 Explorar el sistema")

# ===== GRID NAVEGACIÓN =====
row1 = st.columns(3)
row2 = st.columns(3)

def nav_card(col, icon, title, page, key):
    with col:
        st.markdown(f"""
        <div class="nav-tile">
            <div class="nav-icon">{icon}</div>
            <div class="nav-title">{title}</div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Abrir módulo", key=key):
            st.switch_page(page)

nav_card(row1[0], "📚", "Metodología", "pages/1_📚_Metodologia.py", "met")
nav_card(row1[1], "📊", "EDA", "pages/2_📊_EDA.py", "eda")
nav_card(row1[2], "🧠", "Predicción", "pages/3_🧠_Prediccion.py", "pred")

nav_card(row2[0], "⚕️", "Escenarios", "pages/4_⚕️_Escenarios_Tratamiento.py", "esc")
nav_card(row2[1], "📈", "Rendimiento", "pages/5_📈_Rendimiento_Modelos.py", "rend")
nav_card(row2[2], "👨‍💻", "Equipo", "pages/7_👨‍💻_Equipo.py", "team")
