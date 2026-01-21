## 1. Variables Demográficas y Socioeconómicas
Estas definen quién es el paciente y su entorno.

<h3>Age recode with "<"1 year olds and 90+ :</h3> Edad agrupada. Es preferible a la edad continua para evitar identificar personas muy ancianas. Úsala para ver la distribución por cohortes de edad.

<h3>Race and origin (recommended by SEER) :</h3> Clasificación detallada de etnia (incluye específicos como filipino, japonés, etc.).

<h3>Race recode (White, Black, Other) :</h3> Versión simplificada de la anterior. Ideal para análisis de disparidades si los grupos pequeños no tienen suficiente volumen.

<h3>Origin recode NHIA (Hispanic, Non-Hisp) :</h3> Específico para identificar población de origen hispano.
El algoritmo NHIA (NAACCR Hispanic Identification Algorithm) es el estándar de oro para identificar la etnia hispana en bases de datos de EE. UU., combinando el apellido, el lugar de nacimiento y la autodeclaración.

Spanish-Hispanic-Latino: El paciente se identifica como hispano.

Non-Spanish-Hispanic-Latino: El paciente no es de origen hispano.

<h3>Median household income inflation adj to 2023 :</h3> Ingreso promedio del área de residencia del paciente. Es una variable "proxy" del nivel socioeconómico (Determinantes Sociales de la Salud).

<h3>Rural-Urban Continuum Code :</h3> Clasifica el condado del paciente desde metrópolis grandes hasta zonas rurales remotas. Vital para analizar acceso a salud.Esta variable clasifica el lugar de residencia del paciente. Es vital para tu modelo porque la supervivencia suele ser mayor en zonas con grandes centros hospitalarios.

Counties in metropolitan areas ge 1 million pop: Ciudades grandes (Nueva York, Los Ángeles, etc.). Máximo acceso a tecnología.

Counties in metropolitan areas of 250,000 to 1 million: Áreas urbanas medianas.

Nonmetropolitan counties (adjacent or not): Zonas rurales. Aquí la supervivencia puede ser menor debido a la distancia que el paciente debe recorrer para recibir quimioterapia o cirugía.

Unknown/no match: Generalmente registros con códigos postales incompletos o de territorios fuera de la zona estándar.

<h3>PRCDA 2020 (PurchasedReferred Care Delivery Area)</h3>
Esta variable es un indicador de geografía médica en Estados Unidos.

PRCDA: El paciente reside en un condado donde el Servicio de Salud Indígena (IHS) puede financiar atención médica externa.

Not PRCDA: El condado no pertenece a esta categoría.

Unknown PRCDA: Información geográfica incompleta.

## 2. Variables del Tumor (Biología y Localización)
Definen qué tipo de cáncer es.

<h3>Primary Site - labeled :</h3> Indica en qué parte específica del pulmón se originó el tumor.

C34.1, C34.2, C34.3: Lóbulos superior, medio e inferior. Es vital para la supervivencia; los tumores en el lóbulo superior a veces tienen pronósticos distintos por la cercanía a grandes vasos.

C34.0 (Main bronchus): El bronquio principal. Suele ser más central y difícil de operar.

C34.9 (Lung, NOS): "Not Otherwise Specified". Significa que en la historia clínica solo dice "pulmón" sin aclarar el lóbulo.

C34.8 (Overlapping lesion): El tumor es tan grande que abarca más de un lóbulo.


<h3>Histologic Type ICD-O-3 :</h3> El código de morfología. Crucial para distinguir entre Cáncer de pulmón de células no pequeñas (Adenocarcinoma, Escamoso) y Células pequeñas.

<h3>Grade Clinical (2018+) :</h3> Qué tan diferenciadas (anormales) están las células.Representa qué tan "anormales" se ven las células bajo el microscopio.

1, 2, 3, 4: Grado de diferenciación (1: Muy parecido al tejido normal/lento; 4: Indiferenciado/muy agresivo).

A, B, C, D: Son códigos nuevos introducidos en 2018 para tipos específicos de tumores (ej. Bien diferenciado, Moderadamente, etc.).

9 / Blank(s): Información no disponible o grado desconocido.

