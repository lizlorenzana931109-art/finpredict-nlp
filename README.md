# FinPredict NLP

Prototipo de Procesamiento de Lenguaje Natural para la identificación temprana
de señales de dificultad de pago en textos asociados con créditos hipotecarios.

> Proyecto académico desarrollado con datos sintéticos.  
> No contiene información real de clientes.

## Objetivo

Clasificar textos en:

- `SEÑAL_RIESGO`
- `SIN_SEÑAL_RIESGO`

El propósito es evaluar el uso de modelos preentrenados como apoyo para
priorizar posibles casos de riesgo y no para automatizar decisiones crediticias.

## Modelos evaluados

Se compararon tres estrategias mediante Hugging Face:

| Estrategia | Modelo |
|---|---|
| Español | `Recognai/zeroshot_selectra_medium` |
| Multilingüe | `MoritzLaurer/mDeBERTa-v3-base-xnli-multilingual-nli-2mil7` |
| Inglés + traducción | `facebook/bart-large-mnli` + `Helsinki-NLP/opus-mt-es-en` |

Los criterios de selección están documentados en:

`docs/model_selection.md`

## Dataset

Se utilizó un dataset sintético y reproducible de 2,000 registros:

- 1,000 con señal de riesgo;
- 1,000 sin señal de riesgo.

Incluye categorías de riesgo, dificultad lingüística y expresiones
contextualizadas al español utilizado en México.

Más información:

`data/README.md`

## Metodología experimental

La evaluación se dividió en:

| Etapa | Registros |
|---|---:|
| Piloto | 10 |
| Calibración | 60 |
| Evaluación final | 1,930 |

La configuración semántica fue seleccionada con el conjunto de calibración y
posteriormente se mantuvo fija durante la evaluación final.

## Resultados

| Modelo | Accuracy | Precision | Recall | F1 riesgo | F1 macro | Latencia |
|---|---:|---:|---:|---:|---:|---:|
| SELECTRA | 60.73 % | 56.02 % | 99.79 % | 71.76 % | 53.65 % | 5.13 ms |
| mDeBERTa | 66.42 % | 59.83 % | 100.00 % | 74.86 % | 62.16 % | 10.82 ms |
| **BART + traducción** | **74.25 %** | **66.01 %** | **100.00 %** | **79.52 %** | **72.42 %** | 61.41 ms |

Los resultados completos se encuentran en:

`results/`

## Modelo recomendado

Para la prueba de concepto se recomienda **BART + traducción** debido a que
obtuvo el mejor desempeño global y mantuvo su ventaja en los análisis por
dificultad lingüística y lenguaje local.

Su principal trade-off es la eficiencia: requiere una etapa adicional de
traducción y presentó una latencia considerablemente mayor.

Si el escenario priorizara eficiencia computacional, `mDeBERTa` sería la
segunda alternativa recomendada.

Debido a la precisión obtenida y al carácter sintético del dataset, la solución
se plantea como herramienta de priorización con supervisión humana y no como
mecanismo automático de decisión crediticia.

## Estructura del repositorio

```text
finpredict-nlp/
├── README.md
├── requirements.txt
├── data/
│   ├── README.md
│   └── finpredict_nlp_dataset.csv
├── docs/
│   └── model_selection.md
├── notebooks/
│   ├── 00_dataset_generation_validation.ipynb
│   └── 01_model_comparison.ipynb
├── results/
│   ├── README.md
│   ├── metricas_modelos.csv
│   ├── metricas_por_dificultad.csv
│   └── metricas_lenguaje_local.csv
└── src/
    └── data_generation.py
