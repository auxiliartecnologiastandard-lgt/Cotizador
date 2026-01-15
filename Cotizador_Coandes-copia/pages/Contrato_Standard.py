import streamlit as st
from fpdf import FPDF

# --- Datos de ejemplo ---
datos = {}

# Streamlit: Selección de opciones
datos["Marca"] = st.selectbox("Selecciona la marca", [1,2,3,4,5,6,7,8,9,10,11])
datos["RAM"] = st.selectbox("Selecciona la RAM", [2,4,6,7,12,16,32,64])
datos["Procesador"] = st.selectbox("Selecciona el procesador", [5, 5.000001, 5.0000001, 5.00000001, 15, 30, 70, 120])

# --- Convertir números a texto ---
# Marca
if datos["Marca"] == 1:
    datos["Marca"] = "WINDOWS"
elif datos["Marca"] == 2:
    datos["Marca"] = "Koorui"
elif datos["Marca"] == 3:
    datos["Marca"] = "Acer"
elif datos["Marca"] == 4:
    datos["Marca"] = "Hewlettpacka"
elif datos["Marca"] == 5:
    datos["Marca"] = "VICTUS"
elif datos["Marca"] == 6:
    datos["Marca"] = "Asus"
elif datos["Marca"] == 7:
    datos["Marca"] = "SONY"
elif datos["Marca"] == 8:
    datos["Marca"] = "Samsung"
elif datos["Marca"] == 9:
    datos["Marca"] = "Dell"
elif datos["Marca"] == 10:
    datos["Marca"] = "LENOVO"
elif datos["Marca"] == 11:
    datos["Marca"] = "Apple"

# RAM
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

# Procesador
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

# --- Botón para generar PDF ---
if st.button("Generar PDF"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Resumen del Equipo", ln=True, align="C")
    pdf.ln(10)

    pdf.set_font("Arial", "", 12)
    for key, value in datos.items():
        pdf.cell(0, 10, f"{key}: {value}", ln=True)

    pdf_file = "resumen_equipo.pdf"
    pdf.output(pdf_file)

    # Descargar PDF en Streamlit
    with open(pdf_file, "rb") as f:
        st.download_button(
            label="Descargar PDF",
            data=f,
            file_name=pdf_file,
            mime="application/pdf"
        )

    st.success("PDF generado correctamente ✅")

    