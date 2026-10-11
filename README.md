# FinPredict NLP

Prototipo de NLP para la identificación temprana de señales de riesgo hipotecario mediante modelos preentrenados de Hugging Face.

## Descripción del proyecto

FinPredict NLP es una extensión experimental de FinPredict orientada al análisis de información no estructurada.

El proyecto busca evaluar el uso de modelos preentrenados de procesamiento de lenguaje natural (NLP) para identificar señales tempranas de riesgo financiero presentes en textos asociados con la gestión de créditos hipotecarios.

El prototipo se desarrollará utilizando modelos disponibles en Hugging Face y Google Colab con GPU como entorno de experimentación.

## Problema de negocio

Los modelos tradicionales de riesgo utilizan principalmente información estructurada, como historial de pagos, atrasos y comportamiento financiero.

Sin embargo, las interacciones de los clientes pueden contener señales adicionales relacionadas con dificultades económicas, reducción de ingresos, desempleo, solicitudes de reestructura o problemas temporales de liquidez.

Estas señales pueden aparecer en texto antes de reflejarse completamente en las variables transaccionales.

FinPredict NLP explora la posibilidad de identificar automáticamente estas señales mediante técnicas de procesamiento de lenguaje natural.

## Objetivo

Comparar al menos tres modelos preentrenados disponibles en Hugging Face para determinar cuál ofrece el mejor equilibrio entre:

- capacidad de identificación de señales de riesgo;
- precisión;
- recall;
- F1-score;
- latencia de inferencia;
- recursos computacionales requeridos;
- adecuación al procesamiento de textos en español.

La selección final considerará tanto el desempeño técnico como la viabilidad de implementación en un contexto financiero.

## Alcance del prototipo

El proyecto se desarrollará como una prueba de concepto académica.

El alcance incluye:

- generación o utilización de un dataset de textos asociados con situaciones de gestión hipotecaria;
- clasificación binaria de los textos en:
  - `SEÑAL_RIESGO`;
  - `SIN_SEÑAL_RIESGO`;
- evaluación de diferentes estrategias de procesamiento mediante modelos preentrenados;
- comparación de modelos utilizando métricas estándar;
- medición de latencia;
- análisis del equilibrio entre precisión y eficiencia;
- documentación reproducible del experimento.

El prototipo no utilizará información personal ni conversaciones reales de clientes. El dataset empleado será sintético o proveniente de fuentes adecuadas para fines académicos.

## Estado del proyecto

🚧 Proyecto en desarrollo.

Actualmente se encuentra en la etapa de diseño del dataset y definición de los criterios de evaluación.
