import streamlit as st

st.markdown(
    """
    <style>
        /* Elimina el botón > de la esquina superior izquierda */
        [data-testid="collapsedControl"] {
            display: none !important;
        }

        /* Elimina la barra lateral por completo */
        [data-testid="stSidebar"] {
            display: none !important;
        }
        
        /* Elimina el encabezado superior para que no quede espacio vacío */
        header {
            visibility: hidden !important;
            height: 0 !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.set_page_config(page_title="Contrato de Compraventa")

st.title("📄 Contrato")

datos = st.session_state.get("datos_cotizador")

if not datos:
    st.warning("No hay datos del cotizador. Regresa y calcula primero.")
    st.stop()

# Mostrar solo datos de nevera
if datos["Origen"] != "nevera":
    st.error("Este contrato no corresponde a una nevera.")
    st.stop()
if datos['Marca'] == 1:
    datos['Marca'] = "Kalley"

st.write(f"Este contrato se basa en la compra de una {datos["Origen"]}, de la marca {datos['Marca']}, con una capacidad entre {datos['Litros']}, y sistema {datos['Sistema']}, Al precio de: {datos['Precio']}  pesos con una tasa del {datos['Tasa']}%")