<h3>Total number of in situ/malignant tumors for patient :</h3> Indica si el paciente ha tenido otros cánceres. Un número alto puede complicar el pronóstico.

## 3. Estadificación (Severidad y Extensión)

Esta es la parte más técnica. SEER usa diferentes sistemas según el año de diagnóstico.

<h3>Year of diagnosis :</h3> Año en que se confirmó el diagnóstico.

<h3>Derived AJCC T (7th ed, 2010-2015) :</h3> 

Describe el tamaño del tumor original y si ha invadido tejidos cercanos dentro del pulmón o estructuras adyacentes.

T1a, T1b, T2a, T2b, T3, T4: Representan el crecimiento en centímetros y la invasión (T1 es pequeño, T4 es invasión de órganos vitales).

T1NOS / T2NOS: "Not Otherwise Specified". Sabemos que es T1 o T2, pero el informe no aclara si es 'a' o 'b'.
    T1 (T1a, T1b): Tumor pequeño (≤ 3 cm) rodeado por pulmón o pleura visceral.

    T2 (T2a, T2b): Tumor más grande (> 3 cm pero ≤ 7 cm) o que invade el bronquio principal o la pleura visceral.

TX: El tumor primario no puede ser evaluado.

T0: No hay evidencia de tumor primario (muy raro en cáncer de pulmón diagnosticado).

T0: No hay evidencia de tumor primario.


<h3>Derived AJCC N, 7th ed (2010-2015) :</h3> Describe si el cáncer se ha propagado a los ganglios linfáticos regionales y cuáles están afectados.

N0: El cáncer no ha llegado a los ganglios. Es el mejor escenario para una cirugía.

N1: Afectación de ganglios cercanos al pulmón afectado.

N2: El cáncer llegó al centro del pecho (mediastino) del mismo lado. Aquí la cirugía es mucho más compleja.

N3: Afectación del lado opuesto o arriba de la clavícula. Generalmente se considera inoperable.

NX: No se pudo evaluar (a veces por falta de pruebas).

Blank(s)/nan: Datos fuera del periodo 2010-2015.

<h3>Derived AJCC M, 7th ed (2010-2015) :</h3> Describe si el cáncer ha viajado a órganos lejanos.

M0: No hay evidencia de metástasis a distancia.

M1a: El cáncer está en ambos pulmones o en el líquido que rodea al pulmón/corazón.

M1b: Metástasis en órganos lejanos (cerebro, huesos, hígado). Es la fase más grave.

M1NOS: Se sabe que hay metástasis, pero el reporte no especifica de qué tipo.

<h3>Tumor Size Summary (2016+) / CS tumor size (2004-2015) :</h3> El tamaño exacto del tumor en milímetros. Se usan columnas distintas dependiendo del año de diagnóstico.

<h3>Combined Summary Stage (2004+) :</h3> Esta es la de gravedad.

In situ: El cáncer no ha atravesado la capa basal (no es invasivo aún).

Localized only: Solo está en el pulmón.

Regional (Direct extension / Node / Both): Se ha extendido a tejidos vecinos o a los ganglios linfáticos cercanos.

Distant site(s): Metástasis. El cáncer viajó a otros órganos (Etapa IV).

<h3>CS extension (2004-2015) :</h3>  Los números representan qué tan profundo "creció" el tumor.

100: El tumor está confinado al pulmón (localizado).

300 - 400: El tumor ha llegado a la pleura (la capa que recubre el pulmón) o a la pared del pecho.

700 - 800: El tumor invade estructuras críticas como el corazón, el esófago o la tráquea.

999: Información desconocida o no documentada.

Blank(s): Pacientes diagnosticados fuera del rango 2004-2015.

<h3>Derived EOD 2018 Stage Group :</h3> La estadificación más reciente para casos actuales, Este es el sistema más moderno (basado en la 8ª Edición de la AJCC). Es mucho más granular que las versiones anteriores.

1A1, 1A2, 1A3, 1B: Etapas muy tempranas. La diferencia entre 1A1 y 1A2 son milímetros de tamaño.

2A, 2B: Etapas intermedias.

3A, 3B, 3C: Etapas avanzadas regionales (el cáncer está en los ganglios del centro del pecho).

