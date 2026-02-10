import streamlit as st

def set_design(section="general"):

    images = {
        "home": "https://images.unsplash.com/photo-1532187875605-1ef6c8169143?q=80&w=2000",
        "eda": "https://images.unsplash.com/photo-1551288049-bbda38a5f9ce?q=80&w=2000",
        "metodologia": "https://images.unsplash.com/photo-1454165833762-0204b2816721?q=80&w=2000",
        "prediction": "https://images.unsplash.com/photo-1576086213369-97a306d36557?q=80&w=2000",
        "equipo": "https://images.unsplash.com/photo-1522071820081-009f0129c71c?q=80&w=2000",
        "conclusiones": "https://images.unsplash.com/photo-1434030216411-0b793f4b4173?q=80&w=2000",
        "general": "https://images.unsplash.com/photo-1504813184591-01572f98c85f?q=80&w=2000"
    }

    bg = images.get(section, images["general"])

    st.markdown(f"""
    <style>

    /* ===== OCULTA HEADER NATIVO STREAMLIT ===== */
    header {{visibility: hidden; height: 0px;}}
    [data-testid="stToolbar"] {{display: none;}}

    /* ===== FONDO CLÍNICO CLARO ===== */
    .stApp {{
        background:
            linear-gradient(rgba(255,255,255,0.90), rgba(255,255,255,0.90)),
            url("{bg}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* ===== CONTENEDOR PRINCIPAL ===== */
    .block-container {{
        max-width: 1100px;
        padding-top: 1rem !important;
        padding-bottom: 2rem;
    }}

    [data-testid="stAppViewContainer"] > .main {{
        padding-top: 0rem;
    }}

    /* ===== TARJETAS ===== */
    .card {{
        background: white;
        border-radius: 16px;
        padding: 30px;
        box-shadow: 0 10px 35px rgba(0,0,0,0.08);
        border: 1px solid #e5e7eb;
        margin-bottom: 1.2rem;
        transition: 0.2s ease;
    }}
    /* ===== PANEL PRINCIPAL HOME ===== */
    .panel {{
        background: white;
        border-radius: 18px;
        padding: 40px;
        box-shadow: 0 12px 40px rgba(0,0,0,0.08);
        border: 1px solid #e5e7eb;
        margin-bottom: 1.5rem;
        text-align: center;
    }}

    /* ===== TARJETAS DE NAVEGACIÓN ===== */
    .nav-tile {{
        background: white;
        border-radius: 16px;
        padding: 30px 20px;
        border: 1px solid #e5e7eb;
        text-align: center;
        transition: all 0.25s ease;
        box-shadow: 0 6px 20px rgba(0,0,0,0.05);
    }}

    .nav-tile:hover {{
        transform: translateY(-4px);
        box-shadow: 0 14px 35px rgba(0,0,0,0.10);
        border-color: #2563eb;
    }}

    /* ICONO */
    .nav-icon {{
        font-size: 2.4rem;
        margin-bottom: 12px;
    }}

    /* TITULO */
    .nav-title {{
        font-size: 1.05rem;
        font-weight: 600;
        color: #1e293b;
    }}
    .card:hover {{
        transform: translateY(-2px);
        box-shadow: 0 14px 40px rgba(0,0,0,0.10);
    }}

    /* ===== BOTONES ===== */
    .stButton button {{
        background: linear-gradient(135deg, #2563eb, #1d4ed8);
        color: white;
        border-radius: 10px;
        border: none;
        padding: 0.6rem 1.5rem;
        font-weight: 600;
    }}

    /* ===== INPUTS ===== */
    .stSelectbox > div,
    .stNumberInput > div {{
        background: white;
        border-radius: 10px;
        border: 1px solid #e5e7eb;
    }}

    /* ===== METRICS ===== */
    [data-testid="stMetric"] {{
        background: white;
        padding: 15px;
        border-radius: 12px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }}

    /* ===== INDICADORES DE RIESGO ===== */
    .risk-low {{
        background: #dcfce7;
        color: #166534;
        padding: 8px 14px;
        border-radius: 8px;
        font-weight: 600;
        display: inline-block;
    }}

    .risk-medium {{
        background: #fef9c3;
        color: #854d0e;
        padding: 8px 14px;
        border-radius: 8px;
        font-weight: 600;
        display: inline-block;
    }}

    .risk-high {{
        background: #fee2e2;
        color: #991b1b;
        padding: 8px 14px;
        border-radius: 8px;
        font-weight: 600;
        display: inline-block;
    }}

    /* ===== TABLAS ===== */
    .stDataFrame, [data-testid="stTable"] {{
        background: white;
        border-radius: 12px;
        padding: 10px;
        border: 1px solid #e5e7eb;
    }}

    </style>
    """, unsafe_allow_html=True)
