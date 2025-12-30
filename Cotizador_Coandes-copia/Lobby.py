import streamlit as st

st.set_page_config(
    page_title="Cotizador Coandes",
    initial_sidebar_state="collapsed" # Esto la cierra al cargar
)
st.set_page_config(page_title="Lobby de Ventas", layout="wide")


# 1.1. Tamaño y orietación del logo y titulo
col_izq, col_centro, col_der = st.columns([0.000000000000000000000000000000001, 0.025, 0.2]) 

with col_der:
    st.title("Sistema de Cotización Inteligente")
    st.write("Bienvenido. Selecciona una categoría para empezar:")
    st.divider()

# 3. Botones des menu
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("💻 Computadores", use_container_width=True):
        st.switch_page("pages/Com.py")

with col2:
    if st.button("Neveras (Próximamente)", use_container_width=True, disabled=True):
        pass

with col3:
    if st.button("Motos (Próximamente)", use_container_width=True, disabled=True):
        pass

with col4:
    if st.button("Oro (Próximamente)", use_container_width=True, disabled=True):
        pass