import streamlit as st
import google.generativeai as genai
from PIL import Image
import json

def analizar_con_ia(lista_imagenes, precio_base, tipo_producto):
    try:
        # 1. Configuración limpia
        genai.configure(api_key=st.secrets["GEMINI_KEY"])
        
        # 2. Configuración de seguridad (para evitar bloqueos por error)
        safety_settings = [
            {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
        ]
        
        # 3. Probamos con el nombre corto del modelo
        model = genai.GenerativeModel(
            model_name='gemini-1.5-flash',
            safety_settings=safety_settings
        )
        
        # 4. Preparar imágenes
        imagenes_listas = []
        for img_data in lista_imagenes:
            if hasattr(img_data, 'read'):
                img_data.seek(0)
                imagenes_listas.append(Image.open(img_data))
            else:
                imagenes_listas.append(img_data)
        
        if not imagenes_listas:
            return {"exito": False, "error": "No se recibieron imágenes"}

        # 5. El Prompt
        prompt = f"Analiza estas fotos de {tipo_producto}. Detecta daños. Responde SOLO un JSON con: 'categoria' (NUEVO, LEVE, MODERADO, GRAVE), 'porcentaje' (0.0 a 1.0) y 'motivo'."

        # 6. Llamada Directa
        response = model.generate_content([prompt] + imagenes_listas)

        # 7. Procesar respuesta
        res_text = response.text
        start = res_text.find('{')
        end = res_text.rfind('}') + 1
        datos = json.loads(res_text[start:end])
        
        return {
            "exito": True,
            "categoria": datos.get("categoria", "MODERADO"),
            "porcentaje": float(datos.get("porcentaje", 0)),
            "motivo": datos.get("motivo", "Procesado")
        }

    except Exception as e:
        # Si esto vuelve a dar 404, vamos a imprimir qué modelos ve la llave
        return {"exito": False, "error": f"Error persistente: {str(e)}"}