# Dataset - FinPredict NLP

## 1. Descripción

El dataset de FinPredict NLP será utilizado para evaluar modelos preentrenados de procesamiento de lenguaje natural en la identificación de señales tempranas de riesgo financiero asociadas con créditos hipotecarios.

Para evitar el uso de información confidencial o datos personales, el conjunto de datos utilizado en este prototipo será sintético y estará diseñado exclusivamente con fines académicos.

Los textos representarán posibles interacciones o gestiones relacionadas con clientes hipotecarios en un contexto financiero mexicano.

---

## 2. Variable objetivo

El problema se plantea como una tarea de clasificación binaria.

### Clases

- `1 - SEÑAL_RIESGO`: el texto contiene información que puede indicar deterioro de la capacidad de pago o una dificultad financiera actual.
- `0 - SIN_SEÑAL_RIESGO`: el texto no presenta evidencia suficiente de una dificultad financiera actual.

La clasificación será utilizada como referencia para evaluar las predicciones realizadas por los modelos preentrenados.

---

## 3. Diccionario de datos

| Campo | Tipo | Descripción |
|---|---|---|
| id | string | Identificador único del registro |
| texto | string | Texto sintético relacionado con una interacción o gestión hipotecaria |
| etiqueta | integer | Variable objetivo: 1 = señal de riesgo, 0 = sin señal de riesgo |
| clase | string | Descripción de la etiqueta: SEÑAL_RIESGO o SIN_SEÑAL_RIESGO |
| tipo_senal | string | Categoría general asociada con el contenido del texto |
| dificultad | string | Nivel estimado de complejidad lingüística del ejemplo |
| expresion_local | integer | Indica si el texto contiene expresiones o vocabulario de uso común en México |

---

## 4. Categorías de señales

Los textos podrán representar situaciones como:

### Señales de riesgo

- pérdida de empleo;
- reducción de ingresos;
- problemas de liquidez;
- atrasos en pagos;
- solicitud de reestructura;
- solicitud de diferimiento;
- imposibilidad temporal de pago;
- gastos extraordinarios;
- dificultades financieras familiares;
- solicitud de quita.

### Sin señal de riesgo

- consultas administrativas;
- solicitud de estados de cuenta;
- aclaraciones de pagos;
- confirmación de pagos realizados;
- cambios de datos;
- consultas sobre fechas;
- solicitudes de información;
- situaciones hipotéticas;
- problemas ya resueltos sin evidencia de dificultad financiera actual.

---

## 5. Reglas de etiquetado

### SEÑAL_RIESGO

Se asignará la etiqueta `1` cuando el texto presente evidencia explícita o contextual de una dificultad financiera actual que pueda afectar el cumplimiento del crédito.

Ejemplos:

> Perdí mi empleo y necesito revisar opciones para pagar la mensualidad.

> Este mes recibí menos sueldo y no sé si podré cubrir el crédito.

> Se me juntaron varios pagos y necesito solicitar un diferimiento.

---

### SIN_SEÑAL_RIESGO

Se asignará la etiqueta `0` cuando el texto corresponda a una gestión administrativa o cuando no exista evidencia suficiente de una dificultad financiera actual.

Ejemplos:

> Realicé el pago mediante SPEI y quiero confirmar que ya fue aplicado.

> Necesito una copia de mi estado de cuenta.

> Quiero conocer qué opciones existirían si algún día perdiera mi empleo.

---

## 6. Casos lingüísticos especiales

El dataset incluirá ejemplos que permitan evaluar si los modelos comprenden el contexto y no solamente palabras asociadas con riesgo.

### Negación

Ejemplo:

> No tengo problemas económicos y continuaré pagando normalmente.

Aunque contiene la expresión "problemas económicos", debe clasificarse como `SIN_SEÑAL_RIESGO`.

### Situaciones hipotéticas

Ejemplo:

> ¿Qué sucedería con mi crédito si en algún momento perdiera mi empleo?

Debe clasificarse como `SIN_SEÑAL_RIESGO`, ya que no describe una dificultad actual.

### Lenguaje informal o expresiones locales

Ejemplo:

> Este mes ando corto y no creo completar la mensualidad.

Debe clasificarse como `SEÑAL_RIESGO`.

### Situaciones resueltas

Ejemplo:

> Tuve un atraso el mes pasado, pero ya regularicé todos mis pagos.

Debe clasificarse como `SIN_SEÑAL_RIESGO`, salvo que el texto incluya evidencia adicional de dificultad financiera vigente.

---

## 7. Uso de las variables

Para la inferencia de los modelos se utilizará principalmente:

`texto → etiqueta`

Las variables `tipo_senal`, `dificultad` y `expresion_local` serán utilizadas posteriormente para realizar análisis de errores y determinar en qué tipos de lenguaje presenta mayores dificultades cada modelo.

