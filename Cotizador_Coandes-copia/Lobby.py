import streamlit as st
import os

# 0. Ubicar la imagen del logo
ruta_base = os.path.dirname(__file__)
ruta_logo = os.path.join(ruta_base, "Standard_logo.png")

# 1. Configuración de la pagina
st.set_page_config(page_title="Lobby", initial_sidebar_state="collapsed", layout="wide")
st.markdown(
    """
    <style>
        [data-testid="collapsedControl"], [data-testid="stSidebar"] { display: none !important; }
        header { visibility: hidden !important; height: 0 !important; }
        
        /* Esto hace que el contenedor de botones se vea como una "zona" diferente */
        .stElementContainer div[data-testid="stVerticalBlockBorderWrapper"] {
            background-color: #F0F2F6; /* Color gris sutil para la zona de botones */
            padding: 20px;
            border-radius: 15px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# 2. Encabezado (Logo y Título)
col_logo, col_titulo = st.columns([0.2, 0.8]) 

if os.path.exists(ruta_logo):
    with col_logo:
        st.image(ruta_logo, width=180)
with col_titulo:
    st.title("Sistema de Cotización Inteligente")
    st.write("Bienvenido/a. Selecciona una categoría para empezar:")

st.divider()

# 3. ZONA DIVIDIDA (Contenedor de botones)
# Todo lo que esté dentro de este "with" se verá como una sección aparte
with st.container(border=True):
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Computadores", use_container_width=True):
            st.switch_page("pages/Com.py")
        if st.button("Oro (Próximamente)", use_container_width=True, disabled=True):
            pass

    with col2:
        if st.button("Neveras", use_container_width=True):
            st.switch_page("pages/Nev.py")
        if st.button("Herramientas (Próximamente)", use_container_width=True, disabled=True):
            pass

    with col3:
        if st.button("Motos (Próximamente)", use_container_width=True, disabled=True):
            pass
        if st.button("Instrumentos (Próximamente)", use_container_width=True, disabled=True):
            pass