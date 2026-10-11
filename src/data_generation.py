"""
FinPredict NLP
Generación reproducible del dataset sintético.

Este script construirá un conjunto de textos sintéticos relacionados con
interacciones de clientes hipotecarios para evaluar modelos preentrenados
de procesamiento de lenguaje natural.

El dataset final tendrá 2,000 registros balanceados:
- 1,000 registros con SEÑAL_RIESGO
- 1,000 registros con SIN_SEÑAL_RIESGO
"""

import random
from pathlib import Path

import pandas as pd


# ============================================================
# CONFIGURACIÓN GENERAL
# ============================================================

SEED = 42
TOTAL_REGISTROS = 2000
REGISTROS_RIESGO = 1000
REGISTROS_SIN_RIESGO = 1000


# Fijamos la semilla para garantizar reproducibilidad
random.seed(SEED)


# Ruta del archivo generado
OUTPUT_PATH = Path("data/finpredict_nlp_dataset.csv")
