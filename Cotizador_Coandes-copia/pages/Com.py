import streamlit as st
import sys
import os
import importlib.util

# 1. Estética limpia
st.set_page_config(initial_sidebar_state="collapsed")
st.markdown("<style>[data-testid='stSidebar']{display:none;}</style>", unsafe_allow_html=True)

# 2. RUTA EXACTA (Ajustada a tu estructura de GitHub)
# Buscamos: /mount/src/cotizador/Cotizador_Coandes-copia/Computadores/app.py
ruta_proyecto = os.path.dirname(os.path.dirname(__file__)) # Sube un nivel desde 'pages'
ruta_app = os.path.join(ruta_proyecto, "Computadores", "app.py")

# 3. CARGA DINÁMICA (Sin usar 'import app' normal)
if os.path.exists(ruta_app):
    try:
        spec = importlib.util.spec_from_file_location("modulo_cotizador", ruta_app)
        modulo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(modulo) 
        # Esto ejecuta el código de app.py aquí mismo
    except Exception as e:
        st.error("Error al ejecutar el cotizador")
        st.exception(e)
else:
    st.error(f"❌ No encontré el archivo en: {ruta_app}")
    # Si falla, te mostrará qué hay en esa carpeta para corregirlo
    if os.path.exists(ruta_proyecto):
        st.write("Dentro de la carpeta encontré:", os.listdir(ruta_proyecto))