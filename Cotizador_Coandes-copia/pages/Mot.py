import streamlit as st
import os

# 1. Configuración de pantalla
st.set_page_config(page_title="Cotizador Computadores", initial_sidebar_state="collapsed")

# Ocultar barra lateral
st.markdown("<style>[data-testid='stSidebar']{display:none;}</style>", unsafe_allow_html=True)

# 2. RUTA EXACTA (Basada en tu diagnóstico)
# El archivo está en: Cotizador_Coandes-copia/Computadores/app.py
ruta_archivo = os.path.join("Cotizador_Coandes-copia", "Motos", "app.py")

if os.path.exists(ruta_archivo):
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as f:
            codigo = f.read()
        
        # Como ya tenemos joblib (CUADRO VERDE), esto ya no fallará
        exec(codigo)
        
    except Exception as e:
        st.error("Error al ejecutar el cotizador")
        st.exception(e)
else:
    st.error(f"No se encontró el archivo en: {ruta_archivo}")