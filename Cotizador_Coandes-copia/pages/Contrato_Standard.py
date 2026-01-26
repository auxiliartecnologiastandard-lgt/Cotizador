import streamlit as st
from fpdf import FPDF
from datetime import date
from datetime import datetime
import qrcode
import os
import io
from dateutil.relativedelta import relativedelta
from zoneinfo import ZoneInfo

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

st.set_page_config(page_title="Contrato standard")

IdentificadorSede = 0

datos = st.session_state.get("datos_cotizador")

if not datos:
    st.warning("No hay datos del cotizador. Regresa y calcula primero.")
    st.stop()

def leer_contador():
    if not os.path.exists("contador.txt"):
        with open("contador.txt", "w") as f:
            f.write("0")

    with open("contador.txt", "r") as f:
        contenido = f.read().strip()

    if not contenido.isdigit():
        # si el archivo está dañado, lo reseteamos
        with open("contador.txt", "w") as f:
            f.write("0")
        return 0

    return int(contenido)

def incrementar_contador():
    contador = leer_contador() + 1
    with open("contador.txt", "w") as f:
        f.write(str(contador))
        
    return contador


numero_contrato = leer_contador()

if datos['Sede'] in [1, 2, 3, 4, 5]:
    datos['Direcciones'] = "PEREIRA"
elif datos['Sede'] in [6, 7, 8]:
    datos['Direcciones'] = "DOSQUEBRADAS"
elif datos['Sede'] in [9, 10]:
    datos['Direcciones'] = "TULUÁ"
else:
    datos['Direcciones'] = "ARMENIA"

if datos['Sede'] == 1:
    datos['IdentificadorSede'] = 4
elif datos['Sede'] == 2:
    datos['IdentificadorSede'] = 16
elif datos['Sede'] == 3:
    datos['IdentificadorSede'] = 11
elif datos['Sede'] == 4:
    datos['IdentificadorSede'] = 7
elif datos['Sede'] == 5:
    datos['IdentificadorSede'] = 15
elif datos['Sede'] == 6:
    datos['IdentificadorSede'] = 8
elif datos['Sede'] == 7:
    datos['IdentificadorSede'] = 12
elif datos['Sede'] == 8:
    datos['IdentificadorSede'] = 27
elif datos['Sede'] == 9:
    datos['IdentificadorSede'] = 19
elif datos['Sede'] == 10:
    datos['IdentificadorSede'] = 18
elif datos['Sede'] == 11:
    datos['IdentificadorSede'] = 9

if datos['Sede'] == 1:
    datos['Sede'] = "Calle 14 # 8-24 \n Standard La 14 \n 320 610 403 \n standardcuatro.per@standard.com.co \n Nit. 800.205.573-1"
elif datos['Sede'] == 2:
    datos['Sede'] = "Calle 18 # 8-07 \n Standard La 18 \n 310 397 1905 \n standardla18.per@standard.com.co \n Nit. 800.205.573-1"
elif datos['Sede'] == 3:
    datos['Sede'] = "Calle 19 # 10-53 \n Standard La 19 \n 316 833 6917 \n standardla19.per@standard.com.co \n Nit. 800.205.573-1"
elif datos['Sede'] == 4:
    datos['Sede'] = "Cra 23bis # 71-32 \n Standard Cuba \n 320 766 9884 \n standardcuba.per@standard.com.co \n Nit. 800.205.573-1"
elif datos['Sede'] == 5:
    datos['Sede'] = "Cra 7 # 29-07 \n Standard La 29 \n 322 304 8622 \n standardla29.per@standard.com.co \n Nit. 800.205.573-1"
elif datos['Sede'] == 6:
    datos['Sede'] = "Cra 16 # 44-23 \n Standard Crucero \n 310 396 8819 \n standardcrucero.per@standard.com.co \n Nit. 800.205.573-1"
elif datos['Sede'] == 7:
    datos['Sede'] = "Cra 16 # 51-27 \n Standard Naranjos \n 310 396 8819 \n standardnaranjos.per@standard.com.co \n Nit. 800.205.573-1"
elif datos['Sede'] == 8:
    datos['Sede'] = "Calle 8 # 23-10 \n Standard Japón \n 322 311 9148 \n standardjapon.dqs@standard.com.co \n Nit. 800.205.573-1"
