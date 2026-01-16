import streamlit as st
import pandas as pd
import joblib
import numpy as np

# ELIMINAR BARRA LATERAL
st.set_page_config(
    page_title="Cotizador Coandes",
    initial_sidebar_state="collapsed"
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
    # Busca el modelo dentro de la carpeta
    ruta_modelo = "Cotizador_Coandes-copia/Computadores/modelo_pcs.pkl"
    modelo = joblib.load(ruta_modelo)

except:
    st.error("⚠️ No se encontró el modelo. Ejecuta 'py Computadores/entrenar.py' primero.")

# Botón volver
if st.button("⬅  Volver al Menú Principal"):
    st.switch_page("Lobby.py")

st.title("💻 Cotizador de Computadores")

# --- LÓGICA DE SINCRONIZACIÓN ---
def sync_slider_to_num(key_slider, key_num):
    st.session_state[key_num] = st.session_state[key_slider]

def sync_num_to_slider(key_num, key_slider):
    st.session_state[key_slider] = st.session_state[key_num]

# --- INTERFAZ ---

# 1. Marca
st.markdown("### 1. Marca del equipo")
marca_opciones = {
    "WINDOWS": 1,
    "Koorui": 2,
    "Acer": 3,
    "Hewlettpacka": 4,
    "VICTUS": 5,
    "Asus": 6,
    "SONY": 7,
    "Samsung": 8,
    "Dell": 9,
    "LENOVO": 10,
    "Apple": 11,
    
}
sel_marca = st.selectbox("Seleccione la marca del equipo:", list(marca_opciones.keys()), index=1)
valor_marca = marca_opciones[sel_marca]

# 2. Memoria RAM (Mapeada por potencia)
st.markdown("### 2. Memoria RAM")
ram_opciones = {
    "2 GB (Cantidad minima)": 2,
    "4 GB (Uso básico)": 4,
    "5 / 6 GB (Uso de hogar)": 6,
    "8 GB (Estándar/Oficina)": 7,
    "12 GB (Multitarea fluida)": 12,
    "16 GB (Diseño/Gaming)": 16,
    "32 GB (Profesional/Streaming)": 32,
    "64 GB (Servidores/Rendimiento Extremo)": 64,
}
sel_ram = st.selectbox("Seleccione capacidad de RAM:", list(ram_opciones.keys()), index=1)
valor_ram = ram_opciones[sel_ram]

# 3. Almacenamiento
st.markdown("### 3. Capacidad de Almacenamiento (GB)")
disco_dict = {
    "128 GB": 128,
    "256 GB": 256,
    "512 GB": 512,
    "1 TB": 1024,
    "2 TB": 2048,
    "Otro (Escribir valor... )": "OTRO"
}

seleccion = st.selectbox("Seleccione capacidad o elija 'Otro':", list(disco_dict.keys()), index=1)
    # Si elige 'Otro', mostramos un campo de entrada numérica
if disco_dict[seleccion] == "OTRO":
    
    Valor_Usuario = st.number_input("Escriba el valor exacto en GB:", min_value=1, max_value=10000)
    Valor_Memoria_Real = Valor_Usuario
    # Ancla de realidad para ajustar el precio
    if Valor_Usuario  >= 1 and Valor_Usuario  < 256:
            valor_disco_final = 128
    elif Valor_Usuario  >= 256 and Valor_Usuario  < 500:
            valor_disco_final = 256
    elif Valor_Usuario  >= 500 and Valor_Usuario  < 512:
            valor_disco_final = 512
    elif Valor_Usuario > 512:
            valor_disco_final = Valor_Usuario
else:
    valor_disco_final = disco_dict[seleccion]
    Valor_Memoria_Real = valor_disco_final

# 4. Procesador
st.markdown("### 4. Procesador")
proc_opciones = {
    "Celeron": 5, 
    "Pentium": 5.000001,
    "AMD": 5.0000001,
    "Athlon": 5.00000001,
    "Core i3 / Ryzen 3": 15, 
    "Core i5 / Ryzen 5": 30, 
    "Core i7 / Ryzen 7": 70, 
    "Core i9 / Ryzen 9": 120,
}
seleccion = st.selectbox("Seleccione el Modelo:", list(proc_opciones.keys()), index=1)
valor_procesador = proc_opciones[seleccion]

# 5. Gráfica
st.markdown("### 5. Potencia Gráfica")
tiene_grafica = st.checkbox("¿Tiene Tarjeta de Video Dedicada? (Nvidia/Radeon)", value=False)
grafica = 1 if tiene_grafica else 0

st.divider()

# 6. Tasa para contrato
if st.toggle("OPCIONAL: Agregar tasa"):
    valor_tasa = st.number_input("Escriba la tasa:", min_value=1, max_value=100)
else:
    valor_tasa = 0

st.divider()

col1, col2, = st.columns(2)

with col1:
    # --- CÁLCULO FINAL ---
    if st.button("🚀 CALCULAR VALOR"):
        
        # 1. Ajuste de peso para que el disco no infle el precio en equipos básicos
        valor_disco_ia = valor_disco_final * 0.01 if valor_procesador <= 16 else valor_disco_final
        
        # 2. Predicción
        entrada = np.array([[valor_marca, valor_ram, valor_disco_ia, valor_procesador, grafica]])
        precio_base = modelo.predict(entrada)[0]

        # 3. Filtros de Realidad (Anclas de precio de los procesadores basicos)
        if valor_procesador <= 5: 
            precio_base = np.clip(precio_base * 0.25, 100000, 150000)
        # 3.1 Ancla para los procesadores I3 
        elif valor_procesador <= 15:
            if valor_ram >= 7:
                precio_base = np.clip(precio_base * 1.05, 300000, 480000)
            elif valor_ram >= 4 and valor_disco_ia >= 900:
                precio_base = np.clip(precio_base * 0.90, 260000, 420000)
            elif valor_ram >= 4 and precio_base > 460000:
                precio_base = np.clip(precio_base * 1.0, 300000, 620000)
            elif valor_marca == 6 and valor_ram >= 4 and valor_disco_ia == 1.28:
                precio_base == 600000
            else:
                precio_base = np.clip(precio_base * 0.35, 120000, 210000)
        # 3.2 Ancla de los procesadores I5
        elif valor_procesador <= 30:
            precio_base = precio_base * 0.88
            precio_base = precio_base * 1.10
        # 3.3 Ancla de los procesadores I5
        elif valor_procesador <= 70:
            precio_base = precio_base * 1.055

        # 4. Redondear precios
        precio_base_redondo = round(precio_base / 10000) * 10000
        precio_venta_redondo = round((precio_base_redondo * 1.4) / 10000) * 10000

        # 5. Resultados
        v_venta = f"${precio_venta_redondo:,.0f}".replace(",", ".")
        v_compra = f"${precio_base_redondo:,.0f}".replace(",", ".")
        
        #st.success(f"### Precio Sugerido Venta: {v_venta}")
        st.info(f"### Oferta de Compraventa: {v_compra}")

with col2:
    if st.button("📄 Crear contrato"):
        st.session_state["precio_calculado"] = True
        if valor_tasa == 0:
            st.warning("Porfavor agregue una tasa")
        else:
        
            st.markdown("### Antes de crear tu contrato porfavor llena danos la información correcta")
            
            Nombre_Usuario = st.text_input("Escribe tu nombre:")
            Cedula_Usuario = st.number_input("Escribe la cedula del cliente:", min_value=1)
            Meses = st.number_input("Escribe el plazo que tiene el usuario para pagar ( Meses ):", min_value=1)
            SEDES = {
                "La 14 - Pereira": 1,
                "La 18 - Pereira": 2,
                "La 19 - Pereira": 3,
                "Cuba - Pereira": 4,
                "La 29 - Pereira": 5,
                "Crucero - Doquebradas": 6,
                "Naranjos - Dosquebradas": 7,
                "Japón - Dosquebradas": 8,
                "Sol brilla - Tuluá": 9,
                "Super Standard - Tuluá": 10,
                "Armenia": 11
            }
            sel_SEDE = st.selectbox("Seleccione la sede en la que se encuentra:", list(SEDES.keys()), index=1)
            SEDE_V = SEDES[sel_SEDE]



            # 1. Ajuste de peso para que el disco no infle el precio en equipos básicos
            valor_disco_ia = valor_disco_final * 0.01 if valor_procesador <= 16 else valor_disco_final
            
            # 2. Predicción
            entrada = np.array([[valor_marca, valor_ram, valor_disco_ia, valor_procesador, grafica]])
            precio_base = modelo.predict(entrada)[0]

            # 3. Filtros de Realidad (Anclas de precio de los procesadores basicos)
            if valor_procesador <= 5: 
                precio_base = np.clip(precio_base * 0.25, 100000, 150000)
            # 3.1 Ancla para los procesadores I3 
            elif valor_procesador <= 15:
                if valor_ram >= 7:
                    precio_base = np.clip(precio_base * 1.05, 300000, 480000)
                elif valor_ram >= 4 and valor_disco_ia >= 900:
                    precio_base = np.clip(precio_base * 0.90, 260000, 420000)
                elif valor_ram >= 4 and precio_base > 460000:
                    precio_base = np.clip(precio_base * 1.0, 300000, 620000)
                elif valor_marca == 6 and valor_ram >= 4 and valor_disco_ia == 1.28:
                    precio_base == 600000
                else:
                    precio_base = np.clip(precio_base * 0.35, 120000, 210000)
            # 3.2 Ancla de los procesadores I5
            elif valor_procesador <= 30:
                precio_base = precio_base * 0.88
                precio_base = precio_base * 1.10
            # 3.3 Ancla de los procesadores I5
            elif valor_procesador <= 70:
                precio_base = precio_base * 1.055

            # 4. Redondear precios
            precio_base_redondo = round(precio_base / 10000) * 10000
            precio_venta_redondo = round((precio_base_redondo * 1.4) / 10000) * 10000

            # 3. Formato
            st.session_state["v_compra"] = precio_base_redondo
            st.session_state["v_venta"] = f"${precio_venta_redondo:,.0f}".replace(",", ".")
            # Conversión explícita a números
            Dinero = st.session_state["v_compra"] + (st.session_state["v_compra"] * (valor_tasa / 100) * Meses)
            Dinero = f"${Dinero:,.0f}".replace(",", ".")
            #PARA CONTRATOS
            st.session_state["valor_marca"] = valor_marca
            st.session_state["valor_ram"] = valor_ram
            st.session_state["Valor_Memoria_Real"] = Valor_Memoria_Real
            st.session_state["valor_procesador"] = valor_procesador
            st.session_state["grafica"] = grafica
            st.session_state["valor_tasa"] = valor_tasa
            st.session_state["Nombre_Usuario"] = Nombre_Usuario
            st.session_state["Cedula_Usuario"] = Cedula_Usuario
            st.session_state["Meses"] = Meses
            st.session_state["SEDE_V"] = SEDE_V
            st.session_state["Dinero"] = Dinero

            if "v_compra" in st.session_state:
                st.session_state["datos_cotizador"] = {
                    "Origen": "Computador",
                    "Marca": st.session_state["valor_marca"],
                    "RAM": st.session_state["valor_ram"],
                    "Disco": st.session_state["Valor_Memoria_Real"],
                    "Procesador": st.session_state["valor_procesador"],
                    "Grafica": st.session_state["grafica"],
                    "Precio": st.session_state["v_compra"],
                    "Tasa": st.session_state["valor_tasa"],
                    "Nombre": st.session_state["Nombre_Usuario"],
                    "Cédula": st.session_state["Cedula_Usuario"],
                    "Meses": st.session_state["Meses"],
                    "Sede": st.session_state["SEDE_V"],
                    "Dinero": st.session_state["Dinero"]
                    }
                            
            else:
                st.warning("Primero calcula el precio en el cotizador")
            st.button("Hola mucho gusto")
            st.switch_page("pages/Contrato_Standard.py")