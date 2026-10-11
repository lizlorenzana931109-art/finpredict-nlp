# Selección de modelos - FinPredict NLP

## 1. Objetivo de la selección

El objetivo de esta etapa es identificar modelos preentrenados de Hugging Face
adecuados para clasificar textos asociados con la gestión de créditos
hipotecarios e identificar señales tempranas de riesgo financiero.

La selección no se realizará únicamente con base en popularidad o precisión
reportada por terceros.

Los modelos serán evaluados considerando criterios técnicos, operativos y de
negocio relevantes para el contexto de FinPredict NLP.

---

## 2. Tarea de NLP

El problema corresponde a una tarea de clasificación de texto.

Las clases definidas son:

- `SEÑAL_RIESGO`
- `SIN_SEÑAL_RIESGO`

El prototipo evaluará la capacidad de modelos preentrenados para clasificar
textos sin realizar inicialmente un entrenamiento completo desde cero.

Para esta fase se utilizará un enfoque de clasificación **zero-shot**, lo que
permite evaluar modelos preentrenados sin realizar fine-tuning específico
sobre el dataset de FinPredict NLP.

---

## 3. Estrategias tecnológicas a evaluar

Se analizarán tres estrategias.

### Estrategia A - Modelo orientado a español

Modelo con capacidad específica para procesar textos en español.

La inferencia se realizará directamente sobre el texto original.

### Estrategia B - Modelo multilingüe

Modelo preentrenado con soporte para múltiples idiomas, incluyendo español.

La inferencia también se realizará directamente sobre el texto original.

### Estrategia C - Modelo especializado en inglés

Modelo cuya principal capacidad se encuentre en inglés.

Para utilizarlo con datos de FinPredict NLP será necesario incorporar una etapa
previa de traducción:

`Español → Traducción → Modelo en inglés → Clasificación`

Esta alternativa permitirá analizar si una posible mejora técnica compensa el
costo y latencia adicionales introducidos por la traducción.

---

## 3.1 Ecosistema Hugging Face considerado

La selección se desarrolla dentro del ecosistema Hugging Face, considerando
principalmente los siguientes componentes:

- **Hugging Face Hub:** repositorio utilizado para localizar, consultar y
  acceder a modelos preentrenados.
- **Model Cards:** documentación utilizada para revisar arquitectura, idioma,
  licencia, tarea, limitaciones y características de los modelos.
- **Transformers:** librería utilizada para implementar los pipelines de
  inferencia de los modelos seleccionados.
- **Datasets:** componente disponible para la gestión y evaluación de conjuntos
  de datos dentro del ecosistema.
- **Spaces:** alternativa para una futura demostración interactiva del
  prototipo, aunque no es necesaria para el alcance experimental actual.

La selección de candidatos se realiza utilizando información disponible en sus
respectivas Model Cards y considerando su compatibilidad con el flujo
experimental desarrollado en Google Colab.

---

## 4. Criterios obligatorios

Para formar parte de la evaluación, un modelo deberá cumplir con los siguientes
requisitos:

- estar disponible en Hugging Face Hub;
- contar con documentación o Model Card;
- ser compatible con una tarea de clasificación aplicable al caso de uso;
- permitir inferencia mediante el ecosistema Transformers;
- poder ejecutarse en Google Colab;
- contar con una licencia identificable;
- permitir reproducir el experimento;
- tener requerimientos computacionales razonables para el prototipo.

Los modelos que no cumplan estos requisitos serán descartados antes de la
comparación.

---

## 5. Criterios de evaluación

Los modelos candidatos serán evaluados mediante una matriz ponderada.

| Criterio | Peso |
|---|---:|
| Adecuación al caso de uso | 20 % |
| Capacidad lingüística | 20 % |
| Desempeño esperado / evidencia disponible | 15 % |
| Recursos computacionales | 10 % |
| Tamaño del modelo | 10 % |
| Latencia esperada | 10 % |
| Licencia y posibilidad de uso | 5 % |
| Calidad de documentación | 5 % |
| Facilidad de integración y reproducibilidad | 5 % |
| **Total** | **100 %** |

La matriz funciona como una herramienta de preselección técnica y no como
sustituto de la evaluación experimental.

La decisión final dependerá de las métricas obtenidas sobre un conjunto común
de evaluación.

---

## 6. Criterio lingüístico

