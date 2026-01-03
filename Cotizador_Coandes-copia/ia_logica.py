import streamlit as st
from google import genai
from PIL import Image
import json
import io

def analizar_con_ia(lista_imagenes, precio_base, tipo_producto):
    """
    Cerebro universal de peritaje para Coandes con salida JSON estricta.
    """
    try:
        # 1. Configuración del cliente
        client = genai.Client(api_key=st.secrets["GEMINI_KEY"])
        
        # --- PROCESAMIENTO DE IMÁGENES ---
        imagenes_listas = []
        for img_data in lista_imagenes:
            try:
                if hasattr(img_data, 'read'):
                    img_data.seek(0)
                    img = Image.open(img_data)
                else:
                    img = img_data
                imagenes_listas.append(img)
            except Exception as e_img:
                return {"exito": False, "error": f"Error en formato de imagen: {e_img}"}
        
        # 2. Instrucción con formato JSON
        prompt = f"""
        Actúa como un perito técnico experto en la compra de {tipo_producto}.
        Analiza detalladamente estas 3 imágenes en busca de fallas, desgaste, golpes o suciedad.
        
        Responde EXCLUSIVAMENTE en formato JSON con la siguiente estructura:
        {{
            "categoria": "NUEVO, LEVE, MODERADO o GRAVE",
            "porcentaje": valor_decimal_entre_0_y_1,
            "motivo": "explicación corta del daño"
        }}

        REGLAS DE CLASIFICACIÓN:
        - NUEVO: 0.0
        - LEVE: 0.10 a 0.15
        - MODERADO: 0.25 a 0.40
        - GRAVE: 0.50 a 0.80
        """

        # 3. LLAMADA CORREGIDA (Sintaxis exacta para el SDK nuevo)
        # Se eliminó la instancia redundante de GenerativeModel que causaba el error de paréntesis
        response = client.models.generate_content(
            model='gemini-1.5-flash-latest',
            contents=[prompt, *imagenes_listas]
        )

        # 4. Limpieza y procesamiento de la respuesta JSON
        texto_limpio = response.text.replace("```json", "").replace("```", "").strip()
        datos = json.loads(texto_limpio)
        
        # 5. Devolvemos el resultado formateado
        return {
            "exito": True,
            "categoria": datos.get("categoria", "DESCONOCIDO"),
            "porcentaje": float(datos.get("porcentaje", 0)),
            "motivo": datos.get("motivo", "Sin motivo especificado")
        }

    except Exception as e:
        return {"exito": False, "error": f"Error técnico: {str(e)}"}