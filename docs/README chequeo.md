📊 Origen de los Datos y Metodología
Este proyecto utiliza datos del programa Surveillance, Epidemiology, and End Results (SEER) de los Estados Unidos. La muestra se compone de 72,462 registros procesados mediante el software SEER*Stat.

Especificaciones del Dataset
Base de Datos: Incidence - SEER Research Data, 17 Registries, Nov 2024 Sub (2000-2022).

Atributos Vinculados: Atributos de condados dependientes del tiempo (Ingresos/Ruralidad 1990-2023).

Tipo de Sesión: Case Listing (Listado de casos individuales).

Rango de Diagnóstico: 2018 - 2022 (con histórico complementario).



📂 Diccionario Completo de Variables (29)
1. Perfil Demográfico y Socioeconómico
Age recode with <1 year olds and 90+: Edad del paciente categorizada al momento del diagnóstico.

Sex: Género biológico del paciente.

Race and origin (recommended by SEER): Variable combinada de raza y origen étnico (incluye NHW, NHB, etc.).

Race recode (White, Black, Other): Clasificación racial simplificada en tres categorías.

Origin recode NHIA (Hispanic, Non-Hisp): Identificador específico de herencia hispana (Algoritmo NHIA).

Marital status at diagnosis: Estado civil al momento de detectar la enfermedad.

Median household income inflation adj to 2023: Ingreso familiar medio del condado, ajustado al valor real de 2023.

Rural-Urban Continuum Code: Índice de urbanización del condado de residencia.

PRCDA 2020: Indicador de condados cubiertos por el Purchased/Referred Care Delivery Area (áreas con poblaciones indígenas o específicas).

2. Identificación y Fuente de Datos
Primary Site - labeled: Código del sitio anatómico donde se originó el tumor.

Year of diagnosis: Año en que se confirmó el diagnóstico.

Type of Reporting Source: Origen del reporte (Hospital, laboratorio, certificado de defunción, etc.).

Sequence number: Orden de aparición de este tumor en la vida del paciente (ej. si es su primer o segundo cáncer).

Total number of in situ/malignant tumors for patient: Conteo total de tumores diagnosticados en el individuo.

3. Caracterización del Tumor (Patología y Clínica)
Histologic Type ICD-O-3: Tipo celular del tumor (Morfología).

Grade Clinical (2018+): Grado de diferenciación de las células cancerosas (I al IV).

Diagnostic Confirmation: Método utilizado para confirmar el cáncer (Histología, citología, solo imagen, etc.).

Tumor Size Summary (2016+): Tamaño del tumor en milímetros (datos recientes).

CS tumor size (2004-2015): Tamaño del tumor registrado bajo el sistema Collaborative Stage (histórico).

4. Estadificación y Extensión (Staging)
Derived EOD 2018 Stage Group Recode (2018+): Grupo de etapa derivado de la Extensión de la Enfermedad (EOD).

AJCC ID (2018+): Identificador de estadificación basado en la 8va edición de AJCC.

Combined Summary Stage with Expanded Regional Codes (2004+): Clasificación general (Localizado, Regional, Distante).

CS extension (2004-2015): Detalle de qué tan lejos se extendió el tumor primario (histórico).

Derived AJCC T, 7th ed (2010-2015): Categoría T (Tumor) de la 7ma edición.

Derived AJCC N, 7th ed (2010-2015): Categoría N (Nodos/Gánglios) de la 7ma edición.

Derived AJCC M, 7th ed (2010-2015): Categoría M (Metástasis) de la 7ma edición.

5. Tratamiento y Resultados (Target Variables)
Survival months: Variable de tiempo hasta el evento o último contacto (Meses).

Vital status recode (study cutoff used): Estado final del paciente al cierre del estudio (Vivo/Muerto).

SEER cause-specific death classification: Indica si la muerte fue causada por este cáncer o por otra razón.

RX Summ--Surg Prim Site (1998+): Tipo de cirugía realizada en el sitio primario.
