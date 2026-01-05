import streamlit as st
import google.generativeai as genai
from PIL import Image
import json

def analizar_con_ia(lista_imagenes, precio_base, tipo_producto):
    try:
        genai.configure(api_key=st.secrets["GEMINI_KEY"])
        
        # USAMOS EL MODELO QUE TU CUENTA SÍ VE (Gemini 2.0 Flash)
        # Es mucho mejor que el 1.5 y está disponible para ti
        model = genai.GenerativeModel('gemini-1.0-pro-vision') 
        
        imagenes_listas = []
        for img_data in lista_imagenes:
            if hasattr(img_data, 'read'):
                img_data.seek(0)
                img = Image.open(img_data).convert('RGB')
                img.thumbnail((800, 800)) 
                imagenes_listas.append(img)
        
        prompt = f"""
        Actúa como perito técnico. Analiza estas fotos de {tipo_producto}.
        Detecta daños o estado de uso.
        Responde exclusivamente en JSON:
        {{
            "categoria": "NUEVO, LEVE, MODERADO o GRAVE",
            "porcentaje": 0.1,
            "motivo": "razón del estado"
        }}
        """

        # Generación de contenido
        response = model.generate_content([prompt] + imagenes_listas)

        # Procesamiento del JSON
        texto = response.text
        start = texto.find('{')
        end = texto.rfind('}') + 1
        datos = json.loads(texto[start:end])
        
        return {
            "exito": True,
            "categoria": datos.get("categoria", "MODERADO"),
            "porcentaje": float(datos.get("porcentaje", 0)),
            "motivo": datos.get("motivo", "Analizado con Gemini 2.0")
        }

    except Exception as e:
        return {"exito": False, "error": f"Error con Gemini 2.0: {str(e)}"}