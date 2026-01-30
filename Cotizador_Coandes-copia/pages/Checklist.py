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

st.markdown("### 1. Información del equipo") 
Marca = st.text_input("Escribe la marca del equipo")
Modelo = st.text_input("Escribe la modelo del equipo")
with st.expander("Como sacar el modelo del equipo"):
    st.write('1. Presionar " Windows + R ", escribe cmd y preciona enter')
    st.write('2. Escribe " wmic csproduct get name " y despues presiona Enter')
    st.write('3. Aparecera la palabra " Name " y justo debajo el modelo del equipo')
Serial = st.text_input("Escribe el serial del equipo")
with st.expander("Como sacar el serial del equipo"):
    st.write('1. Presionar " Windows + R ", escribe cmd y preciona enter')
    st.write('2. Escribe " wmic bios get serialnumber " y despues presiona Enter')
    st.write('3. Aparecera la palabra " SerialNumber " y justo debajo el serial del equipo')
RAM = st.number_input("Escribe la RAM ( Solo el número )", min_value=1)
Disco = st.number_input("Escribe la capacidad ( Solo el número )", min_value=1)
Nombre = st.text_input("Escribe el nombre del equipo")
with st.expander("Como sacar la RAM y capacidad del disco duro del equipo"):
    st.write('1. Presionar la tecla windows ( El cuadrado dividdido en 4 )')
    st.write('2. Escribe " Configuracion " y despues presiona Enter')
    st.write('3. Busca el apartado que diga sistema')
    st.write('4. En la parte lateral izquierda baja hasta encontrar una opción que diga " Acerca de " o " Más información " y dale click')
    st.write('5. Hay encontraras la capacidad de la RAM, la capacidad del disco duro y el nombre del equipo')
Bateria = st.number_input("Escribe el estado de la bateria", min_value=1)
with st.expander("Como sacar el estado de la bateria"):
    st.write('1. Presionar " Windows + X "y selecciona Windows powershell')
    st.write('2. Copia ➡ " powercfg /batteryreport ", pegalo en powershell y despues presiona Enter')
    st.write('3. Copia el link que te ofrecio powershell. Ejemplo: C:\\Users\\TuUsuario\\Battery-report.html.')
    st.write('4. Pega ese link que copiaste en cualquier navegador ( Microsoft edge, Chrome, Firefox...)')
    st.write('5. Busca un apartado que diga " Installed batteries " ( Esta al principio de la pagina )')
    st.write('6. Busca en installed bateries secciones que digan " DESIGN CAPACITY " y " FULL CHARGE CAPACITY " ')
    st.write('7. Divide el numero alfrente de FULL CHARGE CAPACITY por DESIGN CAPACITY y el resultado multiplicalo por 100')
    st.write('8. ⚠ NO COPIES DECIMALES')

st.markdown("### 2. Pruebas de conectividad")
Wifi = 8