elif datos['Sede'] == 9:
    datos['Sede'] = "Cra 25 # 26-65 \n Sol Brilla \n 313 496 4897 \n solbrilla.tul@standard.com.co \n Nit. 800.205.573-1"
elif datos['Sede'] == 10:
    datos['Sede'] = "Cra 21 # 26A-20 \n Super Standard \n 316 833 6924 \n superstandard18.tul@standard.com.co \n Nit. 800.205.573-1"
elif datos['Sede'] == 11:
    datos['Sede'] = "Cra 17 # 21-13 \n Standard Armenia \n 320 766 9899 \n standardarmenia@standard.com.co \n Nit. 800.205.573-1"

def mc(pdf, txt, h=3, max_size=8, min_size=1):
    limite_y = pdf.h - pdf.b_margin - 5
    y_start = pdf.get_y()

    for size in [x / 2 for x in range(int(max_size*2), int(min_size*2)-1, -1)]:
        pdf.set_font("Arial", "", size)

        # Simulación sin imprimir
        y_test = y_start
        for line in pdf.multi_cell(0, h, txt, split_only=True):
            y_test += h

        if y_test <= limite_y:
            pdf.set_font("Arial", "", size)
            pdf.set_y(y_start)
            pdf.multi_cell(0, h, txt)
            return

    # Último recurso
    pdf.set_font("Arial", "", min_size)
    pdf.set_y(y_start)
    pdf.multi_cell(0, h, txt)



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
        

    def dibujar_contrato(pdf, datos, y_offset=0):

        # Margen contrato
        # Margen contrato
        pdf.rect(
        x=pdf.l_margin,
        y=22 + y_offset,
        w=pdf.w - pdf.l_margin - pdf.r_margin,
        h=132)

        # LOGO DE LA EMPRESA
        ruta_base = os.path.dirname(__file__)
        ruta_logo = os.path.join(ruta_base, "Standard_logo.png")
        pdf.image(ruta_logo, x=10, y=23.5 + y_offset, w=40)

        # TITULO DEL PDF
        pdf.set_y(20 + y_offset)
        pdf.set_font("Arial", "B", 10)
        pdf.ln(3)  # baja el cursor para no chocar con el logo
        pdf.cell(0, 3, f"STANDARD {datos["Direcciones"]}", ln=True, align="C")
        # DIRRECIONES
        pdf.set_font("Arial", "", 7)
        pdf.ln(2.5)
        pdf.multi_cell(0, 2.5, f"{datos['Sede']}", align="C")

        # CONSEGUIR FECHA ACTUAL
        fecha_actual = date.today()

        # FECHA VENCIMIENTO
        Meses = int(datos["Meses"])  # o tu variable Meses
        fecha_vencimiento = fecha_actual + relativedelta(months=Meses)
        fecha_vencimiento_str = fecha_vencimiento.strftime("%d/%m/%Y")
        fecha_actual = date.today().strftime("%d/%m/%Y")

        hora_actual = datetime.now(ZoneInfo("America/Bogota")).strftime("%I:%M %p")

        pdf.set_xy(1,46 + y_offset)
        pdf.set_draw_color(0, 0, 0)
        pdf.rect(
            x=1,
            y=45 + y_offset,
            w=33,
            h=5)
        pdf.multi_cell(0, 3, f"Fecha Inicio:  {fecha_actual}", align="L")


        # QR de las redes sociales de la empresa
        link = "https://hab.me/YCh4LCw"
        qr = qrcode.make(link)
        qr.save("qr_temp.png")

        # Posición base del bloque (debajo del título)
        y_bloque = 20

        # Posición de la tabla (derecha)
        tabla_x = 175
        tabla_y = 27 + y_offset

        # QR a la izquierda de la tabla (NO de la hoja)
        pdf.image(
            "qr_temp.png",
            x=tabla_x - 17,
            y=y_bloque + 8 + y_offset,
            w=17)
        

        pdf.set_xy(175, 22 + y_offset)
        pdf.set_font("Arial", "B", size=8)
        pdf.multi_cell(0, 2.5, f"Contrato No.\n{datos["IdentificadorSede"]}-{numero_contrato}", align="C")

        # Tabla
        pdf.set_xy(tabla_x, tabla_y)
        pdf.set_font("Arial", size=7)
        # Fila 1 – Fecha
        pdf.cell(33, 5.5, f"Fecha:  {fecha_actual}", border=1, ln=True)
        # Fila 2 – Tasa
        pdf.set_x(tabla_x)
        pdf.cell(33, 5.5, f"Plazo:  {datos["Meses"]} Meses", border=1, ln=True)
        # Fila 3 – Precio
        pdf.set_x(tabla_x)
        pdf.cell(33, 5.5, f"Precio:  {datos["Precio"]}", border=1, ln=True)

        # CUERPO DEL PDF
        # INICIO 
        pdf.ln(5)
        pdf.set_font("Arial","B", size=8)

        pdf.multi_cell(
            0,      # ancho automático
            2,      # alto de línea
            "CONTRATO DE COMPRAVENTA CON PACTO DE RETROVENTA. "
            "Artículo 1939 del Código Civil Colombiano.",
            align="C"   # L, C, R, J
            )
        
        # INICIO TEXTO
        pdf.ln(1)
        pdf.set_font("Arial", size=4)
        
        mc(pdf,
            f"Entre los suscritos {datos['Nombre']} identificado con C.C. {datos['Cedula']}, mayor de edad quien obra en nombre propio y se denomina para efectos del presente contrato EL VENDEDOR de una parte, y por otra parte CASA COMERCIAL DE LOS ANDES S.A.S - Nit. 800.205.573-1, quien para los efectos del presente contrato se denomina EL COMPRADOR. Manifestamos que hemos celebrado un contrato de compraventa entre el siguiente bien que a continuación se identifica.\n\nObjeto: {datos['Origen']}\n Marca: {datos['Marca']}\nCapacidad {datos['Litros']}\nSistema: {datos['Sistema']}\n\nEl valor de la compraventa es la suma de {datos['Precio']} M/cte. EL VENDEDOR transfiere AL COMPRADOR, a título de compraventa el derecho de dominio y posesión que tiene y ejerce sobre el anterior articulo y declara que los bienes que transfiere, los adquirió lícitamente, no fue su importador, son de su exclusiva propiedad, los posee de manera regular, publica y pacífica, están libres de gravamen, limitación al dominio, pleitos pendientes y embargos, con la obligación de salir al saneamiento en casos de ley."
            )
        
        # CLAUSULA
        pdf.ln(1)
        pdf.set_font("Arial","B", size=7)

        pdf.multi_cell(
            0,      # ancho automático
            1,      # alto de línea
            "CLÁUSULAS ACCESORIAS QUE RIGEN EL PRESENTE CONTRATO",
            align="C"   # L, C, R, J
            )

        # CLAUSULA TEXTO
        pdf.ln(1)
        pdf.set_font("Arial", size=5)

        mc(pdf,
            f"PRIMERA: Los contratantes de conformidad con el artículo 1939 del Código Civil Colombiano, pactan que EL VENDEDOR se reserva la facultad de recobrar los artículos vendidos por medio de este contrato, pagando AL COMPRADOR como precio de retroventa la suma de: {datos['Dinero']} SEGUNDA: El derecho que nace del pacto de retroventa del presente contrato, no podrácederse a ningún título. En caso de pérdida de este contrato EL VENDEDOR se obliga a dar noticia inmediata AL COMPRADOR y este, solo exhibirá el articulo descrito a la terminación del presente contrato. TERCERA: EL VENDEDOR y EL COMPRADOR pactan que la facultad de retroventa del presente contrato la podrá ejercer EL VENDEDOR dentro del término de -- {datos['Meses']} Meses -- prorrogables CUARTA: Autorizo a COANDES S.A.S, a consultar y verificar la información en las listas restrictivas con el fin de prevenir situaciones relacionadas con el lavado de activos y financiación del terrorismo. QUINTA: El VENDEDOR autoriza para que se recopile, almacene, use y suprima los datos personales aquí suministrados. Ley 1581 de 2012 y sus decretos reglamentarios. Podrá revocar esta autorización dirigiendo su petición al correo electrónico servicioalcliente@standard.com.co SEXTA: Las controversias relativas al presente contrato se resolverán por un tribunal de arbitramento de conformidad con las disposiciones que rigen la materia, nombrado por la Cámara de Comercio de esta ciudad. SEPTIMA: Tanto EL VENDEDOR como EL COMPRADOR hemos leído, comprendido y aceptado el texto de este contrato. OCTAVA: Así mismo acepto desde ahora la venta o cesión de los derechos que adquiere Casa comercial de los andes a otra empresa. En constancia de lo anterior lo firman las partes en la fecha {fecha_actual}, {hora_actual}."
            )

        pdf.ln(3)
        pdf.set_font("Arial","B", size=8)

        # OTROS
        pdf.multi_cell(
            0,      # ancho automático
            1,      # alto de línea
            "EL VENDEDOR",
            align="L"   # L, C, R, J
            )
        
        pdf.set_draw_color(0, 0, 0)
        pdf.rect(x=185, y=128.5 + y_offset, w=30, h=5)
        pdf.multi_cell(0, 1, f"Vence:  {fecha_vencimiento_str}", align="R")

        if y_offset >= 130:

            pdf.ln(3)
            pdf.set_font("Arial","", size=7)
            pdf.multi_cell(
                0,      # ancho automático
                3,      # alto de línea
                f"_____________________________\n{datos['Nombre']}\nC.C: {datos['Cedula']}",
                align="L"   # L, C, R, J
                )

            pdf.set_xy(50, 126.4 + y_offset)   # Ajusta posición
            pdf.cell(20, 18, "", border=1)

            pdf.ln(3)
            pdf.set_xy(90, 128.5 + y_offset)
            pdf.set_font("Arial","B", size=8)

            # OTROS
            pdf.multi_cell(
                0,      # ancho automático
                1,      # alto de línea
                "EL COMPRADOR",
                align="L"   # L, C, R, J
                )
            
            pdf.ln(14)
            pdf.set_xy(90, 130 + y_offset)
            pdf.set_font("Arial","", size=7)
            pdf.multi_cell(
                0,      # ancho automático
                3,      # alto de línea
                f"_____________________________ \n EL COMPRADOR",   # L, C, R, J
                )
            
            pdf.ln(10)
            pdf.set_xy(160, 141.5 + y_offset)
            pdf.set_font("Arial","", size=7)
            pdf.multi_cell(
                0,      # ancho automático
                3.5,      # alto de línea
                f"_____________________________ \n VISTO BUENO",   # L, C, R, J
                    )
        else:

            pdf.ln(7)
            pdf.set_font("Arial","", size=7)
            pdf.multi_cell(
                0,      # ancho automático
                3,      # alto de línea
                f"_____________________________\n{datos['Nombre']}\nC.C: {datos['Cedula']}",
                align="L"   # L, C, R, J
                )
        
            pdf.set_xy(50, 131 + y_offset)   # Ajusta posición
            pdf.cell(20, 21, "", border=1)

            pdf.set_font("Arial","", size=5)
            pdf.set_xy(50, 141 + y_offset)
            pdf.cell(20, 20, "Huella del vendedor", align="C")


            pdf.ln(3)
            pdf.set_xy(90, 131 + y_offset)
            pdf.set_font("Arial","B", size=8)

            # OTROS
            pdf.multi_cell(
                0,      # ancho automático
                1,      # alto de línea
                "EL COMPRADOR",
                align="L"   # L, C, R, J
                )
            
            pdf.ln(14)
            pdf.set_xy(90, 141.5 + y_offset)
            pdf.set_font("Arial","", size=7)
            pdf.multi_cell(
                0,      # ancho automático
                3,      # alto de línea
                f"_____________________________ \n EL COMPRADOR",   # L, C, R, J
                )
            
            pdf.ln(10)
            pdf.set_xy(160, 141.5 + y_offset)
            pdf.set_font("Arial","", size=7)
            pdf.multi_cell(
                0,      # ancho automático
                3.5,      # alto de línea
                f"_____________________________ \n VISTO BUENO",   # L, C, R, J
                    )


    # CREACIÓN DEL PDF
    pdf = FPDF(orientation="P",  # P = vertical, L = horizontal
    unit="mm", format="Letter")
    pdf.set_margins(left=1, top=1, right=1)
    pdf.set_auto_page_break(auto=True, margin=1)

    # color rojo para que sea visible
    pdf.set_draw_color(0, 0, 0)
    # dibuja un rectángulo que represente el margen
    pdf.add_page()

    # BLOQUE SUPERIOR ( Identificador )
    alto_bloque = 20

    pdf.set_draw_color(0, 0, 0)
    pdf.rect(
        x=pdf.l_margin,
        y=pdf.t_margin,
        w=90,
        h=alto_bloque
    )
    pdf.set_font("Arial", "B", 18)
    pdf.cell(0, 6, f"{datos["IdentificadorSede"]}-{numero_contrato}")
    pdf.set_font("Arial", "", 9)
    pdf.set_xy(35, 1)
    pdf.multi_cell(0, 3, f"Marca: {datos['Marca']}\nCapacidad: {datos['Litros']}\nSistema: {datos['Sistema']}")
    pdf.set_y(5.5)
    pdf.cell(0, 8, f"{datos['Meses']} Meses", ln=True)
    pdf.cell(0, 3, f"{datos['Nombre']} - CC {datos['Cedula']}", ln=True)
    pdf.cell(0, 3, f"{datos['Origen']}: {datos['Precio']}", ln=True)
    pdf.set_xy(140, 5.5)
    pdf.multi_cell(0, 6, "__________________________________ \n Firma Vendedor")


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


    def dibujar_contrato(pdf, datos, y_offset=0):
    
        # Margen contrato
        pdf.rect(
        x=pdf.l_margin,
        y=22 + y_offset,
        w=pdf.w - pdf.l_margin - pdf.r_margin,
        h=132)

        # LOGO DE LA EMPRESA
        ruta_base = os.path.dirname(__file__)
        ruta_logo = os.path.join(ruta_base, "Standard_logo.png")
        pdf.image(ruta_logo, x=10, y=23.5 + y_offset, w=40)

        # TITULO DEL PDF
        pdf.set_y(20 + y_offset)
        pdf.set_font("Arial", "B", 10)
        pdf.ln(3)  # baja el cursor para no chocar con el logo
        pdf.cell(0, 3, f"STANDARD {datos["Direcciones"]}", ln=True, align="C")
        # DIRRECIONES
        pdf.set_font("Arial", "", 7)
        pdf.ln(2.5)
        pdf.multi_cell(0, 2.5, f"{datos['Sede']}", align="C")

        # CONSEGUIR FECHA ACTUAL
        fecha_actual = date.today()

        # FECHA VENCIMIENTO
        Meses = int(datos["Meses"])  # o tu variable Meses
        fecha_vencimiento = fecha_actual + relativedelta(months=Meses)
        fecha_vencimiento_str = fecha_vencimiento.strftime("%d/%m/%Y")
        fecha_actual = date.today().strftime("%d/%m/%Y")

        hora_actual = datetime.now(ZoneInfo("America/Bogota")).strftime("%I:%M %p")

        pdf.set_xy(1,46 + y_offset)
        pdf.set_draw_color(0, 0, 0)
        pdf.rect(
            x=1,
            y=45 + y_offset,
            w=33,
            h=5)
        pdf.multi_cell(0, 3, f"Fecha Inicio:  {fecha_actual}", align="L")
        

        # QR de las redes sociales de la empresa
        link = "https://hab.me/YCh4LCw"
        qr = qrcode.make(link)
        qr.save("qr_temp.png")

        # Posición base del bloque (debajo del título)
        y_bloque = 20

        # Posición de la tabla (derecha)
        tabla_x = 175
        tabla_y = 27 + y_offset

        # QR a la izquierda de la tabla (NO de la hoja)
        pdf.image(
            "qr_temp.png",
            x=tabla_x - 17,
            y=y_bloque + 8 + y_offset,
            w=17)
        

        pdf.set_xy(175, 22 + y_offset)
        pdf.set_font("Arial", "B", size=8)
        pdf.multi_cell(0, 2.5, f"Contrato No.\n{datos["IdentificadorSede"]}-{numero_contrato}", align="C")

        
        # Tabla
        pdf.set_xy(tabla_x, tabla_y)
        pdf.set_font("Arial", size=7)
        # Fila 1 – Fecha
        pdf.cell(33, 5.5, f"Fecha:  {fecha_actual}", border=1, ln=True)
        # Fila 2 – Tasa
        pdf.set_x(tabla_x)
        pdf.cell(33, 5.5, f"Plazo:  {datos["Meses"]} Meses", border=1, ln=True)
        # Fila 3 – Precio
        pdf.set_x(tabla_x)
        pdf.cell(33, 5.5, f"Precio:  {datos["Precio"]}", border=1, ln=True)

        # CUERPO DEL PDF
        # INICIO 
        pdf.ln(5)
        pdf.set_font("Arial","B", size=8)

        pdf.multi_cell(
            0,      # ancho automático
            2,      # alto de línea
            "CONTRATO DE COMPRAVENTA CON PACTO DE RETROVENTA. "
            "Artículo 1939 del Código Civil Colombiano.",
            align="C"   # L, C, R, J
            )
        
        # INICIO TEXTO
        pdf.ln(1)
        pdf.set_font("Arial", size=4)
        
        mc(pdf,
            f"Entre los suscritos {datos['Nombre']} identificado con C.C. {datos['Cedula']}, mayor de edad quien obra en nombre propio y se denomina para efectos del presente contrato EL VENDEDOR de una parte, y por otra parte CASA COMERCIAL DE LOS ANDES S.A.S - Nit. 800.205.573-1, quien para los efectos del presente contrato se denomina EL COMPRADOR. Manifestamos que hemos celebrado un contrato de compraventa entre el siguiente bien que a continuación se identifica.\n\nObjeto: {datos['Origen']}\nMemoria RAM: {datos['RAM']}\nAlmacenamiento: {datos['Disco']} GB\nProcesador: {datos['Procesador']}\n{datos['Grafica']}\n\nEl valor de la compraventa es la suma de {datos['Precio']} M/cte. EL VENDEDOR transfiere AL COMPRADOR, a título de compraventa el derecho de dominio y posesión que tiene y ejerce sobre el anterior articulo y declara que los bienes que transfiere, los adquirió lícitamente, no fue su importador, son de su exclusiva propiedad, los posee de manera regular, publica y pacífica, están libres de gravamen, limitación al dominio, pleitos pendientes y embargos, con la obligación de salir al saneamiento en casos de ley."
            )
        
        # CLAUSULA
        pdf.ln(1)
        pdf.set_font("Arial","B", size=7)

        pdf.multi_cell(
            0,      # ancho automático
            1,      # alto de línea
            "CLÁUSULAS ACCESORIAS QUE RIGEN EL PRESENTE CONTRATO",
            align="C"   # L, C, R, J
            )

        # CLAUSULA TEXTO
        pdf.ln(1)
        pdf.set_font("Arial", size=5)

        mc(pdf,
            f"PRIMERA: Los contratantes de conformidad con el artículo 1939 del Código Civil Colombiano, pactan que EL VENDEDOR se reserva la facultad de recobrar los artículos vendidos por medio de este contrato, pagando AL COMPRADOR como precio de retroventa la suma de: {datos['Dinero']} SEGUNDA: El derecho que nace del pacto de retroventa del presente contrato, no podrácederse a ningún título. En caso de pérdida de este contrato EL VENDEDOR se obliga a dar noticia inmediata AL COMPRADOR y este, solo exhibirá el articulo descrito a la terminación del presente contrato. TERCERA: EL VENDEDOR y EL COMPRADOR pactan que la facultad de retroventa del presente contrato la podrá ejercer EL VENDEDOR dentro del término de -- {datos['Meses']} Meses -- prorrogables CUARTA: Autorizo a COANDES S.A.S, a consultar y verificar la información en las listas restrictivas con el fin de prevenir situaciones relacionadas con el lavado de activos y financiación del terrorismo. QUINTA: El VENDEDOR autoriza para que se recopile, almacene, use y suprima los datos personales aquí suministrados. Ley 1581 de 2012 y sus decretos reglamentarios. Podrá revocar esta autorización dirigiendo su petición al correo electrónico servicioalcliente@standard.com.co SEXTA: Las controversias relativas al presente contrato se resolverán por un tribunal de arbitramento de conformidad con las disposiciones que rigen la materia, nombrado por la Cámara de Comercio de esta ciudad. SEPTIMA: Tanto EL VENDEDOR como EL COMPRADOR hemos leído, comprendido y aceptado el texto de este contrato. OCTAVA: Así mismo acepto desde ahora la venta o cesión de los derechos que adquiere Casa comercial de los andes a otra empresa. En constancia de lo anterior lo firman las partes en la fecha {fecha_actual}, {hora_actual}."
            )

        pdf.ln(3)
        pdf.set_font("Arial","B", size=8)

        # OTROS
        pdf.multi_cell(
            0,      # ancho automático
            1,      # alto de línea
            "EL VENDEDOR",
            align="L"   # L, C, R, J
            )
        
        
        pdf.set_draw_color(0, 0, 0)
        pdf.rect(x=185, y=131.5 + y_offset, w=30, h=4)
        pdf.multi_cell(0, 1, f"Vence:  {fecha_vencimiento_str}", align="R")

        
        pdf.ln(7)
        pdf.set_font("Arial","", size=7)
        pdf.multi_cell(
            0,      # ancho automático
            3,      # alto de línea
            f"_____________________________ \n {datos['Nombre']} \n C.C: {datos['Cedula']}",
            align="L"   # L, C, R, J
            )
        
        pdf.set_xy(50, 131 + y_offset)   # Ajusta posición
        pdf.cell(20, 21, "", border=1)

        pdf.set_font("Arial","", size=5)
        pdf.set_xy(50, 141 + y_offset)
        pdf.cell(20, 20, "Huella del vendedor", align="C")


        pdf.ln(3)
        pdf.set_xy(90, 131 + y_offset)
        pdf.set_font("Arial","B", size=8)

        # OTROS
        pdf.multi_cell(
            0,      # ancho automático
            1,      # alto de línea
            "EL COMPRADOR",
            align="L"   # L, C, R, J
            )
        
        pdf.ln(14)
        pdf.set_xy(90, 141.5 + y_offset)
        pdf.set_font("Arial","", size=7)
        pdf.multi_cell(
            0,      # ancho automático
            3,      # alto de línea
            f"_____________________________ \n EL COMPRADOR",   # L, C, R, J
            )
        
        pdf.ln(10)
        pdf.set_xy(160, 141.5 + y_offset)
        pdf.set_font("Arial","", size=7)
        pdf.multi_cell(
            0,      # ancho automático
            3.5,      # alto de línea
            f"_____________________________ \n VISTO BUENO",   # L, C, R, J
                )


    # CREACIÓN DEL PDF
    pdf = FPDF(orientation="P",  # P = vertical, L = horizontal
    unit="mm", format="Letter")
    pdf.set_margins(left=1, top=1, right=1)

    # color rojo para que sea visible
    pdf.set_draw_color(0, 0, 0)
    # dibuja un rectángulo que represente el margen
    pdf.add_page()

    
    # BLOQUE SUPERIOR ( Identificador )
    alto_bloque = 20

    pdf.set_draw_color(0, 0, 0)
    pdf.rect(
        x=pdf.l_margin,
        y=pdf.t_margin,
        w=85,
        h=alto_bloque
    )
    pdf.set_font("Arial", "B", 18)
    pdf.cell(0, 6, f"{datos["IdentificadorSede"]}-{numero_contrato}")
    pdf.set_font("Arial", "", 9)
    pdf.set_xy(35, 1)
    pdf.multi_cell(0, 3, f"{datos['RAM']}\nAlmacenamiento: {datos['Disco']} GB\nProcesador: {datos['Procesador']}\n{datos['Grafica']}")
    pdf.set_y(5.2)
    pdf.cell(0, 9, f"{datos['Meses']} Meses", ln=True)
    pdf.cell(0, 3, f"{datos['Nombre']} - CC {datos['Cedula']}", ln=True)
    pdf.cell(0, 3, f"{datos['Origen']}: {datos['Precio']}", ln=True)
    pdf.set_xy(140, 5.5)
    pdf.multi_cell(0, 6, "__________________________________ \n Firma Vendedor")
    

dibujar_contrato(pdf, datos, y_offset=0)
dibujar_contrato(pdf, datos, y_offset=134)

pdf_bytes = pdf.output(dest="S").encode("latin-1")
pdf_buffer = io.BytesIO(pdf_bytes)

st.success("Contrato creado y listo para la descarga ✔")
# Botón de descarga
if "descargar_pdf" not in st.session_state:
    st.session_state["descargar_pdf"] = False

if st.download_button(
    label="📥 Descargar y volver al menú principal",
    data=pdf_buffer,
    file_name=f"Contrato {datos['Origen']}.pdf",
    mime="application/pdf"
):
    st.session_state["descargar_pdf"] = True

if st.session_state["descargar_pdf"]:
    st.session_state["descargar_pdf"] = False
    
    numero_contrato = incrementar_contador()
    st.switch_page("Lobby.py")