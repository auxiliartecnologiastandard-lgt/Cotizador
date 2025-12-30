import streamlit as st
import os

st.set_page_config(initial_sidebar_state="collapsed")

def buscar_archivo(nombre_archivo, ruta_inicial="."):
    """Busca un archivo en todas las subcarpetas."""
    for raiz, dirs, archivos in os.walk(ruta_inicial):
        if nombre_archivo in archivos:
            # Retorna la ruta relativa quitando el './' inicial
            return os.path.join(raiz, nombre_archivo).replace("./", "")
    return None

# 1. Intentamos encontrar la ruta real de app.py
ruta_encontrada = buscar_archivo("app.py")

if ruta_encontrada:
    try:
        # 2. Si lo encuentra, salta automáticamente
        st.switch_page(ruta_encontrada)
    except Exception as e:
        st.error(f"Error al intentar saltar a: {ruta_encontrada}")
        st.write(e)
else:
    # 3. Si no lo encuentra, nos muestra el mapa del tesoro para ver qué pasa
    st.error("❌ No se encontró 'app.py' en ningún lugar del repositorio.")
    st.write("Estructura detectada para que revises:")
    for raiz, dirs, archivos in os.walk("."):
        nivel = raiz.replace(".", "").count(os.sep)
        sangria = " " * 4 * (nivel)
        st.text(f"{sangria}📁 {os.path.basename(raiz)}/")
        for f in archivos:
            st.text(f"{sangria}    📄 {f}")