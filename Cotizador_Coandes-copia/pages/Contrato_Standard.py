import streamlit as st

st.title("Contrato de Compraventa - Nevera")

# Verificamos si hay datos en session_state
datos = st.session_state.get('datos_cotizador', None)

if not datos:
    st.warning("No se han recibido datos desde ningún cotizador. Por favor, vuelve al cotizador.")
else:
    # Solo consideramos nevera
    if datos.get("Origen") != "nevera":
        st.warning("Los datos recibidos no corresponden a una nevera.")
    else:
        st.subheader("Detalles del Contrato")

        st.write(f"Marca: {datos.get('Marca', 'No especificada')}")
        st.write(f"Capacidad: {datos.get('Litros', 'No especificada')} litros")
        st.write(f"Sistema de enfriamiento: {datos.get('Sistema', 'No especificado')}")
        st.write(f"Tasa de interés o comisión: {datos.get('Tasa', 'No especificada')}")
        st.write(f"Precio estimado: {datos.get('Precio', 'No especificado')}")

        # Botón opcional para guardar o descargar contrato
        if st.button("Generar PDF del contrato"):
            # Aquí pondrías la lógica para generar PDF
            st.success("PDF generado (funcionalidad pendiente de implementar).")
