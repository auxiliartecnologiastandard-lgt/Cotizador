import streamlit as st
from google import genai
import json

def analizar_con_ia(lista_imagenes, precio_base, tipo_producto):
    """
    Cerebro universal de peritaje para Coandes con salida JSON estricta.
    """
    try:
        # 1. Configuración del cliente
        client = genai.Client(api_key=st.secrets["GEMINI_KEY"])
        
        # 2. Instrucción con formato JSON (Más difícil de romper)
        prompt = f"""
        Actúa como un perito técnico experto en la compra de {tipo_producto}.
        Analiza estas 3 imágenes en busca de fallas, desgaste o daños.
        
        Responde EXCLUSIVAMENTE en formato JSON con la siguiente estructura:
        {{
            "categoria": "NUEVO, LEVE, MODERADO o GRAVE",
            "porcentaje": valor_decimal_entre_0_y_1,
            "motivo": "explicación breve"
        }}

        REGLAS:
        - NUEVO: 0.0
        - LEVE: 0.10 a 0.15
        - MODERADO: 0.25 a 0.40
        - GRAVE: 0.50 a 0.80
        """

        # 3. Llamada al modelo
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=[prompt, *lista_imagenes]
        )

        # 4. Limpieza de la respuesta (Quitamos posibles marcas de markdown ```json)
        texto = response.text.replace("```json", "").replace("```", "").strip()
        datos = json.loads(texto) # Convertimos el texto en un diccionario real
        
        # 5. Devolvemos el resultado formateado
        return {
            "exito": True,
            "categoria": datos.get("categoria", "DESCONOCIDO"),
            "porcentaje": float(datos.get("porcentaje", 0)),
            "motivo": datos.get("motivo", "Sin motivo especificado")
        }

    except Exception as e:
        # Si algo falla (JSON mal formado o conexión)
        return {"exito": False, "error": str(e)}