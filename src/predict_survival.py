import joblib
import pandas as pd
import re

# 1. Cargar el modelo final
# Asegúrate de que la ruta sea correcta desde la carpeta /src
try:
    model = joblib.load('../models/survival_xgboost_final.pkl')
    print("✅ Modelo cargado exitosamente.")
except FileNotFoundError:
    print("❌ Error: No se encontró el archivo del modelo en ../models/")


def clean_column_names_for_predict(df):
    """Limpia los nombres de las columnas para que coincidan con el entrenamiento de XGBoost"""
    df.columns = [re.sub(r'[<]', 'menor_a_', str(col)) for col in df.columns]
    df.columns = [re.sub(r'[>]', 'mayor_a_', str(col)) for col in df.columns]
    df.columns = [re.sub(r'[\[\]]', '', str(col)) for col in df.columns]
    df.columns = [col.replace(' ', '_').replace('+', 'plus') for col in df.columns]
    return df


def predecir_supervivencia(datos_paciente):
    """
    Recibe un diccionario con los datos del paciente y devuelve los meses estimados.
    """
    # Crear DataFrame a partir del diccionario
    df_input = pd.DataFrame([datos_paciente])

    # Asegurarse de que el orden de las columnas sea el mismo que en el entrenamiento
    # Nota: Aquí deberías incluir todas las columnas que resultaron del get_dummies
    # Para simplificar, este script asume que df_input ya tiene la estructura de X_train

    df_input = clean_column_names_for_predict(df_input)

    # Realizar la predicción
    prediccion = model.predict(df_input)
    return prediccion[0]


# --- EJEMPLO DE USO ---
# Este diccionario debe contener las mismas columnas (dummies) que usaste en X_train
ejemplo_paciente = {
    'Event': 1,
    'Has_Surgery': 1,
    'Income_Level_70,000_-_74,999': 1,  # Ejemplo de columna dummy
    'Stage_Consolidated_Localized': 1,
    # ... añadir el resto de columnas necesarias según tu X_train.columns
}

# meses = predecir_supervivencia(ejemplo_paciente)
# print(f"Estimación de supervivencia: {meses:.2f} meses")