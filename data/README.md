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