Debido a que el caso de uso se plantea para un contexto mexicano, el idioma
constituye una variable relevante para la selección.

Se considerarán:

- comprensión directa del español;
- capacidad para interpretar negaciones;
- comprensión de temporalidad;
- lenguaje informal;
- expresiones contextualizadas al español utilizado en México;
- posible pérdida semántica ocasionada por traducción.

El dataset contiene una muestra controlada de lenguaje local que permitirá
evaluar posteriormente este aspecto.

---

## 7. Criterio de eficiencia

La selección final no dependerá exclusivamente de la métrica con mayor valor.

Se analizará el equilibrio entre:

`Calidad de clasificación ↔ Latencia ↔ Recursos ↔ Complejidad operativa`

Por ejemplo, un modelo con una mejora marginal en F1-score podría no ser
seleccionado si requiere considerablemente más recursos o introduce una etapa
adicional de traducción.

---

## 8. Métricas experimentales

Los modelos seleccionados serán evaluados sobre el mismo dataset mediante:

- accuracy;
- precision;
- recall;
- F1-score;
- F1 macro;
- matriz de confusión;
- latencia de inferencia;
- throughput.

También se realizarán análisis segmentados considerando:

- dificultad lingüística;
- lenguaje estándar;
- lenguaje local.

La evaluación utilizará el mismo conjunto final para los tres modelos con el
objetivo de mantener condiciones comparables.

---

## 9. Criterio de negocio

Para FinPredict NLP se dará especial atención al recall de la clase
`SEÑAL_RIESGO`.

Un falso negativo representa un texto que contiene una señal potencial de
deterioro financiero pero que el modelo no identifica.

En un escenario de uso real, este error podría implicar la pérdida de una
oportunidad de intervención preventiva.

Por este motivo, la selección final considerará tanto F1-score como recall de
la clase de riesgo.

Sin embargo, también se analizará la precision debido a que una cantidad
elevada de falsos positivos podría generar carga operativa innecesaria sobre
los equipos encargados de revisar las alertas.

Por esta razón, el F1 macro se incorpora como una métrica complementaria para
evaluar el comportamiento del modelo sobre ambas clases.

---

## 10. Decisión

Los modelos específicos serán seleccionados después de aplicar los criterios
anteriores a candidatos disponibles en Hugging Face Hub.

La decisión y sus evidencias serán documentadas antes de iniciar la
comparación experimental.

---

## 11. Modelos candidatos seleccionados

Después de aplicar los criterios técnicos y prácticos definidos para el
proyecto, se seleccionaron tres estrategias de modelado para la evaluación
experimental.

| Estrategia | Modelo | Idioma / enfoque | Uso en FinPredict NLP |
|---|---|---|---|
| Español | `Recognai/zeroshot_selectra_medium` | Español | Inferencia directa sobre el texto original |
| Multilingüe | `MoritzLaurer/mDeBERTa-v3-base-xnli-multilingual-nli-2mil7` | Multilingüe | Inferencia directa sobre el texto original |
| Inglés + traducción | `facebook/bart-large-mnli` | Inglés | Traducción previa español → inglés y posterior clasificación |

Para la estrategia en inglés se utilizará adicionalmente:

`Helsinki-NLP/opus-mt-es-en`

como modelo de traducción de español a inglés.

---

## 11.1 Matriz preliminar de selección de candidatos

Los tres modelos seleccionados fueron revisados utilizando los criterios
definidos previamente.

La puntuación corresponde a una evaluación preliminar de **1 a 5**, donde:

- `1` representa una adecuación baja;
- `3` representa una adecuación media;
- `5` representa una adecuación alta.

Esta evaluación fue realizada antes de conocer los resultados experimentales.

| Criterio | Peso | SELECTRA | mDeBERTa | BART + traducción |
|---|---:|---:|---:|---:|
| Adecuación al caso de uso | 20 % | 4 | 4 | 4 |
| Capacidad lingüística | 20 % | 5 | 4 | 3 |
| Evidencia técnica disponible | 15 % | 4 | 5 | 5 |
| Recursos computacionales | 10 % | 5 | 3 | 2 |
| Tamaño del modelo | 10 % | 5 | 3 | 2 |
| Latencia esperada | 10 % | 5 | 4 | 2 |
| Licencia | 5 % | 5 | 5 | 5 |
| Documentación | 5 % | 4 | 5 | 5 |
| Integración y reproducibilidad | 5 % | 5 | 5 | 4 |

