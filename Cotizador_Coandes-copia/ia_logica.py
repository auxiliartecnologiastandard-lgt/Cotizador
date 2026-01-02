import streamlit as st
from google import genai

def analizar_con_ia(lista_imagenes, precio_base, tipo_producto):
    """
    Cerebro universal de peritaje para Coandes.
    Recibe: lista de fotos, precio inicial y nombre del producto (PC, Nevera, etc.)
    Devuelve: Diccionario con categoría, descuento, monto reducido y motivo.
    """
    try:
        # 1. Configuración del cliente (Usa el Secret configurado en Streamlit Cloud)
        client = genai.Client(api_key=st.secrets["GEMINI_KEY"])
        
        # 2. Instrucción dinámica según el producto
        prompt = f"""
        Actúa como un perito técnico experto en la compra de {tipo_producto}.
        Analiza detalladamente estas 3 imágenes en busca de fallas, desgaste, golpes o suciedad.
        
        REGLAS DE CLASIFICACIÓN:
        - NUEVO: Sin detalles, 0% descuento.
        - LEVE: Rayones mínimos o suciedad, 10-15% descuento.
        - MODERADO: Abolladuras, teclas/piezas faltantes o manchas, 25-40% descuento.
        - GRAVE: Daño estructural, óxido profundo o fallas críticas, 50-80% descuento.
        
        FORMATO DE RESPUESTA OBLIGATORIO:
        CATEGORIA | PORCENTAJE_DECIMAL | JUSTIFICACION_CORTA
        
        Ejemplo: MODERADO | 0.30 | Pantalla con píxeles muertos y bordes desgastados.
        """

        # 3. Llamada al modelo Gemini 1.5 Flash (Optimizado para visión y velocidad)
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=[prompt, *lista_imagenes]
        )

        # 4. Limpieza y procesamiento de la respuesta
        respuesta_texto = response.text.strip()
        partes = respuesta_texto.split("|")
        
        if len(partes) == 3:
            categoria = partes[0].strip()
            porcentaje = float(partes[1].strip())
            motivo = partes[2].strip()
            
            # Cálculo del impacto financiero
            dinero_reducido = precio_base * porcentaje
            
            return {
                "exito": True,
                "categoria": categoria,
                "porcentaje": porcentaje,
                "dinero_reducido": dinero_reducido,
                "motivo": motivo
            }
        else:
            return {"exito": False, "error": "Formato de respuesta IA inválido."}

    except Exception as e:
        # Manejo de errores de cuota o conexión
        error_msg = str(e)
        if "429" in error_msg:
            return {"exito": False, "error": "Límite de la IA alcanzado. Espera 60 segundos."}
        return {"exito": False, "error": f"Error técnico: {error_msg}"}