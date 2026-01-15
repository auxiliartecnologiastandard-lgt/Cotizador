import streamlit as st
from fpdf import FPDF
from datetime import date
import qrcode
import os
import io

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
    ruta_base = os.path.dirname(__file__)
    ruta_logo = os.path.join(ruta_base, "Standard_logo.png")
    pdf.image(ruta_logo, x=10, y=8, w=40)

    # TITULO DEL PDF
    pdf.set_font("Arial", "B", 14)
    pdf.ln(35)  # baja el cursor para no chocar con el logo
    pdf.cell(0, 10, "CONTRATO STANDARD", ln=True, align="C")

    # CONSEGUIR FECHA ACTUAL
    fecha_actual = date.today().strftime("%d/%m/%Y")

    # QR de las redes sociales de la empresa
    link = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSKGOMWCWfns00LGBl_0JZe53sCFCrp1xnQmg&s"
    qr = qrcode.make(link)
    qr.save("qr_temp.png")

    # Posición base del bloque (debajo del título)
    y_bloque = 55

    # Posición de la tabla (derecha)
    tabla_x = 70
    tabla_y = y_bloque

    # QR a la izquierda de la tabla (NO de la hoja)
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
    pdf.multi_cell(
    0,
    8,
    "CONTRATO DE COMPRAVENTA CON PACTO DE RETROVENTA. "
    "Artículo 1939 del Código Civil Colombiano."
)


    texto_grande = f"""
    Hola"""

    pdf_bytes = pdf.output(dest="S").encode("latin-1")
    pdf_buffer = io.BytesIO(pdf_bytes)

    # Botón de descarga
    st.download_button(
        label="📥 Descargar PDF",
        data=pdf_buffer,
        file_name="contrato.pdf",
        mime="application/pdf"
    )