---

## 8. Consideraciones

El dataset no busca representar información real de clientes ni reproducir datos de una institución financiera específica.

Su finalidad es permitir una comparación controlada y reproducible entre diferentes modelos preentrenados de Hugging Face.

---

## 9. Composición del dataset

El dataset estará compuesto por 2,000 registros sintéticos y balanceados:

| Clase | Registros | Proporción |
|---|---:|---:|
| SEÑAL_RIESGO | 1,000 | 50 % |
| SIN_SEÑAL_RIESGO | 1,000 | 50 % |
| **Total** | **2,000** | **100 %** |

El balance entre clases permitirá comparar los modelos bajo condiciones controladas y facilitará la interpretación de métricas como accuracy, precision, recall y F1-score.

---

## 10. Distribución de casos con señal de riesgo

| Tipo de señal | Registros |
|---|---:|
| Pérdida de empleo | 140 |
| Reducción de ingresos | 140 |
| Problemas de liquidez | 140 |
| Atraso o dificultad de pago | 120 |
| Solicitud de reestructura | 120 |
| Solicitud de diferimiento | 100 |
| Gastos extraordinarios | 90 |
| Solicitud de quita | 80 |
| Dificultades financieras familiares | 70 |
| **Total** | **1,000** |

---

## 11. Distribución de casos sin señal de riesgo

| Tipo de interacción | Registros |
|---|---:|
| Confirmación de pago realizado | 180 |
| Aclaración de pago | 150 |
| Solicitud de estado de cuenta | 140 |
| Consulta de fechas o información | 140 |
| Cambio o actualización de datos | 100 |
| Situaciones hipotéticas | 120 |
| Situaciones financieras resueltas | 100 |
| Consultas preventivas | 70 |
| **Total** | **1,000** |

---

## 12. Complejidad lingüística

Los textos se clasifican en tres niveles de dificultad:

- `baja`
- `media`
- `alta`

A diferencia de la distribución de clases, los niveles de dificultad no se asignan mediante proporciones predeterminadas.

La dificultad se determina mediante reglas lingüísticas observables en cada texto.

### Dificultad baja

Corresponde principalmente a textos con una intención explícita y directa.

Ejemplo:

> Perdí mi empleo y no podré cubrir la mensualidad completa.

### Dificultad media

Incluye textos con incertidumbre, lenguaje indirecto o situaciones que requieren cierto nivel de interpretación contextual.

Ejemplo:

> Mis ingresos disminuyeron y probablemente tenga dificultades para cubrir la mensualidad.

### Dificultad alta

Incluye textos con elementos como:

- negaciones;
- situaciones hipotéticas;
- situaciones financieras ya resueltas;
- temporalidad;
- expresiones locales;
- contraste entre diferentes partes del mensaje;
- mayor ambigüedad contextual.

Ejemplo:

> Tuve problemas económicos el mes pasado, pero ya regularicé todos mis pagos.

La dificultad se calcula automáticamente durante la generación del dataset para permitir posteriormente el análisis del desempeño de los modelos según la complejidad lingüística.

## 13. Lenguaje local

El dataset contiene 400 registros con expresiones o construcciones lingüísticas contextualizadas al español utilizado en México.

La distribución se encuentra balanceada entre las dos clases:

| Clase | Lenguaje estándar | Lenguaje local |
|---|---:|---:|
| SEÑAL_RIESGO | 800 | 200 |
| SIN_SEÑAL_RIESGO | 800 | 200 |
| **Total** | **1,600** | **400** |

El balance evita que la presencia de lenguaje local quede asociada artificialmente con una determinada clase.

Esta característica permitirá analizar posteriormente si el desempeño de los modelos cambia al procesar expresiones locales o lenguaje menos formal.

## 14. Principio de diseño

El dataset se diseñará para evitar que la clasificación pueda resolverse únicamente mediante palabras clave.

Se incluirán pares de textos con vocabulario similar pero diferente significado contextual.

Ejemplo:

**SEÑAL_RIESGO**

> Me quedé sin trabajo y no sé cómo voy a pagar la siguiente mensualidad.

**SIN_SEÑAL_RIESGO**

> No me quedé sin trabajo; sólo quiero saber qué opciones tendría si eso ocurriera en el futuro.

Esto permitirá evaluar la capacidad de los modelos para interpretar contexto, negación y temporalidad.

## Reproducibilidad en Google Colab

El proceso de generación y validación del dataset puede reproducirse
directamente desde Google Colab mediante el siguiente notebook:

[![Abrir en Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lizlorenzana931109-art/finpredict-nlp/blob/main/notebooks/00_dataset_generation_validation.ipynb)

El notebook ejecuta el script `src/data_generation.py`, genera el dataset
y realiza las validaciones de calidad documentadas en esta sección.
