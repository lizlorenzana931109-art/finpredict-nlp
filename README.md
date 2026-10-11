# FinPredict NLP

## Identificación temprana de señales de riesgo hipotecario mediante Procesamiento de Lenguaje Natural

**FinPredict NLP** es una prueba de concepto orientada a identificar señales
tempranas de dificultad de pago en textos asociados con la atención y gestión
de clientes hipotecarios.

El proyecto compara distintas estrategias de Procesamiento de Lenguaje Natural
utilizando modelos preentrenados disponibles en el ecosistema de
**Hugging Face**.

> **Proyecto académico desarrollado con datos sintéticos.**
> No contiene información real de clientes y sus resultados no deben
> interpretarse como evidencia suficiente para una implementación productiva.

---

## 1. Problema de negocio

Los modelos tradicionales de riesgo crediticio suelen apoyarse principalmente
en información estructurada, como pagos, atrasos, saldos y comportamiento
histórico.

Sin embargo, durante las interacciones con clientes pueden aparecer señales
lingüísticas previas al deterioro observable en estas variables, por ejemplo:

- pérdida de empleo;
- reducción de ingresos;
- problemas de liquidez;
- dificultad para realizar un pago;
- solicitudes de reestructura;
- diferimientos;
- gastos extraordinarios;
- situaciones familiares con impacto financiero.

FinPredict NLP explora la posibilidad de identificar este tipo de señales
mediante modelos de lenguaje antes de que se materialicen en indicadores
tradicionales de incumplimiento.

---

## 2. Objetivo

Clasificar textos asociados con la gestión de créditos hipotecarios en dos
categorías:

- `1 = SEÑAL_RIESGO`
- `0 = SIN_SEÑAL_RIESGO`

El objetivo del prototipo no es automatizar decisiones crediticias.

La solución se plantea como una herramienta de **priorización y apoyo a la
revisión humana**, que permita identificar posibles casos que requieran una
atención preventiva.

---

## 3. Dataset

Se construyó un dataset sintético y reproducible de **2,000 registros**:

- 1,000 textos con señal de riesgo;
- 1,000 textos sin señal de riesgo.

Las variables utilizadas son:

| Variable | Descripción |
|---|---|
| `id` | Identificador único del registro |
| `texto` | Texto sintético de interacción |
| `etiqueta` | Variable objetivo binaria |
| `clase` | Descripción de la clase |
| `tipo_senal` | Categoría temática del texto |
| `dificultad` | Nivel de dificultad lingüística |
| `expresion_local` | Indicador de presencia de lenguaje local |

El dataset incluye expresiones contextualizadas al español utilizado en México
para evaluar el comportamiento de los modelos ante variaciones lingüísticas.

La metodología de generación y validación está documentada en:

`data/README.md`

El script reproducible utilizado para construir el dataset se encuentra en:

`src/data_generation.py`

---

## 4. Estrategias evaluadas

Se compararon tres estrategias de clasificación zero-shot.

| Estrategia | Modelo | Procesamiento |
|---|---|---|
| Español | `Recognai/zeroshot_selectra_medium` | Texto original en español |
| Multilingüe | `MoritzLaurer/mDeBERTa-v3-base-xnli-multilingual-nli-2mil7` | Texto original en español |
| Inglés + traducción | `facebook/bart-large-mnli` | Traducción previa al inglés |

Para la estrategia basada en inglés se utilizó adicionalmente:

`Helsinki-NLP/opus-mt-es-en`

como modelo de traducción español → inglés.

Los criterios técnicos, lingüísticos, operativos y de negocio utilizados para
seleccionar los candidatos están documentados en:

`docs/model_selection.md`

---

## 5. Ecosistema Hugging Face

El proyecto utiliza principalmente los siguientes componentes del ecosistema
Hugging Face:

- **Hugging Face Hub:** acceso a modelos preentrenados y Model Cards.
- **Transformers:** implementación de pipelines de inferencia.
- **Model Cards:** revisión de características técnicas, idioma, licencia y
  compatibilidad de los modelos.
- **Autenticación mediante token de lectura:** acceso al Hub sin almacenar
  credenciales dentro del código versionado.

Hugging Face Spaces se identificó como una posible alternativa para una futura
demostración interactiva, aunque no forma parte del alcance actual.

---

## 6. Metodología experimental

El experimento se estructuró en tres etapas independientes:

| Etapa | Registros | Objetivo |
|---|---:|---|
| Piloto | 10 | Exploración inicial |
| Calibración | 60 | Selección de configuración semántica |
| Evaluación final | 1,930 | Comparación definitiva de modelos |

