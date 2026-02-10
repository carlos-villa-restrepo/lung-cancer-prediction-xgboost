import streamlit as st
import base64
import os
from utils import set_design

set_design("equipo")


def get_base64(bin_file):
    if os.path.exists(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return f"data:image/jpeg;base64,{base64.b64encode(data).decode()}"
    return ""


# --- CSS DE ALTO IMPACTO ---
st.markdown("""
    <style>
    .team-container {
        display: flex;
        flex-direction: column;
        gap: 20px;
        padding: 10px;
    }

    .team-widget {
        display: flex;
        align-items: center;
        background: linear-gradient(145deg, #ffffff, #f8fafc);
        border-left: 5px solid #3182ce; /* Línea de color acento */
        border-radius: 20px;
        padding: 25px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }

    .team-widget:hover {
        transform: translateY(-5px) scale(1.01);
        box-shadow: 0 15px 35px rgba(49, 130, 206, 0.15);
        border-left: 8px solid #2c5282;
    }

    .widget-img {
        width: 130px;
        height: 130px;
        border-radius: 50%; /* Imagen circular para look más moderno */
        object-fit: cover;
        margin-right: 30px;
        border: 4px solid white;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }

    .widget-info {
        flex-grow: 1;
    }

    .widget-name {
        font-size: 24px;
        font-weight: 800;
        color: #1a202c;
        margin-bottom: 5px;
        font-family: 'Inter', sans-serif;
    }

    /* Estilo tipo 'Badge' para el rol */
    .widget-role {
        display: inline-block;
        padding: 4px 12px;
        background: #ebf8ff;
        color: #3182ce;
        font-size: 13px;
        font-weight: 700;
        border-radius: 50px;
        text-transform: uppercase;
        margin-bottom: 15px;
    }

    .widget-links {
        display: flex;
        gap: 12px;
    }

    .widget-links a {
        text-decoration: none;
        display: flex;
        align-items: center;
        gap: 8px;
        background: white;
        padding: 8px 16px;
        border-radius: 10px;
        font-size: 14px;
        font-weight: 600;
        color: #4a5568;
        border: 1px solid #e2e8f0;
        transition: all 0.3s;
    }

    .widget-links a:hover {
        background: #3182ce;
        color: white;
        border-color: #3182ce;
        box-shadow: 0 4px 12px rgba(49, 130, 206, 0.2);
    }
    </style>
""", unsafe_allow_html=True)

st.title("🚀 Equipo de Desarrollo")
st.write("Conoce a los integrantes del equipo.")


def team_widget(nombre, rol, path_foto, linkedin, github):
    img_base64 = get_base64(path_foto)

    st.markdown(f"""
        <div class="team-widget">
            <img src="{img_base64}" class="widget-img">
            <div class="widget-info">
                <div class="widget-name">{nombre}</div>
                <div class="widget-role">{rol}</div>
                <div class="widget-links">
                    <a href="{linkedin}" target="_blank"><span>🔗</span> LinkedIn</a>
                    <a href="{github}" target="_blank"><span>💻</span> GitHub</a>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)


# Listado de integrantes
team_widget("Betania Medina", "Data Scientist", "assets/betania.jpg",
            "https://linkedin.com/in/betania-medina-b2b733269/", "https://github.com/Betaniammc")
st.write("---")
team_widget("Carlos Restrepo", "Data Scientist", "assets/carlos.jpg",
            "https://www.linkedin.com/in/carlos-restrepo-a7b188390/", "https://github.com/carlos-villa-restrepo")
st.write("---")
team_widget("Elius Trujillo", "Data Scientist", "assets/elius.jpg",
            "https://www.linkedin.com/in/elius-trujillo", "https://github.com/elius123ef")