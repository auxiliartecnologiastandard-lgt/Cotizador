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

if datos['Sede'] == 1:
    datos['Sede'] = "La 14 (Pereira)"
elif datos['Sede'] == 2:
    datos['Sede'] = "La 18 (Pereira)"
elif datos['Sede'] == 3:
    datos['Sede'] = "La 19 (Pereira)"
elif datos['Sede'] == 4:
    datos['Sede'] = "Cuba (Pereira)"
elif datos['Sede'] == 5:
    datos['Sede'] = "La 29 (Pereira)"
elif datos['Sede'] == 6:
    datos['Sede'] = "Crucero (Doquebradas)"
elif datos['Sede'] == 7:
    datos['Sede'] = "Naranjos (Dosquebradas)"
elif datos['Sede'] == 8:
    datos['Sede'] = "Japón (Dosquebradas)"
elif datos['Sede'] == 9:
    datos['Sede'] = "Sol brilla (Tuluá)"
elif datos['Sede'] == 10:
    datos['Sede'] = "Super Standard (Tuluá)"
elif datos['Sede'] == 11:
    datos['Sede'] = "Armenia"

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
    pdf = FPDF(orientation="P",  # P = vertical, L = horizontal
    unit="mm", format="Letter")
    pdf.set_margins(left=5, top=5, right=5)
    pdf.set_auto_page_break(auto=True, margin=5)

    # color rojo para que sea visible
    pdf.set_draw_color(0, 0, 0)
    # dibuja un rectángulo que represente el margen
    pdf.add_page()
    pdf.rect(
    x=pdf.l_margin,
    y=pdf.t_margin,
    w=pdf.w - pdf.l_margin - pdf.r_margin,
    h=pdf.h - pdf.t_margin - pdf.b_margin)

    # LOGO DE LA EMPRESA
    ruta_base = os.path.dirname(__file__)
    ruta_logo = os.path.join(ruta_base, "Standard_logo.png")
    pdf.image(ruta_logo, x=10, y=8, w=40)

    # TITULO DEL PDF
    pdf.set_font("Arial", "B", 15)
    pdf.ln(3)  # baja el cursor para no chocar con el logo
    pdf.cell(0, 3.5, "CONTRATO STANDARD", ln=True, align="C")

    # CONSEGUIR FECHA ACTUAL
    fecha_actual = date.today().strftime("%d/%m/%Y")

    # QR de las redes sociales de la empresa
    link = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSKGOMWCWfns00LGBl_0JZe53sCFCrp1xnQmg&s"
    qr = qrcode.make(link)
    qr.save("qr_temp.png")

    # Posición base del bloque (debajo del título)
    y_bloque = 7

    # Posición de la tabla (derecha)
    tabla_x = 175
    tabla_y = 7

    # QR a la izquierda de la tabla (NO de la hoja)
    pdf.image(
        "qr_temp.png",
        x=tabla_x - 17,
        y=y_bloque + 8,
        w=17)

    # Tabla
    pdf.set_xy(tabla_x, tabla_y)
    pdf.set_font("Arial", size=10)
    # Fila 1 – Fecha
    pdf.cell(33, 8, f"Fecha:  {fecha_actual}", border=1, ln=True)
    # Fila 2 – Tasa
    pdf.set_x(tabla_x)
    pdf.cell(33, 8, f"Plazo:  {datos["Meses"]} Meses", border=1, ln=True)
    # Fila 3 – Precio
    pdf.set_x(tabla_x)
    pdf.cell(33, 8, f"Precio:  {datos["Precio"]}", border=1, ln=True)

    # CONTENIDO DEL PDF
    pdf.ln(15)
    pdf.set_font("Arial","B", size=7)

    pdf.multi_cell(
        0,      # ancho automático
        2,      # alto de línea
        "CONTRATO DE COMPRAVENTA CON PACTO DE RETROVENTA. "
        "Artículo 1939 del Código Civil Colombiano.",
        align="C"   # L, C, R, J
        )
    pdf.ln(5)
    pdf.set_font("Arial", size=8)

    pdf.multi_cell(
        0,
        3,
        f"Entre los suscritos {datos['Nombre']} identificado con C.C. {datos['Cedula']}, mayor de edad quien obra en nombre propio y se denomina para efectos del presente contrato EL VENDEDOR de una parte, y por otra parte CASA COMERCIAL DE LOS ANDES S.A.S - Nit. 800.205.573-1, quien para los efectos del presente contrato se denomina EL COMPRADOR. Manifestamos que hemos celebrado un contrato de compraventa entre el siguiente bien que a continuación se identifica.\n\nObjeto: {datos['Origen']}\nMemoria RAM: {datos['RAM']}\nAlmacenamiento: {datos['Disco']} GB\nProcesador: {datos['Procesador']}\n{datos['Grafica']}\n\nEl valor de la compraventa es la suma de {datos['Precio']} M/cte. EL VENDEDOR transfiere AL COMPRADOR, a título de compraventa el derecho de dominio y posesión que tiene y ejerce sobre el anterior articulo y declara que los bienes que transfiere, los adquirió lícitamente, no fue su importador, son de su exclusiva propiedad, los posee de manera regular, publica y pacífica, están libres de gravamen, limitación al dominio, pleitos pendientes y embargos, con la obligación de salir al saneamiento en casos de ley.\n\n"
        )
    
    pdf.multi_cell(
        0,      # ancho automático
        3,      # alto de línea
        "CLÁUSULAS ACCESORIAS QUE RIGEN EL PRESENTE CONTRATO",
        align="C"   # L, C, R, J
        )
    pdf.ln(5)
    pdf.set_font("Arial", size=8)

    pdf.multi_cell(
        0,
        3,
        f"PRIMERA: Los contratantes de conformidad con el artículo 1939 del Código Civil Colombiano, pactan que EL VENDEDOR se reserva la facultad de recobrar los artículos vendidos por medio de este contrato, pagando AL COMPRADOR como precio de retroventa la suma de: {datos['Dinero']} SEGUNDA: El derecho que nace del pacto de retroventa del presente contrato, no podrácederse a ningún título. En caso de pérdida de este contrato EL VENDEDOR se obliga a dar noticia inmediata AL COMPRADOR y este, solo exhibirá el articulo descrito a la terminación del presente contrato. TERCERA: EL VENDEDOR y EL COMPRADOR pactan que la facultad de retroventa del presente contrato la podrá ejercer EL VENDEDOR dentro del término de -- {datos['Meses']} Meses -- prorrogables CUARTA: Autorizo a COANDES S.A.S, a consultar y verificar la información en las listas restrictivas con el fin de prevenir situaciones relacionadas con el lavado de activos y financiación del terrorismo. QUINTA: El VENDEDOR autoriza para que se recopile, almacene, use y suprima los datos personales aquí suministrados. Ley 1581 de 2012 y sus decretos reglamentarios. Podrá revocar esta autorización dirigiendo su petición al correo electrónico servicioalcliente@standard.com.co SEXTA: Las controversias relativas al presente contrato se resolverán por un tribunal de arbitramento de conformidad con las disposiciones que rigen la materia, nombrado por la Cámara de Comercio de esta ciudad. SEPTIMA: Tanto EL VENDEDOR como EL COMPRADOR hemos leído, comprendido y aceptado el texto de este contrato. OCTAVA: Así mismo acepto desde ahora la venta o cesión de los derechos que adquiere Casa comercial de los andes a otra empresa. En constancia de lo anterior lo firman las partes en la fecha {fecha_actual}"
        )

    pdf_bytes = pdf.output(dest="S").encode("latin-1")
    pdf_buffer = io.BytesIO(pdf_bytes)

    # Botón de descarga
    st.download_button(
        label="📥 Descargar PDF",
        data=pdf_buffer,
        file_name="contrato.pdf",
        mime="application/pdf"
    )