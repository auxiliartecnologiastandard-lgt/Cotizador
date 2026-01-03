import streamlit as st
import google.generativeai as genai
from PIL import Image
import json

def analizar_con_ia(lista_imagenes, precio_base, tipo_producto):
    try:
        # 1. Configuración forzando la versión estable
        genai.configure(api_key=st.secrets["GEMINI_KEY"])
        
        # Intentamos con el nombre técnico completo
        model = genai.GenerativeModel('models/gemini-1.5-flash')
        
        imagenes_listas = []
        for img_data in lista_imagenes:
            if hasattr(img_data, 'read'):
                img_data.seek(0)
                imagenes_listas.append(Image.open(img_data))
            else:
                imagenes_listas.append(img_data)
        
        prompt = f"""
        Actúa como perito técnico de {tipo_producto}. 
        Analiza las fotos y detecta daños.
        Responde estrictamente en este formato JSON:
        {{
            "categoria": "NUEVO, LEVE, MODERADO o GRAVE",
            "porcentaje": 0.0,
            "motivo": "razón corta"
        }}
        """

        # 2. Llamada al modelo
        response = model.generate_content([prompt] + imagenes_listas)

        # 3. Limpieza de respuesta (A veces la IA devuelve texto extra)
        res_text = response.text
        start = res_text.find('{')
        end = res_text.rfind('}') + 1
        
        if start == -1:
            return {"exito": False, "error": "La IA no devolvió un formato válido."}
            
        datos = json.loads(res_text[start:end])
        
        return {
            "exito": True,
            "categoria": datos.get("categoria", "DESCONOCIDO"),
            "porcentaje": float(datos.get("porcentaje", 0)),
            "motivo": datos.get("motivo", "Procesado")
        }

    except Exception as e:
        # Si esto falla, el problema es la API KEY o la región
        return {"exito": False, "error": f"Error detallado: {str(e)}"}