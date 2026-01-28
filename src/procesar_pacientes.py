import pandas as pd
import numpy as np
import joblib
import os

# Rutas seguras
base_path = os.path.dirname(os.path.abspath(__file__))
path_xgboost = os.path.join(base_path, "..", "models", "xgboost_model.pkl")
path_cox = os.path.join(base_path, "..", "models", "cox_model.pkl")

# Carga de modelos al inicio (Evita NameError)
try:
    modelo_survival = joblib.load(path_xgboost)
    modelo_treatment = joblib.load(path_cox)
except:
    modelo_survival = None
    modelo_treatment = None


def procesar_lista_pacientes(datos_lista):
    df = pd.DataFrame(datos_lista)

    # Simulación de predicciones (Aquí conectas tus modelos reales)
    df['paciente_id'] = [f"ID-{i + 1:03d}" for i in range(len(df))]
    df['expectativa_total_meses'] = np.random.uniform(15, 110, len(df))
    df['ganancia_meses'] = np.random.uniform(1, 20, len(df))
    df['recomendacion'] = df['ganancia_meses'].apply(lambda x: "SUGERIR_QUIMIO" if x > 7 else "OBSERVACIÓN")

    return df