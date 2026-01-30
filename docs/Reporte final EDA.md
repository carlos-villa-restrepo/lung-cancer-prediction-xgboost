# Análisis Exploratorio y Modelado Predictivo de Supervivencia en Cáncer de Pulmón

---

1. **Contexto y Motivación**

El cáncer de pulmón es una de las principales causas de mortalidad a nivel mundial. Comprender los factores asociados a la supervivencia de los pacientes y cómo estos interactúan con distintos tratamientos es clave para apoyar el análisis clínico y la investigación en salud.

Este proyecto aborda el problema desde una perspectiva de Data Science aplicada, combinando análisis exploratorio, modelos predictivos tradicionales y técnicas de Survival Analysis, con el objetivo de extraer patrones relevantes y explorar el riesgo de mortalidad a lo largo del tiempo.

---

⚠️ **Nota importante:** Este proyecto es de carácter académico y exploratorio. Los resultados reflejan asociaciones estadísticas aprendidas por los modelos y no implican relaciones causales ni deben interpretarse como recomendaciones clínicas.

---

2. **Objetivos del Proyecto**
- Objetivo general

  - Analizar la supervivencia de pacientes con cáncer de pulmón a partir de variables clínicas, demográficas y temporales, utilizando enfoques de Data Science y Machine Learning.

  - Objetivos específicos

  - Realizar un Análisis Exploratorio de Datos (EDA) con énfasis clínico y estadístico.

  - Identificar variables e interacciones asociadas a diferencias significativas en supervivencia.

  - Comparar modelos de Machine Learning tradicionales para la predicción de tiempo de supervivencia (enfoque comparativo).

  - Aplicar técnicas de Survival Analysis para estimar riesgo y curvas de supervivencia.

  - Explorar escenarios y análisis de sensibilidad del tratamiento desde una perspectiva predictiva.
  
---

3. **Dataset**

El dataset contiene información clínica anonimizada de pacientes diagnosticados con cáncer de pulmón.

- Incluye variables como:

    - Edad y características demográficas.

    - Estado funcional y variables socioeconómicas.

    - Tipo, tamaño y estadio del tumor.

    - Información de tratamiento.

    - Tiempo de seguimiento.

    - Indicador de evento (fallecimiento) y censura.

La presencia de datos censurados motiva el uso de técnicas específicas de survival analysis.

---

4. Estructura del Proyecto
```text
├── 01_eda_elius.ipynb              # Análisis exploratorio y síntesis de hallazgos
├── 02-00_ML_prediccion_elius.ipynb  # Modelos de ML para predicción de supervivencia
├── 03-00_ML_survival_elius.ipynb    # Survival analysis y análisis de escenarios
├── requirements.txt                # Librerías necesarias
└── README.md                       # Documentación del proyecto
```
   ---
5. Metodología

-  **5.1 Análisis Exploratorio de Datos (EDA)**

    - Análisis univariado y bivariado.

    - Visualizaciones clínicas.

    - Curvas de Kaplan–Meier.

    - Tests estadísticos (log-rank, chi-cuadrado).

    - Síntesis de variables relevantes y posibles interacciones.


-  **5.2 Machine Learning (Enfoque comparativo)**


- Modelos evaluados:

    - Random Forest Regressor.

    - XGBoost Regressor.

    
- Métricas:

  - MAE.

  - RMSE.

  - R².

Este enfoque se utiliza con fines comparativos y exploratorios, ya que los modelos de regresión no manejan explícitamente la censura de datos.

- **5.3 Survival Analysis y Riesgo**

  - Modelos de supervivencia para:

  - Estimación de riesgo individual.

  - Curvas de supervivencia por subgrupos.

  - Análisis de escenarios y sensibilidad del tratamiento.
---
6. **Resultados Principales**

   - La supervivencia se ve influenciada por factores clínicos, temporales y socioeconómicos.

   - Variables como la etapa clínica y el tamaño tumoral emergen como predictores dominantes.

   - Los modelos de ML tradicionales muestran un desempeño razonable, pero presentan limitaciones ante datos censurados.

   - Los modelos de supervivencia permiten una representación más realista del riesgo a lo largo del tiempo.
---

7. **Limitaciones**

   - Dataset de tamaño limitado.

   - Posibles sesgos en variables clínicas y socioeconómicas.

   - Ausencia de validación externa.

   - No se realiza inferencia causal ni ajuste por confounding avanzado.
---

8. **Próximos Pasos**

   - Validar supuestos de riesgos proporcionales en modelos de Cox.

   - Incorporar métricas específicas de survival analysis (C-index).

   - Explorar modelos avanzados (Random Survival Forests, Deep Survival Models).

    - Mejorar interpretabilidad clínica y análisis de subgrupos.
---

9. **Tecnologías Utilizadas**

   
   - pandas, numpy

   - matplotlib, seaborn

   - scikit-learn

   - lifelines

   - xgboost
---
10. **Autores**

- [Betania Medina](https://github.com/Betaniammc)
- [Carlos Restrepo ](https://github.com/carlos-villa-restrepo)
- [Elius Trujillo](https://www.linkedin.com/in/elius-trujillo/)
---
Proyecto de Data Science enfocado en Machine Learning aplicado y Survival Analysis.