import streamlit as st
import google.generativeai as genai
from PIL import Image
import json

def analizar_con_ia(lista_imagenes, precio_base, tipo_producto):
    try:
        # 1. Forzamos la configuración a la versión estable V1
        genai.configure(api_key=st.secrets["GEMINI_KEY"], transport='rest')
        
        # 2. Usamos el modelo más básico y compatible
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        imagenes_listas = []
        for img_data in lista_imagenes:
            if hasattr(img_data, 'read'):
                img_data.seek(0)
                imagenes_listas.append(Image.open(img_data).convert('RGB'))
        
        prompt = f"Analiza estas fotos de {tipo_producto}. Responde solo JSON: {{\"categoria\": \"LEVE\", \"porcentaje\": 0.1, \"motivo\": \"...\"}}"

        # 3. Llamada con configuración de generación explícita
        response = model.generate_content(
            contents=[prompt] + imagenes_listas
        )

        # 4. Procesar con seguridad
        texto = response.text
        start = texto.find('{')
        end = texto.rfind('}') + 1
        return {**json.loads(texto[start:end]), "exito": True}

    except Exception as e:
        # ESTO ES CLAVE: Si vuelve a fallar, vamos a pedirle a la API que nos diga
        # qué modelos SÍ tiene permitidos tu cuenta.
        modelos_disponibles = [m.name for m in genai.list_models()]
        return {
            "exito": False, 
            "error": f"Error: {str(e)}. Modelos que ve tu cuenta: {modelos_disponibles}"
        }