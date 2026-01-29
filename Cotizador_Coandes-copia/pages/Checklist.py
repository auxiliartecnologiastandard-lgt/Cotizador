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
# Botón volver
if st.button("⬅  Volver al Menú Principal"):
    st.switch_page("Lobby.py")

with st.expander("📝 Observaciones del equipo"):
    estado = st.selectbox(
        "Estado del equipo",
        ["Bueno", "Regular", "Malo"]
    )

    observaciones = ""
    if estado != "Bueno":
        observaciones = st.text_area(
            "Detalle obligatorio",
            placeholder="Describe el daño o condición del equipo"
        )
