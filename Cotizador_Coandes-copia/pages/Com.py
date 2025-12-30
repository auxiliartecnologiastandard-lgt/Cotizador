import streamlit as st
import sys
import os

# 1. Configuración estética
st.set_page_config(initial_sidebar_state="collapsed")
st.markdown("<style>[data-testid='stSidebar']{display:none;}</style>", unsafe_allow_html=True)

# 2. Truco de magia: Añadimos la carpeta 'Computadores' a la memoria de Python
ruta_carpeta = os.path.join(os.getcwd(), "Computadores")
if ruta_carpeta not in sys.path:
    sys.path.append(ruta_carpeta)

# 3. Importamos el contenido del archivo app.py como si fuera parte de este archivo
try:
    import app 
    # Al importar 'app', se ejecutará todo el código del cotizador aquí mismo
except Exception as e:
    st.error("Error al cargar el cotizador")
    st.write(e)