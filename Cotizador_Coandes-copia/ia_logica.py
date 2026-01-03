import streamlit as st
import google.generativeai as genai
from PIL import Image
import json

def analizar_con_ia(lista_imagenes, precio_base, tipo_producto):
    try:
        genai.configure(api_key=st.secrets["GEMINI_KEY"])
        
        # CAMBIO CLAVE: Usamos el nombre técnico de producción v1
        # Intentamos con la versión "8b" que es más ligera y compatible
        model = genai.GenerativeModel('gemini-1.5-flash-8b') 
        
        imagenes_listas = []
        for img_data in lista_imagenes:
            if hasattr(img_data, 'read'):
                img_data.seek(0)
                img = Image.open(img_data).convert('RGB')
                imagenes_listas.append(img)
        
        prompt = "Analiza estas fotos y detecta daños. Responde solo JSON: {\"categoria\": \"...\", \"porcentaje\": 0.0, \"motivo\": \"...\"}"
        
        # Forzamos que la respuesta no use la versión beta
        response = model.generate_content(
            [prompt] + imagenes_listas,
            generation_config={"temperature": 0.1}
        )
        
        texto = response.text
        start = texto.find('{')
        end = texto.rfind('}') + 1
        return {**json.loads(texto[start:end]), "exito": True}

    except Exception as e:
        # Si esto vuelve a dar 404, el problema es la región de tu API KEY
        return {"exito": False, "error": f"Fallo crítico: {str(e)}"}