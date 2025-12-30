import streamlit as st
import os
import sys

st.set_page_config(page_title="Diagnóstico", initial_sidebar_state="collapsed")

# 1. Verificamos si joblib está instalado
try:
    import joblib
    st.success("✅ ¡Increíble! joblib SÍ está instalado. El problema es la ruta.")
except ImportError:
    st.error("❌ joblib NO está instalado. El archivo requirements.txt falló.")

# 2. Verificamos dónde está parado el servidor
st.write("### Diagnóstico de Carpeta")
st.write(f"Estás aquí: `{os.getcwd()}`")
st.write("Archivos que veo aquí afuera:")
st.json(os.listdir("."))

# 3. Verificamos si existe la carpeta de la copia
if os.path.exists("Cotizador_Coandes-copia"):
    st.write("Contenido de 'Cotizador_Coandes-copia':")
    st.json(os.listdir("Cotizador_Coandes-copia"))