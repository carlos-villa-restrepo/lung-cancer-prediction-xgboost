# 🏥 Informe Ejecutivo: Análisis de Supervivencia Oncológica
**Fecha de generación:** 26/01/2026 14:15
**Versión del modelo:** XGBoost Tuned + Cox Proportional Hazards

---

## 📊 Resumen de Resultados
A continuación se presentan las métricas clave obtenidas tras el análisis del lote de pacientes:

| Métrica | Valor |
| :--- | :--- |
| **Total de Pacientes Analizados** | 30 |
| **Pacientes con Recomendación de Quimioterapia** | 3 |
| **Promedio de Vida Ganada (Meses)** | 0.48 meses |

---

## 📈 Visualización de Impacto Clínico
El siguiente gráfico muestra la ganancia estimada de meses de vida para cada paciente analizado. Las barras verdes indican un beneficio clínico positivo.

![Gráfico de Impacto](grafico_impacto.png)

*Figura 1: Comparativa de meses ganados por paciente según el modelo de supervivencia.*

---

## 📑 Detalle de Pacientes Proprocesados
Esta tabla contiene los datos técnicos utilizados para la toma de decisiones:

|   paciente_id |   vida_base_meses | reduccion_riesgo_pct   |   ganancia_meses |   expectativa_total_meses | recomendacion   |
|--------------:|------------------:|:-----------------------|-----------------:|--------------------------:|:----------------|
|             1 |             32.36 | -36.30%                |             0    |                     32.36 | ESTANDAR        |
|             2 |             49.63 | -0.51%                 |             0    |                     49.63 | ESTANDAR        |
|             3 |             54.43 | -2.28%                 |             0    |                     54.43 | ESTANDAR        |
|             4 |             54.32 | -19.61%                |             0    |                     54.32 | ESTANDAR        |
|             5 |             59.65 | -8.11%                 |             0    |                     59.65 | ESTANDAR        |
|             6 |             20.52 | -16.87%                |             0    |                     20.52 | ESTANDAR        |
|             7 |             20.58 | -35.54%                |             0    |                     20.58 | ESTANDAR        |
|             8 |             59.12 | -1.75%                 |             0    |                     59.12 | ESTANDAR        |
|             9 |             23.34 | +18.87%                |             4.4  |                     27.74 | SUGERIR_QUIMIO  |
|            10 |             79.95 | -0.97%                 |             0    |                     79.95 | ESTANDAR        |
|            11 |             36.13 | -6.96%                 |             0    |                     36.13 | ESTANDAR        |
|            12 |             28.22 | -37.74%                |             0    |                     28.22 | ESTANDAR        |
|            13 |             14.78 | +48.75%                |             7.2  |                     21.98 | SUGERIR_QUIMIO  |
|            14 |             63.87 | -7.18%                 |             0    |                     63.87 | ESTANDAR        |
|            15 |             46.3  | -4.31%                 |             0    |                     46.3  | ESTANDAR        |
|            16 |             61.44 | -0.15%                 |             0    |                     61.44 | ESTANDAR        |
|            17 |             44.33 | -15.73%                |             0    |                     44.33 | ESTANDAR        |
|            18 |             69.87 | -1.32%                 |             0    |                     69.87 | ESTANDAR        |
|            19 |             27.67 | -1.07%                 |             0    |                     27.67 | ESTANDAR        |
|            20 |             22.79 | -2.91%                 |             0    |                     22.79 | ESTANDAR        |
|            21 |             52.93 | -3.07%                 |             0    |                     52.93 | ESTANDAR        |
|            22 |             11.53 | -21.17%                |             0    |                     11.53 | ESTANDAR        |
|            23 |             60.97 | -4.95%                 |             0    |                     60.97 | ESTANDAR        |
|            24 |             48.05 | -1.87%                 |             0    |                     48.05 | ESTANDAR        |
|            25 |             14.58 | -91.61%                |             0    |                     14.58 | ESTANDAR        |
|            26 |             54.56 | -2.06%                 |             0    |                     54.56 | ESTANDAR        |
|            27 |             28.14 | -12.56%                |             0    |                     28.14 | ESTANDAR        |
|            28 |             22.7  | -5.68%                 |             0    |                     22.7  | ESTANDAR        |
|            29 |             13.68 | +21.34%                |             2.92 |                     16.6  | SUGERIR_QUIMIO  |
|            30 |             62.24 | -15.38%                |             0    |                     62.24 | ESTANDAR        |

---

## 🧠 Conclusiones del Modelo
1. **Factor Determinante:** Se confirma que el `Stage_Rank` (Etapa del cáncer) es la variable con mayor peso en la predicción de supervivencia base.
2. **Eficacia Terapéutica:** Los pacientes en Etapa IV muestran, proporcionalmente, la mayor variabilidad en respuesta, validando la necesidad de un análisis personalizado.
3. **Optimización:** El uso de un `XGBRegressor` sintonizado redujo el error medio (MAE) a **18.47 meses**, mejorando la precisión del pronóstico base.

---
*Generado automáticamente por el Sistema de Predicción ML-G1.*
