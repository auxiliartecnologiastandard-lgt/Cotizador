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

# Adaptamos los números a texto ( Marca )
if datos['Marca'] == 1:
    datos['Marca'] = "Kalley"
elif datos['Marca'] == 2:
    datos['Marca'] = "Indurama"
elif datos['Marca'] == 3:
    datos['Marca'] = "Challenger"
elif datos['Marca'] == 4:
    datos['Marca'] = "Midea"
elif datos['Marca'] == 4.1:
    datos['Marca'] = "Hisense"
elif datos['Marca'] == 5:
    datos['Marca'] = "Mabe"
elif datos['Marca'] == 6:
    datos['Marca'] = "Haceb"
elif datos['Marca'] == 6.1:
    datos['Marca'] = "Abba"
elif datos['Marca'] == 7:
    datos['Marca'] = "Whirlpool"
elif datos['Marca'] == 8:
    datos['Marca'] = "Electrolux"
elif datos['Marca'] == 9:
    datos['Marca'] = "Samsung"
elif datos['Marca'] == 10:
    datos['Marca'] = "LG"
elif datos['Marca'] == 11:
    datos['Marca'] = "Bosch"
elif datos['Marca'] == 12:
    datos['Marca'] = "KitchenAid"
elif datos['Marca'] == 13:
    datos['Marca'] = "Frigidaire"
elif datos['Marca'] == 13.1:
    datos['Marca'] = "GE Profile"
elif datos['Marca'] == 14:
    datos['Marca'] = "Sub-Zero"
elif datos['Marca'] == 14.1:
    datos['Marca'] = "Monogram"
elif datos['Marca'] == 14.01:
    datos['Marca'] = "Liebherr"

# Adaptamos los números a texto ( Litros )
if datos['Litros'] == 1:
    datos['Litros'] = "40 y 120 litros"
elif datos['Litros'] == 2:
    datos['Litros'] = "121 y 250 litros"
elif datos['Litros'] == 3:
    datos['Litros'] = "251 y 450 litros"
elif datos['Litros'] == 4:
    datos['Litros'] = "450 y 800 litros"

# Adaptamos los números a texto ( Sistema de enfriamiento )
if datos['Sistema'] == 5:
    datos['Sistema'] = "Auto frost"
else:
    datos['Sistema'] = "No frost"
    
st.write(f"Este contrato se basa en la compraventa de una {datos["Origen"]}, de la marca {datos['Marca']}, con una capacidad entre {datos['Litros']}, y sistema {datos['Sistema']}, Al precio de: {datos['Precio']}  pesos con una tasa del {datos['Tasa']}%")
