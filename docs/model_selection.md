# Selección de modelos - FinPredict NLP

## 1. Objetivo de la selección

El objetivo de esta etapa es identificar modelos preentrenados de Hugging Face adecuados para clasificar textos asociados con la gestión de créditos hipotecarios e identificar señales tempranas de riesgo financiero.

La selección no se realizará únicamente con base en popularidad o precisión reportada por terceros.

Los modelos serán evaluados considerando criterios técnicos, operativos y de negocio relevantes para el contexto de FinPredict NLP.

---

## 2. Tarea de NLP

El problema corresponde a una tarea de clasificación de texto.

Las clases definidas son:

- `SEÑAL_RIESGO`
- `SIN_SEÑAL_RIESGO`

El prototipo evaluará la capacidad de modelos preentrenados para clasificar textos sin realizar inicialmente un entrenamiento completo desde cero.

---

## 3. Estrategias tecnológicas a evaluar

Se analizarán tres estrategias:

### Estrategia A - Modelo orientado a español

Modelo con capacidad específica para procesar textos en español.

La inferencia se realizará directamente sobre el texto original.

### Estrategia B - Modelo multilingüe

Modelo preentrenado con soporte para múltiples idiomas, incluyendo español.

La inferencia también se realizará directamente sobre el texto original.

### Estrategia C - Modelo especializado en inglés

Modelo cuya principal capacidad se encuentre en inglés.

Para utilizarlo con datos de FinPredict NLP será necesario incorporar una etapa previa de traducción:

`Español → Traducción → Modelo en inglés → Clasificación`

Esta alternativa permitirá analizar si una posible mejora técnica compensa el costo y latencia adicionales introducidos por la traducción.

---

## 4. Criterios obligatorios

Para formar parte de la evaluación, un modelo deberá cumplir con los siguientes requisitos:

- estar disponible en Hugging Face Hub;
- contar con documentación o Model Card;
- ser compatible con una tarea de clasificación aplicable al caso de uso;
- permitir inferencia mediante el ecosistema Transformers;
- poder ejecutarse en Google Colab;
- contar con una licencia identificable;
- permitir reproducir el experimento;
- tener requerimientos computacionales razonables para el prototipo.

Los modelos que no cumplan estos requisitos serán descartados antes de la comparación.

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

---

## 6. Criterio lingüístico

Debido a que el caso de uso se plantea para un contexto mexicano, el idioma constituye una variable relevante para la selección.

Se considerarán:

- comprensión directa del español;
- capacidad para interpretar negaciones;
- comprensión de temporalidad;
- lenguaje informal;
- expresiones contextualizadas al español utilizado en México;
- posible pérdida semántica ocasionada por traducción.

El dataset contiene una muestra controlada de lenguaje local que permitirá evaluar posteriormente este aspecto.

---

## 7. Criterio de eficiencia

La selección final no dependerá exclusivamente de la métrica con mayor valor.

Se analizará el equilibrio entre:

`Calidad de clasificación ↔ Latencia ↔ Recursos ↔ Complejidad operativa`

Por ejemplo, un modelo con una mejora marginal en F1-score podría no ser seleccionado si requiere considerablemente más recursos o introduce una etapa adicional de traducción.

---

## 8. Métricas experimentales

Los modelos seleccionados serán evaluados sobre el mismo dataset mediante:

- accuracy;
- precision;
- recall;
- F1-score;
- matriz de confusión;
- latencia de inferencia.

También se realizarán análisis segmentados considerando:

- dificultad lingüística;
- lenguaje estándar;
- lenguaje local.

---

## 9. Criterio de negocio

Para FinPredict NLP se dará especial atención al `recall` de la clase `SEÑAL_RIESGO`.

Un falso negativo representa un texto que contiene una señal potencial de deterioro financiero pero que el modelo no identifica.

En un escenario de uso real, este error podría implicar la pérdida de una oportunidad de intervención preventiva.

Por este motivo, la selección final considerará tanto F1-score como recall de la clase de riesgo.

---

## 10. Decisión

Los modelos específicos serán seleccionados después de aplicar los criterios anteriores a candidatos disponibles en Hugging Face Hub.

La decisión y sus evidencias serán documentadas antes de iniciar la comparación experimental.
