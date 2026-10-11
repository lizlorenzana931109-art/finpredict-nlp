# FinPredict NLP

## Identificación temprana de señales de riesgo hipotecario mediante NLP

FinPredict NLP es un prototipo de inteligencia artificial orientado a la
identificación temprana de señales de dificultad de pago en textos de
atención y gestión con clientes hipotecarios.

El proyecto compara diferentes estrategias de Procesamiento de Lenguaje
Natural (NLP) utilizando modelos preentrenados disponibles en el ecosistema
de Hugging Face.

> Proyecto académico desarrollado como prueba de concepto.  
> Los datos utilizados son sintéticos y no contienen información real de clientes.

---

## 1. Problema de negocio

Los modelos tradicionales de riesgo crediticio suelen apoyarse principalmente
en variables estructuradas como pagos, atrasos, saldos o comportamiento
histórico.

Sin embargo, durante las interacciones con clientes pueden aparecer señales
lingüísticas tempranas como:

- pérdida de empleo;
- reducción de ingresos;
- problemas de liquidez;
- dificultad para realizar el siguiente pago;
- solicitudes de reestructura;
- diferimientos;
- gastos extraordinarios;
- situaciones familiares con impacto financiero.

FinPredict NLP explora si estas señales pueden identificarse mediante modelos
preentrenados de lenguaje antes de que se materialicen en variables
estructuradas de incumplimiento.

---

## 2. Objetivo

Clasificar textos relacionados con clientes hipotecarios en dos categorías:

- `1 = SEÑAL_RIESGO`
- `0 = SIN_SEÑAL_RIESGO`

El objetivo del prototipo no es automatizar decisiones crediticias, sino
evaluar la viabilidad de utilizar NLP como mecanismo de priorización para
acciones preventivas y revisión humana.

---

## 3. Dataset

Se generó un dataset sintético y reproducible de:

- 2,000 registros;
- 1,000 textos con señal de riesgo;
- 1,000 textos sin señal de riesgo.

Variables:

| Variable | Descripción |
|---|---|
| `id` | Identificador del registro |
| `texto` | Texto sintético de interacción |
| `etiqueta` | Variable binaria objetivo |
| `clase` | Descripción de la clase |
| `tipo_senal` | Categoría temática |
| `dificultad` | Nivel lingüístico asignado |
| `expresion_local` | Indicador de lenguaje local |

El dataset incorpora expresiones contextualizadas al español utilizado en
México para analizar el comportamiento de los modelos ante variaciones
lingüísticas.

La metodología completa se encuentra en:

`data/README.md`

---

## 4. Modelos evaluados

Se analizaron tres estrategias.

### Estrategia 1 — Español

`Recognai/zeroshot_selectra_medium`

Modelo orientado al español utilizado directamente sobre el texto original.

### Estrategia 2 — Multilingüe

`MoritzLaurer/mDeBERTa-v3-base-xnli-multilingual-nli-2mil7`

Modelo multilingüe utilizado directamente sobre los textos en español.

### Estrategia 3 — Inglés + traducción

Traducción:

`Helsinki-NLP/opus-mt-es-en`

Clasificación:

`facebook/bart-large-mnli`

Esta estrategia traduce primero el texto de español a inglés y posteriormente
realiza la clasificación zero-shot.

Los criterios técnicos utilizados para seleccionar los modelos se documentan
en:

`docs/model_selection.md`

---

## 5. Metodología experimental

El experimento se dividió en tres conjuntos independientes:

| Etapa | Registros | Objetivo |
|---|---:|---|
| Piloto | 10 | Exploración inicial |
| Calibración | 60 | Selección de configuración semántica |
| Evaluación final | 1,930 | Comparación definitiva |

La configuración semántica seleccionada fue determinada utilizando
exclusivamente el conjunto de calibración.

Posteriormente quedó congelada antes de evaluar los 1,930 registros finales,
reduciendo el riesgo de ajustar los prompts a los resultados de evaluación.

---

## 6. Métricas utilizadas

Para comparar los modelos se calcularon:

- Accuracy
- Precision
- Recall
- F1-score de la clase de riesgo
- F1 macro
- Latencia promedio
- Throughput

También se realizaron análisis segmentados por:

- dificultad lingüística;
- presencia de expresiones locales.

---

## 7. Resultados finales