Durante la etapa inicial se probaron distintas formulaciones para las etiquetas
zero-shot.

Posteriormente se creó un conjunto formal de calibración para evitar favorecer
a un modelo particular.

La configuración común seleccionada fue:

`dificultad actual de pago`

vs.

`ausencia de dificultad actual de pago`

Una vez seleccionada, esta configuración permaneció fija durante la evaluación
final de los 1,930 registros.

---

## 7. Métricas de evaluación

Los modelos fueron comparados utilizando:

- Accuracy
- Precision
- Recall
- F1-score de la clase de riesgo
- F1 macro
- Matriz de confusión
- Latencia promedio
- Throughput

Además, se realizaron análisis segmentados considerando:

- dificultad lingüística;
- lenguaje estándar;
- lenguaje local.

El **recall de la clase `SEÑAL_RIESGO`** tiene especial relevancia para el
caso de uso, debido a que un falso negativo podría representar una oportunidad
de intervención preventiva no identificada.

Sin embargo, también se considera la precision, ya que una cantidad elevada de
falsos positivos podría generar carga operativa innecesaria.

---

## 8. Resultados finales

| Modelo | Accuracy | Precision | Recall | F1 riesgo | F1 macro | Latencia promedio |
|---|---:|---:|---:|---:|---:|---:|
| SELECTRA | 60.73 % | 56.02 % | 99.79 % | 71.76 % | 53.65 % | 5.13 ms |
| mDeBERTa | 66.42 % | 59.83 % | 100.00 % | 74.86 % | 62.16 % | 10.82 ms |
| **BART + traducción** | **74.25 %** | **66.01 %** | **100.00 %** | **79.52 %** | **72.42 %** | 61.41 ms |

Los tiempos corresponden al entorno experimental utilizado en Google Colab con
GPU y representan la latencia promedio observada durante el procesamiento por
lotes.

No deben interpretarse como tiempos garantizados para una implementación
productiva.

---

## 9. Análisis de lenguaje local

El desempeño se analizó separando textos estándar y textos con expresiones
locales.

### F1 macro

| Modelo | Lenguaje estándar | Lenguaje local |
|---|---:|---:|
| SELECTRA | 0.5376 | 0.5320 |
| mDeBERTa | 0.6238 | 0.6127 |
| **BART + traducción** | **0.7191** | **0.7442** |

Contrario a la hipótesis inicial, la estrategia basada en traducción no presentó
una caída de desempeño en los textos con lenguaje local incluidos en el
dataset.

BART + traducción obtuvo un F1 macro de **0.7191** en lenguaje estándar y de
**0.7442** en lenguaje local.

Este resultado se limita al conjunto sintético evaluado y no implica que toda
expresión regional o interacción real pueda traducirse sin pérdida semántica.

---

## 10. Análisis por dificultad lingüística

### F1 macro

| Dificultad | SELECTRA | mDeBERTa | BART + traducción |
|---|---:|---:|---:|
| Baja | 0.4124 | 0.4574 | **0.6131** |
| Media | 0.4885 | 0.5761 | **0.6752** |
| Alta | 0.5466 | 0.6588 | **0.7519** |

BART + traducción mantuvo el mejor desempeño en los tres segmentos.

Los niveles de dificultad fueron definidos mediante reglas lingüísticas
establecidas durante la construcción del dataset.

Por lo tanto, se utilizan como evidencia complementaria y no como una medida
absoluta de complejidad para cada arquitectura.

---

## 11. Trade-off entre calidad y eficiencia

Los resultados muestran un intercambio claro entre desempeño predictivo y
eficiencia computacional.

### SELECTRA

- menor latencia;
- mayor throughput;
- procesamiento directo del español;
- menor desempeño global;
- mayor cantidad relativa de falsos positivos.

### mDeBERTa

- desempeño superior a SELECTRA;
- procesamiento directo del español;
- recall de 100 %;
- latencia considerablemente menor que BART;
- alternativa intermedia entre calidad y eficiencia.

### BART + traducción

- mejor accuracy;
- mejor precision;
- recall de 100 %;
- mayor F1 de riesgo;
- mayor F1 macro;
- mejor desempeño en los análisis segmentados;
- mayor latencia;
- mayor complejidad operativa debido a la etapa adicional de traducción.

Los resultados muestran que una mejora en calidad predictiva implica un
incremento relevante en recursos y tiempo de procesamiento.

---

## 12. Modelo recomendado

Para la prueba de concepto se recomienda:

### BART + traducción

Arquitectura:

`Texto en español → Helsinki-NLP/opus-mt-es-en → facebook/bart-large-mnli → Clasificación`

