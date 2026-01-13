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
        
        /* Quitamos el icono predeterminado de la caja de info */
        [data-testid="stNotificationIcon"] { display: none !important; }
        /* Ajustamos el color de la franja (puedes cambiar el LightBlue) */
        [data-testid="stNotification"] {
            background-color: #F0F2F6 !important; 
            border: none !important;
            color: black !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# 2. Encabezado (LOGO Y TITULO DENTRO DE UNA FRANJA)
with st.container():
    # Usamos st.info como "franja" de color porque Streamlit sí permite columnas dentro
    with st.chat_message("assistant", avatar=None): # El chat_message crea un fondo gris garantizado
        col_logo, col_titulo = st.columns([0.2, 0.8])
        
        with col_logo:
            if os.path.exists(ruta_logo):
                st.image(ruta_logo, width=150)
        
        with col_titulo:
            st.title("Sistema de Cotización Inteligente")
            st.write("Bienvenido/a. Selecciona una categoría para empezar:")

# 3. Resto de la página (Fondo normal)
st.divider()

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("💻 Computadores", use_container_width=True):
        st.switch_page("pages/Com.py")
with col2:
    if st.button("🧊 Neveras", use_container_width=True):
        st.switch_page("pages/Nev.py")
# ... el resto de tus botones ...