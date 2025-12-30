import streamlit as st
import os

# 1. Configuración de pantalla
st.set_page_config(page_title="Cotizador Coandes", initial_sidebar_state="collapsed")

# Ocultar barra lateral
st.markdown("<style>[data-testid='stSidebar']{display:none;}</style>", unsafe_allow_html=True)

# 2. RUTA MANUAL (Basada en tu error anterior)
# El error decía que estás en: /mount/src/cotizador/Cotizador_Coandes-copia/pages/Com.py
# Queremos ir a: /mount/src/cotizador/Cotizador_Coandes-copia/Computadores/app.py

ruta_al_archivo = "Computadores/app.py"

if os.path.exists(ruta_al_archivo):
    try:
        # LA LLAVE MAESTRA: Lee el código y lo ejecuta
        with open(ruta_al_archivo, "r", encoding="utf-8") as file:
            codigo = file.read()
        exec(codigo)
    except Exception as e:
        st.error("Error al ejecutar el código del cotizador")
        st.exception(e)
else:
    st.error(f"No se encontró el archivo en: {os.path.abspath(ruta_al_archivo)}")
    # Auxilio visual para saber dónde estamos
    st.write("Archivos detectados en la raíz:", os.listdir("."))