4A, 4B: Metástasis. 4B indica que el cáncer se ha extendido a múltiples órganos lejanos.

Códigos Especiales:

0: Carcinoma in situ (no invasivo).

OC: Cáncer Oculto (se ven células cancerosas en el esputo, pero no encuentran el tumor en imágenes).

88: No aplicable.

99: Desconocido.

<h3>AJCC ID (2018+) :</h3>
Esta variable es puramente administrativa pero vital para limpiar tus datos.

Lung: Confirma que el caso fue evaluado con el protocolo de pulmón.

No AJCC Chapter / Soft tissue sarcoma...: ¡Cuidado aquí! En tu EDA notarás que algunos tumores en el pulmón no son "cáncer de pulmón" típico (carcinoma), sino sarcomas (tejido blando).

Importancia para ML: Te sugiero filtrar tu dataset para quedarte solo con los que dicen Lung si quieres un modelo especializado en los tipos más comunes.

<h3> combined Summary Stage with Expanded Regional Codes (2004+) </h3>
Esta variable es el indicador de gravedad anatómica más completo que tienes para registros históricos (2004 en adelante). A diferencia del TNM (que es muy técnico), esta columna resume la "distancia" que ha recorrido el cáncer desde su origen en un lenguaje más descriptivo.

Para un modelo de ML, esta variable es oro porque tiene una jerarquía clara de supervivencia. Aquí te explico qué significa cada valor, ordenados de menor a mayor gravedad:

1. In situ
Es el estado más temprano posible. El cáncer está "en su lugar", no ha atravesado la membrana basal ni ha invadido el tejido circundante.

Impacto en ML: Supervivencia cercana al 100%.

2. Localized only
El tumor es invasivo (ya es un cáncer "real"), pero está confinado totalmente al pulmón donde empezó. No hay rastro de él en los ganglios ni en otros órganos.

Impacto en ML: Alta probabilidad de éxito con cirugía solo en el sitio primario.

3. Las categorías "Regional" (El cáncer empezó a viajar)
Aquí el cáncer ya salió del pulmón original hacia los "vecinos" (tejidos o ganglios cercanos):

Regional by direct extension only: Se pegó a estructuras vecinas (como la pared torácica) pero los ganglios están limpios.

Regional lymph nodes involved only: El tumor en el pulmón es pequeño, pero ya se detectaron células en los ganglios linfáticos del pecho.

Regional by both direct extension and lymph node involvement: Es el escenario regional más serio; el tumor creció hacia afuera e infectó los ganglios al mismo tiempo.

Distant site(s)/node(s) involved:
Es lo que conocemos como Metástasis. El cáncer ha viajado a través del torrente sanguíneo o sistema linfático a órganos lejanos (cerebro, hígado, huesos) o a ganglios muy alejados del pecho.

Impacto en ML: Es el predictor más fuerte de mortalidad a corto plazo.

Unknown/unstaged/unspecified/DCO:
Significa que no hay suficiente información en el expediente médico para clasificarlo.

DCO (Death Certificate Only): Casos donde solo se supo del cáncer por el certificado de defunción. Como te mencioné antes, estos registros suelen tener supervivencia de "0 meses" y pueden sesgar tu modelo.

## 4. Tratamiento y Fuente de Datos

<h3>RX Summ--Surg Prim Site (1998+) :</h3> Indica si se realizó cirugía y qué tipo (ej. lobectomía, neumonectomía).
00: Sin cirugía. No se realizó ningún procedimiento en el sitio primario.

10 - 19: Cirugía local / Biopsia. Procedimientos menores donde solo se extirpó una pequeña parte de la lesión.

20 - 25: Escisión local / Resección en cuña. Se quita el tumor con un pequeño margen de tejido sano, pero menos que un lóbulo.

30: Resección segmentaria. Se quita un segmento completo del pulmón.

33: Lobectomía con resección segmentaria. * 45 - 48: Lobectomía. Se extirpa un lóbulo completo del pulmón. Es el estándar de oro para muchos cánceres en etapa temprana.

55 - 56: Bilobectomía. Se extirpan dos lóbulos (solo posible en el pulmón derecho).

65 - 66: Neumonectomía. Se extirpa el pulmón completo.

