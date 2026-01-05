import streamlit as st
import google.generativeai as genai
from PIL import Image
import json

def analizar_con_ia(lista_imagenes, precio_base, tipo_producto):
    try:
        genai.configure(api_key=st.secrets["GEMINI_KEY"])
        
        # 1. Usamos la versión 2.0 flash (Más rápida y con más cuota disponible)
        model = genai.GenerativeModel('gemini-2.0-flash') 
        
        # 2. Codigo para cuando la IA reciba las imagenes
        imagenes_listas = []
        for img_data in lista_imagenes:
            if hasattr(img_data, 'read'):
                img_data.seek(0)
                img = Image.open(img_data).convert('RGB')
                # 2.1 REDUCCIÓN DE IMAGEN: Fundamental para no agotar la cuota de tokens
                img.thumbnail((512, 512)) 
                imagenes_listas.append(img)
        
        # 3. Prompt simplificado para ahorrar recursos
        prompt = "Analiza el estado de este producto. Responde SOLO JSON: {\"categoria\": \"NUEVO/LEVE/MODERADO/GRAVE\", \"porcentaje\": 0.1, \"motivo\": \"...\"}"

        response = model.generate_content(
            [prompt] + imagenes_listas,
            generation_config={"temperature": 0.1}
        )

        texto = response.text
        start = texto.find('{')
        end = texto.rfind('}') + 1
        datos = json.loads(texto[start:end])
        
        return {
            "exito": True,
            "categoria": datos.get("categoria", "MODERADO"),
            "porcentaje": float(datos.get("porcentaje", 0)),
            "motivo": datos.get("motivo", "Análisis completado")
        }

    except Exception as e:
        return {"exito": False, "error": f"Error: {str(e)}"}