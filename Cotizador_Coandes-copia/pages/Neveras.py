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
        "Midea": 4,
        "Hisense": 4.1,
        "Mabe": 5,
        "Haceb": 6,
        "Abba": 6.1,
        "Whirlpool": 7,
        "Electrolux": 8,
        "Samsung": 9,
        "LG": 10,
        "Bosch": 11,
        "KitchenAid": 12,
        "Frigidaire": 13,
        "GE Profile": 13.1,
        "Sub-Zero": 14,
        "Monogram": 14.1,
        "Liebherr": 14.01
    }
    sel_marca = st.selectbox("Seleccione la marca:", list(Marca_opciones.keys()), index=1)
    valor_marca = Marca_opciones[sel_marca]

    # 2. Rango de capacidad
    st.markdown("### 2. Rangos de Capacidad (Litros Brutos)")
    Litro_dict = {
        "Mini / Compactas 40L-120L": 1,
        "Pequeñas 120L-250L": 2,
        "Medianas 250L-450L": 3,
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

    st.divider()

    # 6. Tasa para contrato
    if st.toggle("OPCIONAL: Crear contrato"):
        st.markdown("### Antes de crear tu contrato porfavor llena los campos con la información correcta")
        Nombre_Usuario = st.text_input("Escribe el nombre completo del cliente:")
        Cedula_Usuario = st.number_input("Escribe la cedula del cliente:", min_value=1)
        valor_tasa = st.number_input("Escribe la tasa:", min_value=1, max_value=100)     
        Meses = st.number_input("Escribe el plazo que tiene el usuario para pagar ( Meses ):", min_value=1)
        SEDES = {
            "La 14 - Pereira": 1,
            "La 18 - Pereira": 2,
            "La 19 - Pereira": 3,
            "Cuba - Pereira": 4,
            "La 29 - Pereira": 5,
            "Crucero - Dosquebradas": 6,
            "Naranjos - Dosquebradas": 7,
            "Japón - Dosquebradas": 8,
            "Sol brilla - Tuluá": 9,
            "Super Standard - Tuluá": 10,
            "Armenia": 11
        }
        sel_SEDE = st.selectbox("Seleccione la sede en la que se encuentra:", list(SEDES.keys()), index=1)
        SEDE_V = SEDES[sel_SEDE]

    else:
        valor_tasa = 0

    st.divider()

    col1, col2, = st.columns(2)

    with col1:
        # --- CÁLCULO FINAL ---
        if st.button("🗿 CALCULAR VALOR"):

            # 1. Predicción
            entrada = np.array([[valor_marca, valor_litro_final, valor_Sistema_de_enfriamiento]])
            precio_base = modelo.predict(entrada)[0]

            # 2. Redondear precios
            precio_base_redondo = round(precio_base / 10000) * 10000
            precio_venta_redondo = round((precio_base_redondo * 1.4) / 10000) * 10000

            # 3. Formato
            v_compra = f"${precio_base_redondo:,.0f}".replace(",", ".")
            v_venta = f"${precio_venta_redondo:,.0f}".replace(",", ".")

            st.info(f"### Oferta de Compraventa: {v_compra}")


    with col2:
        if st.button("📄 Crear contrato"):
            st.session_state["precio_calculado"] = True
            if valor_tasa == 0:
                st.warning("Porfavor agrega la información necesaria")
            else:
                # 1. Predicción
                entrada = np.array([[valor_marca, valor_litro_final, valor_Sistema_de_enfriamiento]])
                precio_base = modelo.predict(entrada)[0]

                # 2. Redondear precios
                precio_base_redondo = round(precio_base / 10000) * 10000
                precio_venta_redondo = round((precio_base_redondo * 1.4) / 10000) * 10000

                # 3. Formato
                st.session_state["v_compra"] = precio_base_redondo
                st.session_state["v_venta"] = f"${precio_venta_redondo:,.0f}".replace(",", ".")
                # Conversión explícita a números
                Dinero = st.session_state["v_compra"] + (st.session_state["v_compra"] * (valor_tasa / 100) * Meses)
                Dinero = f"${Dinero:,.0f}".replace(",", ".")
                Direcciones = 0
                
                #PARA CONTRATOS
                st.session_state["valor_marca"] = valor_marca
                st.session_state["valor_litro_final"] = valor_litro_final
                st.session_state["valor_Sistema_de_enfriamiento"] = valor_Sistema_de_enfriamiento
                st.session_state["v_compra"] = f"${precio_base_redondo:,.0f}".replace(",", ".")
                st.session_state["valor_tasa"] = valor_tasa
                st.session_state["Nombre_Usuario"] = Nombre_Usuario
                st.session_state["Cedula_Usuario"] = Cedula_Usuario
                st.session_state["Meses"] = Meses
                st.session_state["SEDE_V"] = SEDE_V
                st.session_state["Dinero"] = Dinero
                st.session_state["Direcciones"] = Direcciones


                if "v_compra" in st.session_state:
                    st.session_state["datos_cotizador"] = {
                        "Origen": "Nevera",
                        "Marca": st.session_state["valor_marca"],
                        "Litros": st.session_state["valor_litro_final"],
                        "Sistema": st.session_state["valor_Sistema_de_enfriamiento"],
                        "Precio": st.session_state["v_compra"],
                        "Tasa": st.session_state["valor_tasa"],
                        "Nombre": st.session_state["Nombre_Usuario"],
                        "Cedula": st.session_state["Cedula_Usuario"],
                        "Meses": st.session_state["Meses"],
                        "Sede": st.session_state["SEDE_V"],
                        "Dinero": st.session_state["Dinero"],
                        "Direcciones": st.session_state["Direcciones"]
                        }
                            
                else:
                    st.warning("Primero calcula el precio en el cotizador")
                

                st.switch_page("pages/Contrato_Standard.py")
main()