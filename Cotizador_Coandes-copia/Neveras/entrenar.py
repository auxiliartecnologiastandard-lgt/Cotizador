import os
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor

# 1. LOCALIZAR CARPETAS (La forma más segura)
# Esto busca la carpeta donde está guardado este archivo entrenar.py
base_path = os.path.dirname(os.path.abspath(__file__))

    # Construimos las rutas exactas
ruta_csv = os.path.join(base_path, "datos_pcs.csv")
ruta_modelo = os.path.join(base_path, "modelo_pcs.pkl")

print(f"--- Iniciando Entrenamiento ---")
print(f"Buscando datos en: {ruta_csv}")

# 2. CARGAR DATOS
if not os.path.exists(ruta_csv):
    print(f"❌ ERROR: No encuentro el archivo 'datos_pcs.csv' en {base_path}")
    print("Asegúrate de que el CSV esté en la misma carpeta que este script.")
else:
    try:
        df = pd.read_csv(ruta_csv)
        
        # 3. ENTRENAMIENTO (Asegúrate de que estas columnas existan en tu CSV)
        # Ajusta los nombres de las columnas si son diferentes en tu archivo
        X = df[['ram', 'disco', 'procesador', 'grafica']] 
        y = df['precio_venta']

        modelo = RandomForestRegressor(n_estimators=100, random_state=42)
        modelo.fit(X, y)

        # 4. GUARDAR EL CEREBRO
        joblib.dump(modelo, ruta_modelo)
        
        print(f"✅ ¡ÉXITO! IA entrenada.")
        print(f"Modelo guardado en: {ruta_modelo}")

    except Exception as e:
        print(f"❌ Ocurrió un error durante el entrenamiento: {e}")