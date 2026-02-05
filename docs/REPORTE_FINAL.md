# 🏥 Reporte Exploratorio: Análisis de Escenarios de Supervivencia Oncológica
> Documento exploratorio generado con fines académicos. Los resultados reflejan asociaciones aprendidas por modelos predictivos y de supervivencia, y no implican relaciones causales ni recomendaciones clínicas.

---

## 📊 Resumen de Resultados
A continuación se presentan las métricas clave obtenidas tras el análisis del lote de pacientes:

| Métrica | Valor |
| :--- | :--- |
| **Total de Pacientes Analizados** | 30 |
| **Pacientes con beneficio estimado positivo** | 3 |
| **Beneficio medio estimado (meses)** | 0.48 meses |

*El beneficio medio corresponde a una estimación agregada del modelo y no representa una ganancia clínica observada.*

---

## 📈 Visualización del Beneficio Estimado por Escenario
El gráfico muestra la diferencia estimada en meses de supervivencia bajo distintos escenarios simulados.

![Gráfico de Impacto](grafico_impacto.png)

*Figura 1: Comparativa de meses ganados por paciente según el modelo de supervivencia.*

---

## 📑 Detalle de Pacientes Proprocesados
Esta tabla contiene los datos técnicos utilizados para la toma de decisiones:

| Grupo | Nº pacientes | Beneficio medio (meses) |
| :--- | :---: | :---: |
| **Con beneficio estimado** | 3 | 4.84 |
| **Sin beneficio estimado** | 27 | 0 |

Los resultados individuales se analizan únicamente con fines técnicos y no se presentan como salidas operativas del modelo.

---

## 🧠 Conclusiones del Análisis
1. **Determinantes del riesgo:** La etapa clínica (`Stage_Rank`) emerge consistentemente como el principal factor asociado a la supervivencia base.
2. **Heterogeneidad del efecto:** El análisis de escenarios sugiere que el efecto estimado del tratamiento no es uniforme y varía según el perfil clínico del paciente.
3. **Valor metodológico:** La combinación de modelos de ML y survival analysis permite explorar diferencias relativas entre escenarios, aunque no permite inferir causalidad ni efectividad clínica.
---