La matriz anterior se utiliza únicamente para justificar la inclusión de los
candidatos en la fase experimental.

La selección final del modelo no se determina mediante esta puntuación
preliminar, sino mediante las métricas obtenidas sobre el conjunto común de
evaluación.

Esto permite separar dos momentos del proceso:

`Preselección técnica → Evaluación experimental → Decisión final`

---

## 12. Justificación preliminar de los candidatos

### 12.1 Recognai/zeroshot_selectra_medium

Se seleccionó como representante de la estrategia especializada en español.

El modelo está basado en SELECTRA y fue ajustado utilizando la porción en
español del dataset XNLI para tareas de inferencia de lenguaje natural.

Entre sus características relevantes se encuentran:

- compatibilidad con zero-shot classification;
- especialización en español;
- aproximadamente 40.8 millones de parámetros;
- licencia Apache 2.0;
- tamaño relativamente reducido frente a otras alternativas;
- posibilidad de utilizar directamente los textos originales de FinPredict NLP
  sin traducción.

La ausencia de una etapa de traducción representa una ventaja potencial en
latencia, consumo computacional y conservación del significado lingüístico
original.

Su incorporación permite evaluar si un modelo relativamente compacto y
orientado al español puede proporcionar una relación favorable entre
desempeño y eficiencia.

---

### 12.2 MoritzLaurer/mDeBERTa-v3-base-xnli-multilingual-nli-2mil7

Se seleccionó como representante de una estrategia multilingüe.

El modelo está preparado para zero-shot classification y fue desarrollado
utilizando datos de inferencia de lenguaje natural en múltiples idiomas.

Entre sus características relevantes se encuentran:

- soporte multilingüe, incluyendo español;
- aproximadamente 300 millones de parámetros;
- compatibilidad con Transformers;
- licencia MIT;
- posibilidad de procesar directamente los textos en español;
- entrenamiento relacionado con tareas NLI multilingües.

Su evaluación permitirá determinar si una arquitectura multilingüe de mayor
tamaño proporciona una ventaja suficiente sobre un modelo especializado en
español para justificar el incremento de recursos computacionales.

---

### 12.3 facebook/bart-large-mnli

Se seleccionó como representante de una estrategia especializada
principalmente en inglés.

BART Large MNLI está diseñado para tareas de inferencia de lenguaje natural y
puede utilizarse mediante zero-shot classification.

Entre sus características relevantes se encuentran:

- compatibilidad directa con zero-shot classification;
- entrenamiento asociado con MultiNLI;
- licencia MIT;
- mayor tamaño y requerimiento computacional que el modelo especializado en
  español;
- necesidad de incorporar una etapa de traducción para procesar los textos
  originales del proyecto.

Para esta estrategia se utilizará `Helsinki-NLP/opus-mt-es-en` como componente
de traducción español → inglés.

Esta arquitectura introduce una complejidad adicional que deberá medirse
experimentalmente:

`Texto español → Traducción → Clasificación en inglés`

La evaluación considerará tanto la calidad de clasificación como la latencia
total de esta cadena de procesamiento.

De esta manera será posible determinar si el incremento en complejidad
operativa se encuentra justificado por una mejora relevante en desempeño.

---

## 13. Hipótesis experimental

Antes de ejecutar los modelos se establecen las siguientes hipótesis:

**H1.** Un modelo especializado en español podría ofrecer una relación
favorable entre desempeño y eficiencia al procesar directamente los textos
originales.

**H2.** El modelo multilingüe podría mejorar la comprensión contextual, aunque
con un mayor consumo de recursos computacionales.

**H3.** La estrategia inglés + traducción podría ofrecer buen desempeño de
clasificación, pero presentar mayor latencia y complejidad operativa debido a
la etapa adicional de traducción.

**H4.** La traducción podría afectar de manera particular los textos que
contienen expresiones locales o lenguaje informal utilizado en México.

Estas hipótesis serán contrastadas utilizando exactamente el mismo conjunto de
evaluación.

Los resultados obtenidos posteriormente no modificarán estas hipótesis
iniciales, sino que se utilizarán para aceptarlas, rechazarlas o matizarlas con
base en evidencia experimental.