| Estrategia | Accuracy | Precision | Recall | F1 riesgo | F1 macro | Latencia |
|---|---:|---:|---:|---:|---:|---:|
| SELECTRA | 60.73 % | 56.02 % | 99.79 % | 71.76 % | 53.65 % | 5.13 ms |
| mDeBERTa | 66.42 % | 59.83 % | 100.00 % | 74.86 % | 62.16 % | 10.82 ms |
| **BART + traducción** | **74.25 %** | **66.01 %** | **100.00 %** | **79.52 %** | **72.42 %** | 61.41 ms |

Los tiempos corresponden al entorno experimental utilizado en Google Colab
con GPU y no deben interpretarse como latencias garantizadas en producción.

---

## 8. Lenguaje local

El desempeño también fue analizado sobre textos con expresiones locales.

### F1 macro

| Modelo | Lenguaje estándar | Lenguaje local |
|---|---:|---:|
| SELECTRA | 0.5376 | 0.5320 |
| mDeBERTa | 0.6238 | 0.6127 |
| **BART + traducción** | **0.7191** | **0.7442** |

Dentro del dataset evaluado, la traducción no produjo una pérdida observable
de desempeño ante las expresiones locales incluidas.

Este resultado se limita al conjunto sintético utilizado y no implica que
toda variación regional del español pueda procesarse sin pérdida semántica.

---

## 9. Dificultad lingüística

### F1 macro

| Dificultad | SELECTRA | mDeBERTa | BART + traducción |
|---|---:|---:|---:|
| Baja | 0.4124 | 0.4574 | **0.6131** |
| Media | 0.4885 | 0.5761 | **0.6752** |
| Alta | 0.5466 | 0.6588 | **0.7519** |

BART + traducción mantuvo el mejor desempeño en los tres segmentos.

La dificultad fue definida mediante reglas lingüísticas y se utiliza como
evidencia complementaria; no representa una medida absoluta de complejidad
para cada arquitectura.

---

## 10. Trade-off entre desempeño y eficiencia

Los resultados muestran un intercambio claro:

**SELECTRA**

- menor latencia;
- mayor capacidad de procesamiento;
- menor desempeño global.

**mDeBERTa**

- desempeño intermedio;
- latencia considerablemente menor que BART;
- alternativa con buen equilibrio entre calidad y eficiencia.

**BART + traducción**

- mejor desempeño global;
- mayor robustez en los segmentos analizados;
- mayor costo computacional;
- requiere una etapa adicional de traducción.

---

## 11. Modelo recomendado

Para la prueba de concepto se recomienda:

### `BART + traducción`

La recomendación se sustenta en:

- mayor accuracy;
- mayor precision;
- recall de 100 %;
- mayor F1 de riesgo;
- mayor F1 macro;
- mejor desempeño con lenguaje local;
- mejor desempeño en los tres niveles de dificultad.

La principal desventaja es su mayor latencia.

Si el escenario de implementación priorizara eficiencia computacional sobre
la máxima calidad predictiva, `mDeBERTa` sería la segunda alternativa
recomendada.

---

## 12. Consideraciones para implementación

El prototipo no debe utilizarse para tomar decisiones automáticas sobre
clientes.

Aunque BART + traducción alcanzó recall de 100 %, su precision de 66.01 %
indica que todavía existe una cantidad relevante de falsos positivos.

Por esta razón, su uso inicial sería como:

**herramienta de priorización + revisión humana**

antes de cualquier acción operativa.

Una implementación productiva requeriría, entre otros elementos:

- validación con datos reales y representativos;
- participación de las áreas de Riesgo y Operaciones;
- revisión de sesgos;
- monitoreo de desempeño;
- explicabilidad y trazabilidad;
- definición de umbrales operativos;
- controles de privacidad y seguridad.

---

## 13. Ecosistema Hugging Face

El proyecto utiliza el ecosistema Hugging Face principalmente mediante:

- **Models:** acceso a modelos preentrenados;
- **Hub:** consulta y descarga de modelos y documentación;
- **Transformers:** creación de pipelines de inferencia;
- **Datasets:** disponible dentro del entorno experimental;
- **Spaces:** identificado como alternativa para una futura demostración interactiva.

La autenticación al Hub se realiza mediante token de lectura y las
credenciales no se almacenan dentro del repositorio.

---

## 14. Estructura del repositorio

```text
finpredict-nlp/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   ├── README.md
│   └── finpredict_nlp_dataset.csv
│
├── docs/
│   └── model_selection.md
│
├── notebooks/
│   ├── 00_dataset_generation_validation.ipynb
│   └── 01_model_comparison.ipynb
│
├── results/
│   ├── metricas_modelos.csv
│   ├── metricas_por_dificultad.csv
│   └── metricas_lenguaje_local.csv
│
└── src/
    └── data_generation.py
