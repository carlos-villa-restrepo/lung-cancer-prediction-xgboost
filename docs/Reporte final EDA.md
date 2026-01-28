# Reporte de Resultados: Modelo Predictivo de Supervivencia

## Conclusión General del EDA: Biología y Entorno

El análisis exploratorio final confirma que la supervivencia es un fenómeno multifactorial. Tras la ingeniería de variables, descubrimos que la Era Médica (diagnósticos post-2010) actúa como un catalizador positivo, probablemente debido a la adopción de terapias dirigidas e inmunoterapia.

### **Métricas Clave del Dataset Procesado**

| Dimensión | Variable(s) Clave | Hallazgo Crítico / Impacto |
| :--- | :--- | :--- |
| **Temporal** | `Year_of_diagnosis` | **Evolución Médica:** El diagnóstico reciente actúa como un factor de protección, reflejando mejoras en protocolos clínicos. |
| **Socioeconómica** | `Income_Numeric` | **Determinante de Salud:** El nivel de ingresos es un modulador crítico que facilita el acceso a tratamientos de alta complejidad. |
| **Clínica Base** | `Stage_Rank`, `Tumor_Size_Clean` | **Estratificación de Riesgo:** Son los predictores primarios que definen la agresividad biológica y el pronóstico base. |
| **Carga Tumoral** | `Total_Tumors_Count`, `Is_Multicentric` | **Complejidad Sistémica:** Permite al modelo ajustar la supervivencia basándose en la dispersión del cáncer en el organismo. |
| **Ingeniería Avanzada** | `Tumor_Age_Ratio` | **Cinética del Cáncer:** Proporciona una métrica de velocidad de crecimiento que refina la precisión en etapas intermedias. |

## Resumen Ejecutivo del Modelado

Se evolucionó de un modelo base a un XGBoost con Interacciones que permite entender cómo la quimioterapia afecta de manera distinta a cada etapa. Se logró un $R^2$ de 0.423, superando el 30% del modelo inicial.

###  **Comparativa Final de Modelos**

| Modelo | $R^2$ Score | MAE (Meses) | Estado |
| :--- | :---: | :---: | :--- |
| Random Forest (Base) | 0.320 | 20.00 | Superado |
| **XGBoost (Optimizado)** | **0.423** | **14.22** | **Ganador** |

## Factores Determinantes (Feature Importance)
El modelo final prioriza las variables que realmente "mueven la aguja" en el pronóstico:

- **Etapa del Cáncer (Stage_Rank):** El factor de mayor peso clínico.

- **Interacción Etapa-Quimio:** La variable que define la recomendación de tratamiento.

- **Tamaño del Tumor:** Crítico para definir el beneficio marginal en etapas tempranas.

- **Era de Diagnóstico:** Refleja la evolución del sistema de salud.

## Motor de Recomendación y Análisis de Sensibilidad
La gran innovación de esta entrega es la capacidad de simular escenarios clínicos para determinar el beneficio de la quimioterapia por etapa.

### **Beneficio de Quimioterapia por Escenario**

| Etapa | Beneficio Máximo | Punto de Inflexión | Recomendación |
| :--- | :---: | :---: | :--- |
| **Etapa 1** | ~30% | < 20mm | Alto impacto preventivo |
| **Etapa 2** | **~23%** | **40mm** | **Zona crítica de decisión** |
| **Etapa 3** | ~23% | Estable | Protocolo estándar |
| **Etapa 4** | ~23% | Inmediato | Tratamiento esencial |

## Conclusión del Análisis Predictivo

- **Eficacia:** El modelo es excepcionalmente preciso en casos de corto plazo, donde el 50% de las predicciones tienen un error inferior a 6 meses.

- **Determinantes:** Se validó que el "Efecto Tratamiento" no es lineal; su éxito depende de la interacción directa con la etapa clínica detectada.

- **Recomendación:** El sistema está listo para actuar como una herramienta de segunda opinión médica, ayudando a visualizar el beneficio estadístico de la quimioterapia antes de iniciar ciclos agresivos.