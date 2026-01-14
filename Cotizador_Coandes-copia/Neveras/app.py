import streamlit as st
import pandas as pd
import joblib
import numpy as np

# ELIMINAR BARRA LATERAL
st.set_page_config(
    page_title="Cotizador Coandes",
    initial_sidebar_state="collapsed" # Esto la cierra al cargar
    
)

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

# Cargar el modelo
try:
    # Busca el modelo dentro de la carpeta de la copia
    ruta_modelo = "Cotizador_Coandes-copia/Neveras/modelo_nev.pkl"
    modelo = joblib.load(ruta_modelo)

except:
    st.error("⚠️ No se encontró el modelo. Ejecuta 'py Neveras/entrenar.py' primero.")

def main():
    # Busca el botón de volver en tu app.py y ajusta la ruta así:
    if st.button("⬅  Volver al Menú Principal", key="btn_volver_menu"):
        st.switch_page("Lobby.py")

    st.title("🧊 Cotizador de Neveras")

    # --- LÓGICA DE SINCRONIZACIÓN ---
    def sync_slider_to_num(key_slider, key_num):
        st.session_state[key_num] = st.session_state[key_slider]

    def sync_num_to_slider(key_num, key_slider):
        st.session_state[key_slider] = st.session_state[key_num]

    # --- INTERFAZ ---

    # 1. Marca de la nevera (Mapeada por potencia)
    st.markdown("### 1. Marca")
    Marca_opciones = {
        "Kalley": 1,
        "Indurama": 2,
        "Challenger": 3,
        "Midea / Hisense": 4,
        "Mabe": 5,
        "Haceb": 6,
        "Abba": 6,
        "Whirlpool": 7,
        "Electrolux": 8,
        "Samsung": 9,
        "LG": 10,
        "Bosch": 11,
        "KitchenAid": 12,
        "Frigidaire / GE Profile": 13,
        "Sub-Zero / Monogram / Liebherr": 14,
    }
    sel_marca = st.selectbox("Seleccione la marca:", list(Marca_opciones.keys()), index=1)
    valor_marca = Marca_opciones[sel_marca]

    # 2. Rango de capacidad
    st.markdown("### 2. Rangos de Capacidad (Litros Brutos)")
    Litro_dict = {
        "Mini / Compactas 40L-120L": 1,
        "Pequeñas 120L-250L": 2,
        "Medianas 251L-450L": 3,
        "Grandes 450L-800L+": 4,
        "Otro (Escribir valor... )": "OTRO"
    }

    seleccion = st.selectbox("Seleccione el rango de capacidad o elija 'Otro':", list(Litro_dict.keys()), index=1)
        # Si elige 'Otro', mostramos un campo de entrada numérica
    if Litro_dict[seleccion] == "OTRO":
        valor_litro_final = st.number_input("Escriba el valor exacto en L:", min_value=0, max_value=10000)

    else:
        valor_litro_final = Litro_dict[seleccion]

    # 3. Sistema de enfriamiento
    st.markdown("### 3. Sistema de Enfriamiento")
    SE_opciones = {
        "Auto frost": 5, 
        "No frost": 10,
    }
    seleccion = st.selectbox("Seleccione el Sistema de Enfriamientoelo:", list(SE_opciones.keys()), index=1)
    valor_Sistema_de_enfriamiento = SE_opciones[seleccion]

    # 4. Tasa para contrato
    if st.toggle("OPCIONAL: Agregar tasa"):
        valor_tasa = st.number_input("Escriba el valor exacto en L:", min_value=1, max_value=100)

    st.divider()

    # --- CÁLCULO FINAL ---
    if st.button("🗿 CALCULAR VALOR"):


        # 1. Predicción
        entrada = np.array([[valor_marca, valor_litro_final, valor_Sistema_de_enfriamiento]])
        precio_base = modelo.predict(entrada)[0]

        # 2. Redondear precios
        precio_base_redondo = round(precio_base / 10000) * 10000
        precio_venta_redondo = round((precio_base_redondo * 1.4) / 10000) * 10000

        # 3. Formato
        st.session_state["v_compra"] = f"${precio_base_redondo:,.0f}".replace(",", ".")
        st.session_state["v_venta"] = f"${precio_venta_redondo:,.0f}".replace(",", ".")
        #PARA CONTRATOS
        st.session_state["valor_marca"] = valor_marca
        st.session_state["valor_litro_final"] = valor_litro_final
        st.session_state["valor_Sistema_de_enfriamiento"] = valor_Sistema_de_enfriamiento
        st.session_state["valor_tasa"] = valor_tasa

        #RESULTADO
        st.info(f"### Oferta de Compraventa: {st.session_state['v_compra']}")

        if st.button("Crear contrato"):
            if "v_compra" in st.session_state:
                st.session_state["datos_cotizador"] = {
                    "Origen": "nevera",
                    "Marca": st.session_state["valor_marca"],
                    "Litros": st.session_state["valor_litro_final"],
                    "Sistema": st.session_state["valor_Sistema_de_enfriamiento"],
                    "Precio": st.session_state["v_compra"],
                    "Tasa": st.session_state["valor_tasa"]
                }
                st.success("Contrato generado correctamente!")

                # Esto funciona si el nombre de la página en Streamlit es 'Contrato_Standard'
                st.switch_page("Contrato_Standard")  # NO usar "pages/Contrato_Standard.py"
                
            else:
                st.warning("Primero calcula el precio en el cotizador")
main()
