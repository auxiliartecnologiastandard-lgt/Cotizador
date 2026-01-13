import streamlit as st
import os

# 0. Ubicar la imagen del logo
ruta_base = os.path.dirname(__file__)
ruta_logo = os.path.join(ruta_base, "Standard_logo.png")

# 1. Configuración de la pagina
st.set_page_config(page_title="Lobby", initial_sidebar_state="collapsed", layout="wide")

# CSS GLOBAL: Aquí le decimos que el PRIMER contenedor de la página sea gris
st.markdown(
    """
    <style>
        /* Ocultar elementos de Streamlit */
        [data-testid="collapsedControl"], [data-testid="stSidebar"] { display: none !important; }
        header { visibility: hidden !important; height: 0 !important; }

        /* EL TRUCO: Colorear el bloque superior */
        [data-testid="stVerticalBlock"] > div:first-child {
            background-color: #FF0000; /* Gris claro */
            padding: 30px;
            border-radius: 15px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# 2. ENCABEZADO (Debe ser lo primero que aparezca en el código)
# Al ser el primer elemento, el CSS de arriba lo pintará de gris
col_logo, col_titulo = st.columns([0.2, 0.8])

if os.path.exists(ruta_logo):
    with col_logo:
        st.image(ruta_logo, width=180)

with col_titulo:
    st.title("Sistema de Cotización Inteligente")
    st.write("Bienvenido/a. Selecciona una categoría para empezar:")

# 3. ESPACIO Y BOTONES (Esto quedará con fondo normal)
st.write("") # Un espacio para salir de la zona gris
st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("💻 Computadores", use_container_width=True):
        st.switch_page("pages/Com.py")

with col2:
    if st.button("🧊 Neveras", use_container_width=True):
        st.switch_page("pages/Nev.py")

with col3:
    if st.button("🛵 Motos (Próximamente)", use_container_width=True, disabled=True):
        pass