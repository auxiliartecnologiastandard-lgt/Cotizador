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

with st.expander("📝 Como sacar el estado de la bateria"):
    st.write("1. Presionar ""Windows + X""y selecciona Windows powershell")
    st.write("2. Copia ➡ "" powercfg /batteryreport "", pegalo en powershell y despues presiona Enter")
    st.write("3. Copia el link que te ofrecio powershell. Ejemplo: C:\Users\TuUsuario\Battery-report.html.")
    st.write("4. Pega ese link que copiaste en cualquier navegador ( Microsoft edge, Chrome, Firefox...)")
    st.write("5. Busca un apartado que diga "" Installed batteries "" ( Esta al principio de la pagina )")
    st.write("6. Busca en installed bateries secciones que digan "" DESIGN CAPACITY "" y "" FULL CHARGE CAPACITY """)
    st.write("7. Divide el numero alfrente de FULL CHARGE CAPACITY por DESIGN CAPACITY y el resultado multiplicalo por 100")
    st.write("8. Copia el numero en la casilla de texto aqui abajo ( ⚠ NO COPIES DECIMALES )")
    observacion = st.text_input(
        "Observación",
        placeholder="Ej: Pequeño rayón en la tapa, no afecta funcionamiento" )
