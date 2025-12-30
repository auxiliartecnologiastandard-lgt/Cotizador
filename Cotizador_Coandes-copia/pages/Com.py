import streamlit as st

st.set_page_config(initial_sidebar_state="collapsed")
st.markdown("<style>[data-testid='stSidebar']{display:none;}</style>", unsafe_allow_html=True)

# LA RUTA CORRECTA: 
# Como el Lobby ya está en 'Cotizador_Coandes-copia', 
# solo necesitamos la ruta desde ahí hacia adentro.
ruta_final = "Computadores/app.py"

try:
    st.switch_page(ruta_final)
except Exception as e:
    st.error(f"Casi lo tenemos... intenté entrar a: {ruta_final}")
    st.write("Error técnico:", e)