import streamlit as st
from fpdf import FPDF
from datetime import date
import qrcode


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

st.set_page_config(page_title="Contrato de Compraventa")

st.title("📄 Contrato")

datos = st.session_state.get("datos_cotizador")

if not datos:
    st.warning("No hay datos del cotizador. Regresa y calcula primero.")
    st.stop()

# Mostrar solo datos de nevera
if datos["Origen"] == "Nevera":
    # CONTRATO DE NEVERAS
    # Adaptamos los números a texto ( Marca )
    if datos['Marca'] == 1:
        datos['Marca'] = "Kalley"
    elif datos['Marca'] == 2:
        datos['Marca'] = "Indurama"
    elif datos['Marca'] == 3:
        datos['Marca'] = "Challenger"
    elif datos['Marca'] == 4:
        datos['Marca'] = "Midea"
    elif datos['Marca'] == 4.1:
        datos['Marca'] = "Hisense"
    elif datos['Marca'] == 5:
        datos['Marca'] = "Mabe"
    elif datos['Marca'] == 6:
        datos['Marca'] = "Haceb"
    elif datos['Marca'] == 6.1:
        datos['Marca'] = "Abba"
    elif datos['Marca'] == 7:
        datos['Marca'] = "Whirlpool"
    elif datos['Marca'] == 8:
        datos['Marca'] = "Electrolux"
    elif datos['Marca'] == 9:
        datos['Marca'] = "Samsung"
    elif datos['Marca'] == 10:
        datos['Marca'] = "LG"
    elif datos['Marca'] == 11:
        datos['Marca'] = "Bosch"
    elif datos['Marca'] == 12:
        datos['Marca'] = "KitchenAid"
    elif datos['Marca'] == 13:
        datos['Marca'] = "Frigidaire"
    elif datos['Marca'] == 13.1:
        datos['Marca'] = "GE Profile"
    elif datos['Marca'] == 14:
        datos['Marca'] = "Sub-Zero"
    elif datos['Marca'] == 14.1:
        datos['Marca'] = "Monogram"
    elif datos['Marca'] == 14.01:
        datos['Marca'] = "Liebherr"

    # Adaptamos los números a texto ( Litros )
    if datos['Litros'] == 1:
        datos['Litros'] = "40 y 120 litros"
    elif datos['Litros'] == 2:
        datos['Litros'] = "121 y 250 litros"
    elif datos['Litros'] == 3:
        datos['Litros'] = "251 y 450 litros"
    elif datos['Litros'] == 4:
        datos['Litros'] = "450 y 800 litros"

    # Adaptamos los números a texto ( Sistema de enfriamiento )
    if datos['Sistema'] == 5:
        datos['Sistema'] = "Auto frost"
    else:
        datos['Sistema'] = "No frost"
        
    st.write(f"Este contrato se basa en la compraventa de una {datos["Origen"]}, de la marca {datos['Marca']}, con una capacidad entre {datos['Litros']}, y sistema {datos['Sistema']}, Al precio de: {datos['Precio']}  pesos con una tasa del {datos['Tasa']}%")