70: Cirugía extendida. El cirujano quitó el pulmón y además parte de la pared torácica, diafragma o pericardio.

80: Cirugía, NOS. Se sabe que hubo cirugía, pero el reporte no especifica de qué tipo.

90: Desconocido. No hay registro de si se operó o no.

99: DCO / Autopsia. Casos donde solo se supo del cáncer tras la muerte.

<h3>Reason no cancer-directed surgery :</h3> Por qué no se operó Esta variable es fundamental si quieres entender por qué un paciente con un tumor operable no llegó a quirófano.

Surgery performed: El paciente recibió el tratamiento estándar.

Not recommended: El equipo médico decidió que la cirugía no era la mejor opción (comúnmente porque el cáncer ya está en etapa IV/Metastásica).

Recommended but not performed, patient refused: Un factor psicológico o social. El paciente decidió no operarse a pesar del consejo médico.

Not recommended, contraindicated due to other cond: El paciente tenía otras enfermedades (corazón, riñones, etc.) que hacían que la anestesia o la cirugía fueran más peligrosas que el propio cáncer.

Not performed, patient died prior to recommended surgery: Casos de progresión extremadamente rápida.

Unknown; death certificate; or autopsy only: Casos donde la información es de baja calidad porque el cáncer se descubrió después de la muerte.

<h3>Type of Reporting Source :</h3> De dónde viene el dato (Hospital, laboratorio, certificado de defunción). Ayuda a evaluar la calidad del dato.
Indica quién envió el dato a SEER. Esto afecta directamente la fiabilidad de tu modelo de ML.

Hospital inpatient/outpatient or clinic: Es el dato más fiable. Viene de un historial clínico completo.

Laboratory only: El dato viene de una biopsia. Puede que falte información sobre si el paciente sobrevivió o no a largo plazo.

Death certificate only (DCO): ¡Atención! En ML, estos casos suelen eliminarse. Si el registro viene solo del certificado de defunción, los Survival months suelen ser 0, lo que puede "engañar" a tu modelo SVC haciéndole creer que todos mueren instantáneamente.

Nursing/convalescent home/hospice: Pacientes que ya estaban en cuidados paliativos o residencias de ancianos.

<h3>Diagnostic Confirmation :</h3> Cómo se confirmó el cáncer (Biopsia microscópica, solo imagenología o solo clínica).

Positive histology: Confirmado con biopsia de tejido (Máxima certeza).

Positive exfoliative cytology: Confirmado por células en fluidos (esputo, líquido pleural).

Radiography / Clinical diagnosis only: No hubo biopsia; se determinó por tomografía o síntomas. Esto suele ocurrir en pacientes muy graves que no aguantarían una biopsia.

Direct visualization: El cirujano lo vio con sus propios ojos durante una operación pero no se analizó el tejido.

## 5. Resultados (Supervivencia y Estado Final)

<h3>Survival months :</h3> Tiempo transcurrido desde el diagnóstico hasta la muerte o el último seguimiento.

<h3>Vital status recode (study cutoff used) :</h3> 
Alive / Dead: Es una variable binaria simple. Indica si el paciente estaba vivo en el último contacto registrado por el hospita

<h3>SEER cause-specific death classification :</h3> Dead (attributable to this cancer dx): El paciente murió a causa del cáncer de pulmón.

Alive or dead of other cause: El paciente sigue vivo O murió por otra cosa (ej. un accidente o un infarto).

Nota técnica: En medicina, esto se llama "censura". Si alguien muere de un infarto, no podemos decir que el tratamiento del cáncer falló, simplemente "salieron" del estudio por otra razón.

Dead (missing/unknown COD): Murió, pero no se sabe por qué. Para un modelo de alta precisión, estos registros suelen descartarse

<h3>Sequence number :</h3> Indica el orden de este tumor en la vida del paciente (si es el primero, el segundo, etc.).

One primary only: Este es el único cáncer que el paciente ha tenido en su vida (según el registro). Representa la mayoría de los casos.

1st of 2 or more primaries: Es el primer cáncer detectado en un paciente que luego desarrolló otros.

2nd, 3rd... of N or more: Indica que el paciente ya tuvo otros cánceres antes que este.