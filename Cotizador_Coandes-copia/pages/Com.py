import streamlit as st
import os

# 1. Configuración de estética limpia (Sin barra lateral)
st.set_page_config(page_title="Cargando Cotizador...", initial_sidebar_state="collapsed")

# Ocultar la barra lateral por completo
st.markdown("<style>[data-testid='stSidebar']{display:none;}</style>", unsafe_allow_html=True)

# 2. EL SALTO DIRECTO (El reemplazo de runpy)
# En Streamlit Cloud, la ruta debe ser relativa desde la raíz del proyecto
# Si tu archivo real se llama app.py y está dentro de la carpeta Computadores:
ruta_objetivo = "Computadores/app.py"

try:
    st.switch_page(ruta_objetivo)
except Exception as e:
    st.error("No se pudo encontrar el archivo del cotizador.")
    # Esto te ayudará a ver qué archivos detecta el servidor actualmente
    st.write("Buscando en:", ruta_objetivo)
    st.info("Verifica que en GitHub la carpeta se llame 'Computadores' y el archivo 'app.py'")