import streamlit as st

st.set_page_config(initial_sidebar_state="collapsed")
st.markdown("<style>[data-testid='stSidebar']{display:none;}</style>", unsafe_allow_html=True)

# La ruta real según lo que detectó el buscador:
# Entra a la carpeta de la copia -> Luego a Computadores -> Luego a app.py
ruta_real = "Cotizador_Coandes-copia/Computadores/app.py"

try:
    st.switch_page(ruta_real)
except Exception as e:
    st.error(f"No se pudo encontrar: {ruta_real}")
    st.info("Verifica si dentro de 'Cotizador_Coandes-copia' existe la carpeta 'Computadores'")