La recomendación se sustenta en que esta estrategia obtuvo el mejor desempeño
global y mantuvo su ventaja en los análisis segmentados.

Resultados principales:

- Accuracy: **74.25 %**
- Precision de riesgo: **66.01 %**
- Recall de riesgo: **100 %**
- F1 de riesgo: **79.52 %**
- F1 macro: **72.42 %**

La principal desventaja es su eficiencia.

La latencia promedio experimental fue aproximadamente:

- 12 veces mayor que SELECTRA;
- 5.7 veces mayor que mDeBERTa.

Para un escenario donde la calidad de clasificación sea prioritaria y el
procesamiento pueda realizarse de manera asíncrona o por lotes, esta diferencia
puede ser aceptable dentro de una prueba de concepto.

Si la implementación priorizara velocidad, consumo computacional o mayor
simplicidad operativa, **mDeBERTa** sería la segunda alternativa recomendada.

---

## 13. Condición de uso

Los resultados obtenidos no justifican una automatización completa de
decisiones sobre clientes.

Aunque BART + traducción obtuvo un recall de 100 %, su precision de 66.01 %
indica que todavía existe una proporción relevante de falsos positivos.

Por este motivo, el uso propuesto es:

`Identificación de señal → Priorización → Revisión humana → Acción preventiva`

El modelo funcionaría como herramienta de apoyo y no como mecanismo autónomo
de decisión crediticia.

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
│   ├── README.md
│   ├── metricas_modelos.csv
│   ├── metricas_por_dificultad.csv
│   └── metricas_lenguaje_local.csv
│
└── src/
    └── data_generation.py
```

---

## 15. Ejecución

El proyecto fue desarrollado y probado en **Google Colab**.

Para reproducir el experimento:

1. Abrir `notebooks/00_dataset_generation_validation.ipynb` en Google Colab.
2. Ejecutar las celdas en orden para generar y validar el dataset.
3. Abrir `notebooks/01_model_comparison.ipynb` en Google Colab.
4. Activar un entorno de ejecución con GPU.
5. Ejecutar las celdas en orden.
6. Autenticarse en Hugging Face Hub cuando el notebook lo solicite.

Las dependencias necesarias se encuentran documentadas en:

`requirements.txt`

Los resultados generados por la evaluación se almacenan en:

`results/`

---

## 16. Reproducibilidad

La generación del dataset utiliza una semilla fija:

`SEED = 42`

La lógica de generación se encuentra separada del notebook en:

`src/data_generation.py`

Los notebooks documentan las etapas de:

`Generación → Validación → Calibración → Inferencia → Evaluación → Comparación`

Los tres modelos son evaluados utilizando el mismo conjunto final y una
configuración semántica común seleccionada previamente mediante el conjunto de
calibración.

---

## 17. Limitaciones

Los resultados deben interpretarse considerando las siguientes limitaciones:

- el dataset es sintético;
- los textos fueron construidos mediante reglas y patrones controlados;
- las métricas no representan desempeño sobre conversaciones reales;
- no se realizó fine-tuning específico para el dominio hipotecario;
- los scores generados por los clasificadores zero-shot no se interpretan como
  probabilidades calibradas;
- las expresiones locales evaluadas representan únicamente una muestra
  controlada del español utilizado en México;
- la traducción podría comportarse de manera diferente ante errores
  ortográficos, expresiones regionales adicionales o lenguaje real;
- las mediciones de eficiencia corresponden al entorno experimental utilizado.

---

## 18. Próximos pasos

Una siguiente fase del proyecto podría incorporar:

1. validación con información representativa del dominio;
2. etiquetado supervisado por especialistas;
3. fine-tuning del modelo seleccionado;
4. calibración de probabilidades y umbrales operativos;
5. análisis detallado de falsos positivos y falsos negativos;
6. evaluación de sesgos;
7. monitoreo de drift;
8. controles de privacidad, seguridad y trazabilidad;
9. integración con variables estructuradas de riesgo hipotecario.

Esta evolución permitiría explorar una arquitectura más amplia en la que las
señales obtenidas mediante NLP complementen los indicadores tradicionales de
riesgo.

---

## 19. Uso académico

Proyecto desarrollado para fines académicos dentro de la asignatura:

**Gestión de proyectos de inteligencia artificial**

El proyecto busca aplicar criterios técnicos y de negocio para la selección,
evaluación y recomendación de modelos de inteligencia artificial dentro de un
caso de uso empresarial.

---
## Reporte ejecutivo

El análisis comparativo completo del proyecto se encuentra disponible en:

[FinPredict NLP - Reporte Comparativo Actividad 4](A4_LBL_GP.pdf)
