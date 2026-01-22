# Reporte de Resultados: Modelo Predictivo de Supervivencia

## Conclusión General del EDA: **El Peso de los Factores No Clínicos**

El análisis exploratorio revela que la supervivencia de los pacientes en este dataset no es solo un fenómeno biológico, sino también estructural. Si bien la agresividad del cáncer (etapa) dicta el pronóstico base, el entorno socioeconómico actúa como un modulador crítico del tiempo de vida restante.

## Las tres claves del estudio:

1. **La "Ventana de Oportunidad" Económica:** El nivel de ingresos es un factor determinante de supervivencia principalmente en etapas donde el tratamiento médico tiene mayor potencial curativo. Esto sugiere que las barreras económicas afectan el acceso a tratamientos de alta complejidad o seguimiento intensivo.


2. **Inequidad Persistente** El hecho de que el ingreso sea significativo incluso dentro de la misma etapa clínica (p < 0.05 en el modelo de Cox) confirma que, ante diagnósticos idénticos, los pacientes con menos recursos enfrentan un riesgo de mortalidad mayor.


3. **Prioridad de Intervención:** Los datos justifican que los modelos predictivos futuros no pueden ignorar las variables sociales. Para mejorar la supervivencia global, no solo se requieren mejores fármacos, sino políticas que mitiguen la brecha de acceso según el nivel de ingresos.


## Resumen Ejecutivo:

- Tras la limpieza de datos y la ingeniería de características (incorporando el estado vital y el historial de cirugía), se desarrollaron dos modelos de regresión. El modelo XGBoost resultó ser el más preciso, logrando reducir el error de predicción a 16.27 meses.

## Comparativa de Modelos:

![img_1.png](Comparacion_de_modelos.png)

## Factores Determinantes (Feature Importance):
El análisis de importancia de variables reveló que la supervivencia no depende de un solo factor, sino de una combinación crítica:

- **Estado Vital (Event)** El predictor más fuerte del modelo.
- **Clínica:** Las etapas Localized y Regional muestran un impacto positivo significativo frente a la etapa Distante.
- **Nivel Socioeconómico:** El nivel de ingresos (especialmente en los rangos de $70k-$90k) tiene una importancia superior a la cirugía aislada, sugiriendo que el acceso económico influye directamente en el pronóstico a largo plazo.

## Análisis de Escenarios (Predicciones Reales):
Utilizando el modelo final, se simularon tres perfiles de pacientes para validar la coherencia del sistema:

![img.png](Comparacion.png)

## Conclusión del Análisis Predictivo

El desarrollo de este modelo permitió cuantificar la brecha en el pronóstico de supervivencia de cáncer de pulmón basándose en la intersección de factores clínicos y socioeconómicos.


- **Eficacia del Modelo:** El uso de XGBoost permitió capturar interacciones no lineales que modelos lineales tradicionales pasarían por alto, logrando una precisión del 30% en un fenómeno altamente estocástico como es la supervivencia oncológica.


- **Determinantes de Salud:** Se observó que el "Efecto Cirugía" es interdependiente del nivel de ingresos. Mientras que la etapa clínica dicta la biología de la enfermedad, el nivel de ingresos actúa como un facilitador del acceso a tratamientos oportunos, lo que se refleja en una variación de hasta 52 meses entre los escenarios extremos analizados.


- **Recomendación:** Para futuras iteraciones, se recomienda incluir variables de co-morbilidades y biomarcadores genéticos, los cuales podrían reducir el MAE residual de 16 meses y mejorar la personalización de las predicciones.

## ⚠️ Consideraciones sobre el Modelo
* **Variables omitidas:** Factores como la **Edad** y el **Género** fueron evaluados durante el EDA, pero no se incluyeron en el modelo de producción final para evitar el ruido estadístico, ya que la **Etapa del Cáncer** demostró ser el predictor con mayor relevancia clínica y estadística.