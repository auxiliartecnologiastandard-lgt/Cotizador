import streamlit as st
import os

st.set_page_config(initial_sidebar_state="collapsed")

# 1. ESTO NOS DIRÁ LA VERDAD
st.title("🔍 Buscador de archivos")
archivos_raiz = os.listdir(".") # Mira la carpeta principal
st.write("Archivos en la raíz del proyecto:", archivos_raiz)

# 2. INTENTO DE NAVEGACIÓN DINÁMICA
# Ajusta el nombre según lo que veas en la lista de arriba
if "Computadores" in archivos_raiz:
    st.success("✅ Carpeta 'Computadores' encontrada")
    archivos_comp = os.listdir("Computadores")
    st.write("Archivos dentro de Computadores:", archivos_comp)
    
    if st.button("🚀 Forzar entrada al Cotizador"):
        st.switch_page("Computadores/app.py")
else:
    st.error("❌ No veo ninguna carpeta llamada 'Computadores'")
    st.info("Revisa si tiene mayúsculas, espacios o si se llama 'Computadoras'")