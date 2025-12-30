import runpy
import os
import streamlit as st

# 1. Ocultar el menú lateral también aquí
st.set_page_config(initial_sidebar_state="collapsed")
st.markdown("<style>[data-testid='stSidebar']{display:none;}</style>", unsafe_allow_html=True)

# 2. Ruta hacia tu carpeta organizada
# Buscamos el archivo real dentro de la carpeta 'Computadoras'
ruta = os.path.join("Computadores", "app.py")

# 3. ¡Ejecutar el código!
runpy.run_path(ruta)