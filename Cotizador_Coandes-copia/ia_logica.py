import streamlit as st
import google.generativeai as genai
from PIL import Image
import json

def analizar_con_ia(lista_imagenes, precio_base, tipo_producto):
    try:
        genai.configure(api_key=st.secrets["GEMINI_KEY"])
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        imagenes_listas = []
        for img_data in lista_imagenes:
            if hasattr(img_data, 'read'):
                img_data.seek(0)
                imagenes_listas.append(Image.open(img_data))
            else:
                imagenes_listas.append(img_data)
        
        prompt = "Analiza estas 3 fotos de un producto y detecta daños. Responde SOLO en JSON: {\"categoria\": \"...\", \"porcentaje\": 0.0, \"motivo\": \"...\"}"
        
        response = model.generate_content([prompt] + imagenes_listas)
        
        # Limpieza de JSON
        texto = response.text
        inicio = texto.find('{')
        fin = texto.rfind('}') + 1
        return {**json.loads(texto[inicio:fin]), "exito": True}
    except Exception as e:
        return {"exito": False, "error": str(e)}