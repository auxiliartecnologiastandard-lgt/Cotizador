import streamlit as st
import os
import importlib.util

# 1. Configuración de pantalla
st.set_page_config(page_title="Cotizador Coandes", initial_sidebar_state="collapsed")
st.markdown("<style>[data-testid='stSidebar']{display:none;}</style>", unsafe_allow_html=True)

# 2. Ruta del cotizador de neveras
ruta_archivo = os.path.join("Cotizador_Coandes-copia", "Neveras", "app.py")

if os.path.exists(ruta_archivo):
    try:
        # 3. Importar el archivo como módulo dinámico
        spec = importlib.util.spec_from_file_location("nevera_cotizador", ruta_archivo)
        nevera_cotizador = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(nevera_cotizador)

        # 4. Ejecutar la función principal del cotizador (si tu app.py tiene una función main)
        if hasattr(nevera_cotizador, "main"):
            nevera_cotizador.main()  # esta función muestra el cotizador en Streamlit
        else:
            st.error("El archivo no tiene una función main() definida")

    except Exception as e:
        st.error("Error al ejecutar el cotizador")
        st.exception(e)
else:
    st.error(f"No se encontró el archivo en: {ruta_archivo}")