import streamlit as st
import os

# 1. Configuración de pantalla
st.set_page_config(page_title="Cotizador Coandes", initial_sidebar_state="collapsed")

# Ocultar barra lateral
st.markdown("<style>[data-testid='stSidebar']{display:none;}</style>", unsafe_allow_html=True)

# 2. RUTA CORREGIDA SEGÚN TU ESTRUCTURA REAL
# Entramos a la carpeta de la copia, luego a Computadores y luego al app.py
ruta_archivo = "Cotizador_Coandes-copia/Computadores/app.py"

# 3. EJECUCIÓN
if os.path.exists(ruta_archivo):
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as f:
            codigo = f.read()
        
        # Ejecutamos el código del cotizador aquí mismo
        exec(codigo)
        
    except Exception as e:
        st.error("Error al ejecutar el código del cotizador")
        st.exception(e)
else:
    st.error(f"❌ Sigue sin aparecer en: {ruta_archivo}")
    # Si esto falla, miramos qué hay DENTRO de la carpeta de copia
    try:
        st.write("Contenido de 'Cotizador_Coandes-copia':", os.listdir("Cotizador_Coandes-copia"))
    except:
        st.write("No se pudo leer la carpeta interna.")