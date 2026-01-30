import streamlit as st
import os

# 0. Ubicar la imagen del logo
ruta_base = os.path.dirname(__file__)
ruta_logo = os.path.join(ruta_base, "Standard_logo.png")

# 1. Configuración de la pagina
st.set_page_config(page_title="Lobby", initial_sidebar_state="collapsed", layout="wide")
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
# Botón volver
if st.button("⬅  Volver al Menú Principal"):
    st.switch_page("Lobby.py")

base_datos = [
    # Intel compatibles
    "Intel Atom X7000 Series",
    "Intel Celeron 3000 Series",
    "Intel Celeron 4000 Series",
    "Intel Celeron 5000 Series",
    "Intel Celeron 6000 Series",
    "Intel Celeron 7000 Series",
    "Intel Core i3 (8th-14th Gen)",
    "Intel Core i5 (8th-14th Gen)",
    "Intel Core i7 (8th-14th Gen)",
    "Intel Core i9 (8th-14th Gen)",
    "Intel Core Ultra Series",
    "Intel Pentium Gold",
    "Intel Pentium Silver",
    "Intel Xeon Series",

    # AMD compatibles
    "AMD 3015e",
    "AMD 3020e",
    "AMD Athlon 3000 Series",
    "AMD Athlon 7120 Series",
    "AMD Athlon 7220 Series",
    "AMD Ryzen 3 Series",
    "AMD Ryzen 5 Series",
    "AMD Ryzen 7 Series",
    "AMD Ryzen Embedded R2000",
    "AMD Ryzen Z1",
    "AMD Ryzen Z1 Extreme",
    "AMD EPYC Series"
]

check_bateria = st.checkbox("Estado de la bateria")

st.divider()

if not check_bateria:
    with st.expander("📝 Como sacar el estado de la bateria"):
        st.write('1. Presionar " Windows + X "y selecciona Windows powershell')
        st.write('2. Copia ➡ " powercfg /batteryreport ", pegalo en powershell y despues presiona Enter')
        st.write('3. Copia el link que te ofrecio powershell. Ejemplo: C:\\Users\\TuUsuario\\Battery-report.html.')
        st.write('4. Pega ese link que copiaste en cualquier navegador ( Microsoft edge, Chrome, Firefox...)')
        st.write('5. Busca un apartado que diga " Installed batteries " ( Esta al principio de la pagina )')
        st.write('6. Busca en installed bateries secciones que digan " DESIGN CAPACITY " y " FULL CHARGE CAPACITY " ')
        st.write('7. Divide el numero alfrente de FULL CHARGE CAPACITY por DESIGN CAPACITY y el resultado multiplicalo por 100')
        st.write('8. Copia el numero en la casilla de texto aqui abajo ( ⚠ NO COPIES DECIMALES )')
        observacion = st.number_input(
            "Estado actual de la bateria",
            placeholder="" )
        st.session_state["Estado_B"] = observacion

col1, col2 = st.columns([3, 1])
st.divider()
with col1:
    st.session_state["Win_11"] = st.text_input("Observación",placeholder="Procesador del equipo" )
with col2:
    validar = st.button("Buscar procesador")
    if validar:
        if st.session_state["Win_11"] in base_datos:
            st.success("✅ El procesador es compatible con windows 11")
        else:
            st.error("❌ El procesador NO es compatible con windows 11")
st.divider()
Descripcion = st.text_input("Agrega una descripcion del equipo")