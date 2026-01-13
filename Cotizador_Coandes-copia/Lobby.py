import streamlit as st
import os


st.markdown("""
    <style>
    .stApp { background-color: #FF0000; }
    * { color: #FFFFFF !important; }
    </style>
    """, unsafe_allow_html=True)

# 0. Ubicar la imagen del logo
ruta_base = os.path.dirname(__file__)
ruta_logo = os.path.join(ruta_base, "Standard_logo.png")

# 1. Configuración de la pagina
st.set_page_config(
    page_title="Cotizador Coandes",
    initial_sidebar_state="collapsed"
)

st.markdown(
    """
    <style>
        /* Elimina el botón > de la esquina superior izquierda */
        [data-testid="collapsedControl"] {
            display: none !important;
        }

        /* Elimina la barra lateral por completo */
        [data-testid="stSidebar"] {
            display: none !important;
        }
        
        /* Elimina el encabezado superior para que no quede espacio vacío */
        header {
            visibility: hidden !important;
            height: 0 !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.set_page_config(page_title="Lobby de Ventas", layout="wide")


# 2. Tamaño y orietación del logo y titulo
col_izq, col_centro, col_der = st.columns([0.000000000000000000000000000000001, 0.025, 0.2]) 

if os.path.exists(ruta_logo):
    with col_centro:
        st.image(ruta_logo, width=200)
with col_der:
    st.title("Sistema de Cotización Inteligente")
    st.write("Bienvenido/a. Selecciona una categoría para empezar:")
    st.divider()

# 3. Botones del menu
# 3.1 Color de las letras y el fondo
st.markdown("""
    <style>
    
    /* Estilo para los botones */
    .stButton>button {
        background-color: #FF0000 !important; /* Fondo blanco */
        color: #FFFFFF !important;           /* Texto negro */
        border: 2px solid #000000 !important; /* Borde rojo como tu logo */
    }
    </style>
    """, unsafe_allow_html=True)
 # 3.2 Configuración botones
col1, col2, col3, = st.columns(3)

with col1:
    if st.button ("💻 Computadores",  use_container_width=True):
        st.switch_page("pages/Com.py")

with col2:
    if st.button("🧊 Neveras", use_container_width=True):
        st.switch_page("pages/Nev.py")

with col3:
    if st.button("Motos (Próximamente)", use_container_width=True, disabled=True):
        pass
        st.switch_page("pages/Mot.py")

with col1:
    if st.button("Oro (Próximamente)", use_container_width=True, disabled=True):
        pass
        st.switch_page("pages/Oro.py")