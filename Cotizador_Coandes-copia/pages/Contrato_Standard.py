import streamlit as st

st.set_page_config(page_title="Contrato de Compraventa")

st.title("📄 Contrato de Compraventa – Nevera")

datos = st.session_state.get("datos_cotizador")

if not datos:
    st.warning("No hay datos del cotizador. Regresa y calcula primero.")
    st.stop()

# Mostrar solo datos de nevera
if datos["Origen"] != "nevera":
    st.error("Este contrato no corresponde a una nevera.")
    st.stop()

st.write(f"**Marca:** {datos['Marca']}")
st.write(f"**Capacidad:** {datos['Litros']} litros")
st.write(f"**Sistema:** {datos['Sistema']}")
st.write(f"**Tasa:** {datos['Tasa']} %")
st.write(f"**Precio:** ${datos['Precio']}")