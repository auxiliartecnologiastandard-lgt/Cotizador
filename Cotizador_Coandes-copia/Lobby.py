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
        /* Eliminar elementos de Streamlit */
        [data-testid="collapsedControl"], [data-testid="stSidebar"] { display: none !important; }
        header { visibility: hidden !important; height: 0 !important; }
        
        /* Estilo para la franja del encabezado */
        .header-container {
            background-color: #F0F2F6; /* CAMBIA ESTE COLOR SI DESEAS OTRO FONDO */
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
            display: flex;
            align-items: center;
        }
        
        .header-text {
            margin-left: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# 2. Encabezado con fondo de color (Solo Logo y Título)
# Usamos columnas dentro de un contenedor de fondo
with st.container():
    # Este bloque HTML abre el fondo de color
    st.markdown('<div class="header-container">', unsafe_allow_html=True)
    
    col_logo, col_titulo = st.columns([0.15, 0.85])
    
    with col_logo:
        if os.path.exists(ruta_logo):
            st.image(ruta_logo, width=150)
        else:
            st.write("Logo no encontrado")
            
    with col_titulo:
        st.markdown('<h1 style="margin:0;">Sistema de Cotización Inteligente</h1>', unsafe_allow_html=True)
        st.write("Bienvenido/a. Selecciona una categoría para empezar:")
    
    # Este bloque cierra el fondo de color
    st.markdown('</div>', unsafe_allow_html=True)

# 3. Resto de la página (Fondo normal de Streamlit)
st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("💻 Computadores", use_container_width=True):
        st.switch_page("pages/Com.py")
    if st.button("🥇 Oro (Próximamente)", use_container_width=True, disabled=True):
        pass

with col2:
    if st.button("🧊 Neveras", use_container_width=True):
        st.switch_page("pages/Nev.py")
    if st.button("🔨 Herramientas (Próximamente)", use_container_width=True, disabled=True):
        pass

with col3:
    if st.button("🛵 Motos (Próximamente)", use_container_width=True, disabled=True):
        pass
    if st.button("🎸 Instrumentos (Próximamente)", use_container_width=True, disabled=True):
        pass