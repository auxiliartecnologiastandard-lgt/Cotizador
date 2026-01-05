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

# Busca el botón de volver en tu app.py y ajusta la ruta así:
if st.button("⬅  Volver al Menú Principal"):
    st.switch_page("Lobby.py")

st.title("🧊 Cotizador de Neveras")
st.markdown("---")

# --- LÓGICA DE SINCRONIZACIÓN ---
def sync_slider_to_num(key_slider, key_num):
    st.session_state[key_num] = st.session_state[key_slider]

def sync_num_to_slider(key_num, key_slider):
    st.session_state[key_slider] = st.session_state[key_num]

# --- INTERFAZ ---

# 1. MEMORIA RAM (Mapeada por potencia)
st.markdown("### 1. Memoria RAM")
ram_opciones = {
    "2 GB (Cantidad minima)": 2,
    "4 GB (Uso básico)": 4,
    "6 GB (Uso de hogar)": 6,
    "8 GB (Estándar/Oficina)": 8,
    "12 GB (Multitarea fluida)": 12,
    "16 GB (Diseño/Gaming)": 16,
    "32 GB (Profesional/Streaming)": 32,
    "64 GB (Servidores/Rendimiento Extremo)": 64,
}
sel_ram = st.selectbox("Seleccione capacidad de RAM:", list(ram_opciones.keys()), index=1)
valor_ram = ram_opciones[sel_ram]

# 2. ALMACENAMIENTO
st.markdown("### 2. Rangos de Capacidad (Litros Brutos)")
disco_dict = {
    "Mini / Compactas 40L-120L": 1,
    "Pequeñas 120L-250L": 2,
    "Medianas 250L-450L": 3,
    "Grandes 450L-800L+": 4,
    "Otro (Escribir valor... )": "OTRO"
}

seleccion = st.selectbox("Seleccione el rango de capacidad o elija 'Otro':", list(disco_dict.keys()), index=1)
    # Si elige 'Otro', mostramos un campo de entrada numérica
if disco_dict[seleccion] == "OTRO":
    valor_disco_final = st.number_input("Escriba el valor exacto en L:", min_value=1, max_value=1000000000000000000000000)

else:
    valor_disco_final = disco_dict[seleccion]

# 3. PROCESADOR (Ahora mapeado del 1 al 5 según tu lista)
st.markdown("### 3. Sistema de Enfriamiento")
proc_opciones = {
    "Auto frost": 5, 
    "No frost": 10,
}
seleccion = st.selectbox("Seleccione el Sistema de Enfriamientoelo:", list(proc_opciones.keys()), index=1)
valor_procesador = proc_opciones[seleccion]

# 4. GRÁFICA
st.markdown("### 4. Potencia Gráfica")
tiene_grafica = st.checkbox("¿Tiene Tarjeta de Video Dedicada? (Nvidia/Radeon)", value=False)
grafica = 1 if tiene_grafica else 0

st.divider()

# --- CÁLCULO FINAL ---
if st.button("🚀 CALCULAR VALOR"):
    # 1. Ajuste de peso para que el disco no infle el precio en equipos básicos
    valor_disco_ia = valor_disco_final * 0.01 if valor_procesador <= 15 else valor_disco_final
    
    # 2. Predicción
    entrada = np.array([[valor_ram, valor_disco_ia, valor_procesador, grafica]])
    precio_base = modelo.predict(entrada)[0]
    
    # 3. Filtros de Realidad (Anclas de precio)
    if valor_procesador == 5: 
        precio_base = min(precio_base, 100000)
    elif valor_procesador == 15: 
        precio_base = min(precio_base, 150000)
    elif valor_procesador == 30 and grafica == 0:
        precio_base = min(precio_base, 500000)

    # 4. Redondear precios
    precio_base_redondo = round(precio_base / 10000) * 10000
    precio_venta_redondo = round((precio_base_redondo * 1.4) / 10000) * 10000

    # 5. Resultados
    v_venta = f"${precio_venta_redondo:,.0f}".replace(",", ".")
    v_compra = f"${precio_base_redondo:,.0f}".replace(",", ".")
    
    st.success(f"### Precio Sugerido Venta: {v_venta}")
    st.info(f"### Oferta de Compra Coandes: {v_compra}")