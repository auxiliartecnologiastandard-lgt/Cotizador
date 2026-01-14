import streamlit as st
import os

# 1. Configuración de pantalla
st.set_page_config(page_title="Cotizador Coandes", initial_sidebar_state="collapsed")

# Ocultar barra lateral
st.markdown("<style>[data-testid='stSidebar']{display:none;}</style>", unsafe_allow_html=True)

# 2. RUTA EXACTA
ruta_archivo = os.path.join("Cotizador_Coandes-copia", "Neveras", "app.py")

if os.path.exists(ruta_archivo):
    try:
        st.switch_page("pages/Nev.py")
    except Exception as e:
        st.error("Error al ejecutar el cotizador")
        st.exception(e)
else:
    st.error(f"No se encontró el archivo en: {ruta_archivo}")