elif datos["Origen"] == "Computador":
    # CONTRATO DE COMPUTADOR
    # Adaptamos de número a nombre ( Marca )
    if datos['Marca'] == 1:
        datos['Marca'] = "WINDOWS"
    elif datos['Marca'] == 2:
        datos['Marca'] = "Koorui"
    elif datos['Marca'] == 3:
        datos['Marca'] = "Acer"
    elif datos['Marca'] == 4:
        datos['Marca'] = "Hewlettpacka"
    elif datos['Marca'] == 5:
        datos['Marca'] = "VICTUS"
    elif datos['Marca'] == 6:
        datos['Marca'] = "Asus"
    elif datos['Marca'] == 7:
        datos['Marca'] = "SONY"
    elif datos['Marca'] == 8:
        datos['Marca'] = "Samsung"
    elif datos['Marca'] == 9:
        datos['Marca'] = "Dell"
    elif datos['Marca'] == 10:
        datos['Marca'] = "LENOVO"
    elif datos['Marca'] == 11:
        datos['Marca'] = "Apple"

    # Adaptamos de número a texto ( RAM )
    if datos['RAM'] == 2:
        datos['RAM'] = "2 GB de ram"
    elif datos['RAM'] == 4:
        datos['RAM'] = "4 GB de ram"
    elif datos['RAM'] == 6:
        datos['RAM'] = "6 GB de ram"
    elif datos['RAM'] == 7:
        datos['RAM'] = "8 GB de ram"
    elif datos['RAM'] == 12:
        datos['RAM'] = "12 GB de ram"
    elif datos['RAM'] == 16:
        datos['RAM'] = "16 GB de ram"
    elif datos['RAM'] == 32:
        datos['RAM'] = "32 GB de ram"
    elif datos['RAM'] == 64:
        datos['RAM'] = "64 GB de ram"

    # Adaptamos de número a texto ( Procesador )
    if datos["Procesador"] == 5:
        datos["Procesador"] = "Celeron"
    elif datos["Procesador"] == 5.000001:
        datos["Procesador"] = "Pentium"
    elif datos["Procesador"] == 5.0000001:
        datos["Procesador"] = "AMD"
    elif datos["Procesador"] == 5.00000001:
        datos["Procesador"] = "Athlon"
    elif datos["Procesador"] == 15:
        datos["Procesador"] = "Core i3 / Ryzen 3"
    elif datos["Procesador"] == 30:
        datos["Procesador"] = "Core i5 / Ryzen 5"
    elif datos["Procesador"] == 70:
        datos["Procesador"] = "Core i7 / Ryzen 7"
    elif datos["Procesador"] == 120:
        datos["Procesador"] = "Core i9 / Ryzen 9"

    # Adaptamos de número a texto ( Grafica )
    if datos['Grafica'] == 0:
        datos['Grafica'] = "Sin tarjeta grafica"
    else:
        datos['Grafica'] = "Con tarjeta grafica"

    st.write(f"Este contrato se basa en la compraventa de un {datos["Origen"]}, de la marca {datos['Marca']}, con {datos["RAM"]}, {datos["Disco"]} de espacio, con procesador {datos["Procesador"]}, y {datos["Grafica"]} Al precio de: {datos['Precio']}  pesos con una tasa del {datos['Tasa']}%")
    
    # CREACIÓN DEL PDF
    pdf = FPDF()
    pdf.add_page()

    # LOGO DE LA EMPRESA
    pdf.image("pages/Standard_logo.png", x=10, y=8, w=40)

    # TITULO DEL PDF
    pdf.set_font("Arial", "B", 14)
    pdf.ln(30)  # baja el cursor para no chocar con el logo
    pdf.cell(0, 10, "CONTRATO STANDARD", ln=True, align="C")

    # CONSEGUIR FECHA ACTUAL
    fecha_actual = date.today().strftime("%d/%m/%Y")

    # QR de las redes sociales de la empresa
    link = "data:image/jpeg;base64,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"
    qr = qrcode.make(link)
    qr.save("qr_temp.png")

    # Ubicación tabla
    tabla_x = 50
    tabla_y = 50

    # QR a la izquierda de la tabla
    pdf.image(
        "qr_temp.png",
        x=tabla_x - 35,
        y=tabla_y,
        w=30)

    # Tabla
    pdf.set_xy(tabla_x, tabla_y)
    pdf.set_font("Arial", size=10)
    # Fila 1 – Fecha
    pdf.cell(35, 8, "Fecha", border=1)
    pdf.cell(40, 8, fecha_actual, border=1, ln=True)
    # Fila 2 – Tasa
    pdf.set_x(tabla_x)
    pdf.cell(35, 8, "Tasa", border=1)
    pdf.cell(40, 8, f'{datos["Tasa"]}%', border=1, ln=True)
    # Fila 3 – Precio
    pdf.set_x(tabla_x)
    pdf.cell(35, 8, "Precio", border=1)
    pdf.cell(40, 8, f'${datos["Precio"]}', border=1, ln=True)

    # CONTENIDO DEL PDF
    pdf.ln(15)
    pdf.set_font("Arial", size=12)  # sin "B" que significa negrilla
    pdf.cell(0, 8, "CONTRATO DE COMPRAVENTA CON PACTO DE RETROVENTA. Artículo 1939 del Código Civil Colombiano.", ln=True)

    texto_grande = f"""
    Hola"""