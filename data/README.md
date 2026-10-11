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

Además de la clase y el tipo de señal, los textos tendrán distintos niveles de dificultad:

| Dificultad | Registros aproximados | Proporción |
|---|---:|---:|
| Baja | 800 | 40 % |
| Media | 800 | 40 % |
| Alta | 400 | 20 % |

### Dificultad baja

Textos donde la intención es explícita.

Ejemplo:

> Perdí mi empleo y no puedo cubrir la mensualidad.

### Dificultad media

Textos donde la señal debe interpretarse mediante contexto.

Ejemplo:

> Este mes recibí menos ingresos y probablemente tenga problemas para completar el pago.

### Dificultad alta

Textos con negaciones, temporalidad, lenguaje informal, ambigüedad o información aparentemente contradictoria.

Ejemplo:

> Todavía no estoy atrasado, pero me redujeron las horas y el próximo mes no sé si pueda completar la mensualidad.

---

## 13. Características especiales

Algunos registros incorporarán características adicionales para evaluar la robustez de los modelos.

| Característica | Registros aproximados |
|---|---:|
| Expresiones o vocabulario mexicano | 400 |
| Negaciones | 200 |
| Situaciones hipotéticas | 120 |
| Situaciones resueltas | 100 |

Estas características pueden superponerse con otras categorías y no representan grupos independientes.

Por ejemplo, un registro puede contener simultáneamente una expresión local, una negación y dificultad alta.

---

## 14. Principio de diseño

El dataset se diseñará para evitar que la clasificación pueda resolverse únicamente mediante palabras clave.

Se incluirán pares de textos con vocabulario similar pero diferente significado contextual.

Ejemplo:

**SEÑAL_RIESGO**

> Me quedé sin trabajo y no sé cómo voy a pagar la siguiente mensualidad.

**SIN_SEÑAL_RIESGO**

> No me quedé sin trabajo; sólo quiero saber qué opciones tendría si eso ocurriera en el futuro.

Esto permitirá evaluar la capacidad de los modelos para interpretar contexto, negación y temporalidad.
