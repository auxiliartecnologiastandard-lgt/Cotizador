import streamlit as st
import os

# 1. Configuración de página (solo aquí, no en app.py)
st.set_page_config(page_title="Cotizador Coandes", initial_sidebar_state="collapsed")

# Ocultar barra lateral
st.markdown("<style>[data-testid='stSidebar']{display:none;}</style>", unsafe_allow_html=True)

# 2. Definir la ruta relativa
# Como estamos en /pages/, subimos un nivel para encontrar /Computadores/
ruta_archivo = os.path.join("Computadores", "app.py")

# 3. EJECUCIÓN DIRECTA (La llave maestra)
if os.path.exists(ruta_archivo):
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as f:
            codigo = f.read()
        
        # Ejecutamos el código del cotizador
        exec(codigo)
        
    except Exception as e:
        st.error("Error al ejecutar el cotizador")
        st.exception(e)
else:
    st.error(f"❌ No se encontró el archivo en: {ruta_archivo}")
    st.info("Revisando carpetas disponibles...")
    st.write("En la raíz hay:", os.listdir("."))