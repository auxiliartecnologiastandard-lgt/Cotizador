import streamlit as st
import pandas as pd
import joblib
import numpy as np
from ia_logica import analizar_con_ia
from PIL import Image

# 1. Configuración de la pagina
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

# 1.1 Buscar el modelo IA
try:
    # Busca el modelo dentro de la carpeta de la copia
    ruta_modelo = "Cotizador_Coandes-copia/Computadores/modelo_pcs.pkl"
    modelo = joblib.load(ruta_modelo)

except:
    st.error("⚠️ No se encontró el modelo. Ejecuta 'py Computadores/entrenar.py' primero.")

# 1.2 Boton volver y titulo
if st.button("Volver al Menú Principal"):
    st.switch_page("Lobby.py")

st.title("💻 Cotizador Pro Coandes")
st.markdown("---")

# 1.3 Logica de gemini
def sync_slider_to_num(key_slider, key_num):
    st.session_state[key_num] = st.session_state[key_slider]

def sync_num_to_slider(key_num, key_slider):
    st.session_state[key_slider] = st.session_state[key_num]

# --- INTERFAZ ---

# 2. MEMORIA RAM (Mapeada por potencia)
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

# 3. ALMACENAMIENTO
st.markdown("### 2. Capacidad de Almacenamiento (GB)")
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
    valor_disco_final = st.number_input("Escriba el valor exacto en GB:", min_value=1, max_value=10000)

else:
    valor_disco_final = disco_dict[seleccion]

# 4. PROCESADOR (Ahora mapeado del 1 al 5 según tu lista)
st.markdown("### 3. Procesador")
proc_opciones = {
    "Básico (Celeron/Pentium/AMD A-Series/Athlon)": 5, 
    "Core i3 / Ryzen 3": 15, 
    "Core i5 / Ryzen 5": 30, 
    "Core i7 / Ryzen 7": 70, 
    "Core i9 / Ryzen 9": 120,
}
seleccion = st.selectbox("Seleccione el Modelo:", list(proc_opciones.keys()), index=1)
valor_procesador = proc_opciones[seleccion]

# 5. GRÁFICA
st.markdown("### 4. Potencia Gráfica")
tiene_grafica = st.checkbox("¿Tiene Tarjeta de Video Dedicada? (Nvidia/Radeon)", value=False)
grafica = 1 if tiene_grafica else 0

st.divider()

# 6. Verificador de daños con IA
if st.toggle("🔍 Verificar estado con IA"):
    
    # --- INICIALIZACIÓN DEL BAÚL ---
    if "foto_1" not in st.session_state: st.session_state.foto_1 = None
    if "foto_2" not in st.session_state: st.session_state.foto_2 = None
    if "foto_3" not in st.session_state: st.session_state.foto_3 = None

    if "datos_peritaje" not in st.session_state: 
        st.session_state.datos_peritaje = {"porcentaje": 0, "motivo": "", "listo": False}

    # --- INTERFAZ FOTOS ---
    c1, c2, c3 = st.columns(3)
    
    with c1:
        f1 = st.camera_input("foto_1", key="c1")
        if f1: st.session_state.foto_1 = f1
    with c2:
        f2 = st.camera_input("foto_2", key="c2")
        if f2: st.session_state.foto_2 = f2
    with c3:
        f3 = st.camera_input("foto_3", key="c3")
        if f3: st.session_state.foto_3 = f3

    # --- CODIGO CUANDO SE TOMARON LAS FOTOS ---
    fotos_tomadas = [st.session_state.foto_1, st.session_state.foto_2, st.session_state.foto_3]
    conteo = sum(1 for f in fotos_tomadas if f is not None)
    
    if conteo > 0:
        st.write(f"✅ Fotos en memoria: {conteo} de 3")
    if conteo == 3:
        st.success("📸 ¡Listas las 3 fotos para procesar!")
        
# --- CÁLCULO FINAL ---
if st.button("🚀 CALCULAR VALOR"):
    
    # Aseguramos que la variable exista dentro del botón también
    if "datos_peritaje" not in st.session_state:
        st.session_state.datos_peritaje = {"porcentaje": 0, "motivo": "", "listo": False}
        
    st.write("DEBUG: Iniciando cálculos...") 

    # --- LÓGICA DE LA IA ---
    if st.session_state.foto_1 and st.session_state.foto_2 and st.session_state.foto_3:
        try:
            fotos_para_ia = [
                Image.open(st.session_state.foto_1),
                Image.open(st.session_state.foto_2),
                Image.open(st.session_state.foto_3)
            ]
            
            with st.spinner("Analizando fotos..."):
                analisis = analizar_con_ia(fotos_para_ia, 1, "Computadora")
            
            if analisis and analisis["exito"]:
                st.session_state.datos_peritaje = {
                    "porcentaje": analisis["porcentaje"],
                    "motivo": analisis["motivo"],
                    "listo": True
                }
        except Exception as e:
            st.error(f"Error procesando fotos: {e}")

    # --- LÓGICA DE PRECIO EXISTENTE (No tocar) ---
    valor_disco_ia = valor_disco_final * 0.01 if valor_procesador <= 15 else valor_disco_final
    entrada = np.array([[valor_ram, valor_disco_ia, valor_procesador, grafica]])
    precio_base = modelo.predict(entrada)[0]
    
    # Filtros de Realidad
    if valor_procesador == 5: precio_base = min(precio_base, 100000)
    elif valor_procesador == 15: precio_base = min(precio_base, 150000)
    elif valor_procesador == 30 and grafica == 0: precio_base = min(precio_base, 500000)

    precio_base_redondo = round(precio_base / 10000) * 10000
    precio_venta_redondo = round((precio_base_redondo * 1.4) / 10000) * 10000

    # --- NUEVO: CÁLCULO DE DESCUENTO POR IA ---
    dinero_reducido = 0
    # Usamos .get() por seguridad extra
    peritaje = st.session_state.get("datos_peritaje", {"listo": False})
    
    if peritaje["listo"]:
        porcentaje = peritaje["porcentaje"]
        dinero_reducido = precio_base_redondo * porcentaje
        precio_base_redondo = precio_base_redondo - dinero_reducido

    # --- RESULTADOS ---
    v_venta = f"${precio_venta_redondo:,.0f}".replace(",", ".")
    v_compra = f"${precio_base_redondo:,.0f}".replace(",", ".")
    
    # --- MENSAJE DE LA IA AL FINAL ---
    if peritaje["listo"]:
        motivo = peritaje["motivo"]
        if dinero_reducido > 0:
            (f"⚠️ Por los daños detectados ({motivo}), se redujeron ${dinero_reducido:,.0f} pesos.")
            st.success(f"### Precio sugerido venta: {v_venta}")
            st.info(f"### Oferta de Compra Coandes: {v_compra}")
        
        else:
            st.success(f"### Precio sugerido venta: {v_venta}")
            st.info(f"### Oferta de Compra Coandes: {v_compra}")
            ("✅ No se detectaron daños físicos, el precio se mantiene.")