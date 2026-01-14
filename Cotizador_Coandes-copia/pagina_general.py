# pages/pagina_general.py
import streamlit as st

origen = st.session_state.get('origen', 'desconocido')
st.write(f"Entraste desde: {origen}")