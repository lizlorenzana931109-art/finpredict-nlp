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

# ============================================================
# DISTRIBUCIÓN DE CATEGORÍAS
# ============================================================

DISTRIBUCION_RIESGO = {
    "perdida_empleo": 140,
    "reduccion_ingresos": 140,
    "problemas_liquidez": 140,
    "dificultad_pago": 120,
    "reestructura": 120,
    "diferimiento": 100,
    "gastos_extraordinarios": 90,
    "quita": 80,
    "dificultades_familiares": 70,
}


DISTRIBUCION_SIN_RIESGO = {
    "confirmacion_pago": 180,
    "aclaracion_pago": 150,
    "estado_cuenta": 140,
    "consulta_informacion": 140,
    "actualizacion_datos": 100,
    "situacion_hipotetica": 120,
    "situacion_resuelta": 100,
    "consulta_preventiva": 70,
}


# ============================================================
# VALIDACIONES DE CONFIGURACIÓN
# ============================================================

assert sum(DISTRIBUCION_RIESGO.values()) == REGISTROS_RIESGO, (
    "La distribución de registros con riesgo no suma 1,000."
)

assert sum(DISTRIBUCION_SIN_RIESGO.values()) == REGISTROS_SIN_RIESGO, (
    "La distribución de registros sin riesgo no suma 1,000."
)

assert REGISTROS_RIESGO + REGISTROS_SIN_RIESGO == TOTAL_REGISTROS, (
    "El total de registros configurados no coincide con TOTAL_REGISTROS."
)

# ============================================================
# BANCOS DE LENGUAJE - SEÑAL DE RIESGO
# ============================================================

BANCOS_RIESGO = {

    "perdida_empleo": {
        "situaciones": [
            "perdí mi empleo",
            "me quedé sin trabajo",
            "terminó mi contrato laboral",
            "me despidieron recientemente",
            "actualmente estoy desempleado",
            "dejé de recibir ingresos por mi trabajo",
            "ya no cuento con un empleo estable",
            "me quedé sin chamba",
        ],
        "consecuencias": [
            "no podré cubrir la mensualidad completa",
            "necesito revisar alternativas para pagar el crédito",
            "tendré dificultades para realizar el siguiente pago",
            "no cuento con ingresos suficientes para cubrir la mensualidad",
            "me preocupa no poder pagar este mes",
            "necesito alguna opción temporal para continuar pagando",
        ],
    },

    "reduccion_ingresos": {
        "situaciones": [
            "mis ingresos disminuyeron este mes",
            "me redujeron el sueldo",
            "ahora recibo menos ingresos que antes",
            "me redujeron las horas de trabajo",
            "mis comisiones bajaron considerablemente",
            "este mes recibí menos dinero",
            "mis ingresos familiares disminuyeron",
        ],
        "consecuencias": [
            "podría tener dificultades para cubrir la mensualidad",
            "no sé si podré completar el pago",
            "necesito revisar opciones para reducir temporalmente el pago",
            "el pago del crédito está comenzando a complicarse",
            "probablemente no alcance a cubrir la mensualidad completa",
        ],
    },

    "problemas_liquidez": {
        "situaciones": [
            "este mes tengo problemas de liquidez",
            "no cuento con suficiente efectivo disponible",
            "se me juntaron varios pagos",
            "ando corto esta quincena",
            "mis gastos de este mes fueron mayores de lo esperado",
            "por ahora no tengo suficiente dinero disponible",
            "traigo varios compromisos de pago al mismo tiempo",
        ],
        "consecuencias": [
            "no sé si podré cubrir la mensualidad",
            "necesito algunos días adicionales para realizar el pago",
            "me está costando completar el monto del crédito",
            "quisiera revisar alguna alternativa temporal",
            "el siguiente pago podría retrasarse",
        ],
    },

    "dificultad_pago": {
        "situaciones": [
            "estoy teniendo dificultades para realizar el pago",
            "no he logrado reunir el monto completo de la mensualidad",
            "creo que este mes me voy a atrasar",
            "no voy a completar el pago en la fecha establecida",
            "me está costando cubrir la mensualidad",
            "este mes no me alcanza para pagar todo",
        ],
        "consecuencias": [
            "quisiera conocer qué opciones tengo",
            "necesito apoyo para evitar un atraso mayor",
            "quiero revisar alguna alternativa de pago",
            "me preocupa que la deuda siga aumentando",
            "necesito encontrar una solución antes de la siguiente fecha de pago",
        ],
    },

    "reestructura": {
        "situaciones": [
            "necesito solicitar una reestructura del crédito",
            "quiero revisar si puedo reestructurar mi deuda",
            "la mensualidad actual ya es difícil de cubrir",
            "necesito modificar las condiciones actuales del crédito",
            "quisiera reducir el monto de mis pagos mensuales",
        ],
        "consecuencias": [
            "mis ingresos actuales ya no me permiten pagar igual que antes",
            "necesito una alternativa que se ajuste a mi situación económica",
            "quiero evitar caer en incumplimiento",
            "mi capacidad de pago disminuyó",
            "necesito una opción para mantener el crédito al corriente",
        ],
    },

    "diferimiento": {
        "situaciones": [
            "quisiera solicitar un diferimiento",
            "necesito posponer temporalmente el siguiente pago",
            "quiero saber si puedo aplazar una mensualidad",
            "necesito algunos días adicionales para cubrir el crédito",
            "por ahora necesito diferir el pago",
        ],
        "consecuencias": [
            "este mes tuve una reducción temporal de ingresos",
            "no podré pagar en la fecha habitual",
            "mi situación económica de este mes se complicó",
            "necesito tiempo para recuperar liquidez",
            "quiero evitar que el crédito caiga en atraso",
        ],
    },

    "gastos_extraordinarios": {
        "situaciones": [
            "tuve un gasto inesperado este mes",
            "surgió una emergencia familiar",
            "tuve que cubrir gastos que no tenía contemplados",
            "me cayó un gasto fuerte este mes",
            "una emergencia consumió parte de mis ingresos",
        ],
        "consecuencias": [
            "no sé si podré completar la mensualidad",
            "el pago del crédito podría retrasarse",
            "necesito revisar alguna alternativa temporal",
            "me quedé con menos recursos para cubrir el crédito",
            "este mes será difícil realizar el pago completo",
        ],
    },

    "quita": {
        "situaciones": [
            "quisiera saber si existe alguna opción de quita",
            "necesito negociar una reducción del saldo",
            "quiero revisar alternativas para liquidar con un monto menor",
            "mi situación económica ya no me permite cubrir la deuda como antes",
            "quisiera conocer opciones para negociar el adeudo",
        ],
        "consecuencias": [
            "actualmente tengo dificultades económicas importantes",
            "ya no puedo mantener el nivel actual de pagos",
            "necesito una solución para regularizar mi situación",
            "mi capacidad de pago disminuyó considerablemente",
            "quiero evitar que la deuda continúe creciendo",
        ],
    },

    "dificultades_familiares": {
        "situaciones": [
            "mi familia está atravesando una situación económica complicada",
            "uno de los ingresos principales de mi hogar se perdió",
            "tuvimos gastos familiares inesperados",
            "actualmente dependen más personas de mis ingresos",
            "los gastos de mi hogar aumentaron considerablemente",
        ],
        "consecuencias": [
            "me está resultando difícil cubrir la mensualidad",
            "necesito revisar alternativas de pago",
            "no sé si podré mantener los pagos en las mismas condiciones",
            "el presupuesto familiar ya no alcanza como antes",
            "podría presentar dificultades con los próximos pagos",
        ],
    },
}

# ============================================================
# BANCOS DE LENGUAJE - SIN SEÑAL DE RIESGO
# ============================================================

BANCOS_SIN_RIESGO = {

    "confirmacion_pago": {
        "situaciones": [
            "realicé el pago de mi mensualidad",
            "ya pagué la mensualidad correspondiente",
            "hice una transferencia para cubrir el crédito",
            "el pago ya salió de mi cuenta",
            "realicé el pago mediante SPEI",
            "ya cubrí el monto completo de este mes",
        ],
        "contextos": [
            "quiero confirmar que ya fue aplicado",
            "necesito validar que aparezca correctamente",
            "quisiera confirmar que el crédito está al corriente",
            "solo necesito verificar que el movimiento se refleje",
            "quiero asegurarme de que el pago quedó registrado",
        ],
    },

    "aclaracion_pago": {
        "situaciones": [
            "mi pago todavía no aparece reflejado",
            "realicé el pago pero aún no se visualiza",
            "el SPEI ya salió de mi cuenta",
            "hice el pago ayer y todavía aparece pendiente",
            "la mensualidad fue cubierta pero necesito una aclaración",
        ],
        "contextos": [
            "cuento con el comprobante de la operación",
            "el monto fue cubierto completamente",
            "solo necesito revisar la aplicación del movimiento",
            "quiero confirmar el tiempo de procesamiento",
            "no tengo ningún pago pendiente adicional",
        ],
    },

    "estado_cuenta": {
        "situaciones": [
            "necesito una copia de mi estado de cuenta",
            "quiero consultar los movimientos de mi crédito",
            "quisiera descargar mi estado de cuenta",
            "necesito revisar el saldo actualizado",
            "quiero consultar el detalle de mis mensualidades",
        ],
        "contextos": [
            "es únicamente para llevar mi control personal",
            "quiero revisar que toda la información sea correcta",
            "necesito el documento para mis registros",
            "no tengo ningún problema con los pagos",
            "solo quiero consultar la información disponible",
        ],
    },

    "consulta_informacion": {
        "situaciones": [
            "quiero conocer la fecha de mi siguiente pago",
            "necesito información sobre mi crédito",
            "quisiera consultar las condiciones de mi financiamiento",
            "quiero saber cuánto saldo tengo pendiente",
            "necesito conocer el monto de mi próxima mensualidad",
            "quisiera revisar el calendario de pagos",
        ],
        "contextos": [
            "mis pagos se encuentran al corriente",
            "es una consulta informativa",
            "solo estoy organizando mis próximos pagos",
            "no tengo dificultades para cubrir la mensualidad",
            "quiero llevar un mejor control de mis finanzas",
        ],
    },

    "actualizacion_datos": {
        "situaciones": [
            "necesito actualizar mi número telefónico",
            "quiero cambiar mi correo electrónico",
            "quisiera actualizar mis datos de contacto",
            "cambié de domicilio y necesito actualizarlo",
            "quiero modificar la cuenta asociada a mis pagos",
        ],
        "contextos": [
            "el crédito continúa pagándose normalmente",
            "no existe ningún problema con mis mensualidades",
            "solo necesito mantener mis datos actualizados",
            "mis pagos se encuentran al corriente",
            "es únicamente una actualización administrativa",
        ],
    },

    "situacion_hipotetica": {
        "situaciones": [
            "quiero saber qué pasaría si perdiera mi empleo",
            "¿qué opciones existirían si algún día no pudiera pagar?",
            "quisiera saber qué ocurriría si mis ingresos disminuyeran",
            "¿existe algún apoyo en caso de quedar desempleado?",
            "quiero conocer las alternativas si en el futuro tuviera problemas económicos",
            "¿qué sucede con el crédito si una persona pierde su trabajo?",
        ],
        "contextos": [
            "actualmente no tengo dificultades financieras",
            "mis pagos se encuentran al corriente",
            "solo quiero conocer las opciones de forma preventiva",
            "por ahora puedo continuar pagando normalmente",
            "es únicamente una consulta para estar informado",
        ],
    },

    "situacion_resuelta": {
        "situaciones": [
            "tuve un atraso el mes pasado pero ya lo regularicé",
            "estuve desempleado temporalmente pero ya tengo trabajo nuevamente",
            "tuve problemas económicos pero la situación ya se estabilizó",
            "el mes pasado andaba corto pero ya cubrí todos mis pagos",
            "tuve una reducción temporal de ingresos pero ya se normalizaron",
            "me atrasé unos días pero el crédito ya está al corriente",
        ],
        "contextos": [
            "actualmente no tengo pagos pendientes",
            "ya puedo continuar pagando normalmente",
            "la situación se encuentra completamente regularizada",
            "todos los pagos pendientes fueron cubiertos",
            "mi capacidad de pago ya se estabilizó",
        ],
    },

    "consulta_preventiva": {
        "situaciones": [
            "quiero conocer las opciones de reestructura disponibles",
            "quisiera saber cómo funciona un diferimiento",
            "quiero entender qué significa una quita",
            "necesito conocer qué apoyos existen ante una emergencia",
            "quiero saber qué alternativas ofrece el crédito ante una dificultad futura",
        ],
        "contextos": [
            "no estoy solicitando ninguna de estas opciones actualmente",
            "mi crédito se encuentra al corriente",
            "solo quiero conocer esta información de manera preventiva",
            "actualmente puedo cubrir mis pagos sin problema",
            "es información que quiero conocer para estar preparado",
        ],
    },
}  

# ============================================================
# VARIACIONES LINGÜÍSTICAS
# ============================================================

INICIOS = [
    "",
    "Quisiera comentar que ",
    "Necesito informar que ",
    "Actualmente ",
    "Por el momento ",
    "En este momento ",
    "Quería comentar que ",
]

CONECTORES = [
    " y ",
    ", por lo que ",
    "; por eso, ",
    ". Además, ",
    ", así que ",
    ", debido a esto ",
]

CIERRES = [
    "",
    ".",
    ". Quisiera conocer qué alternativas existen.",
    ". Agradezco orientación sobre esta situación.",
    ". Quisiera saber qué opciones tengo disponibles.",
]


# Expresiones que utilizaremos para identificar lenguaje
# informal o contextualizado al español de México.
EXPRESIONES_LOCALES = [
    "me quedé sin chamba",
    "ando corto",
    "nomás",
    "checar"
    "esta quincena",
    "se me juntaron varios pagos",
    "me cayó un gasto fuerte",
    "no me alcanza",
    "me voy a atrasar",
    "el SPEI ya salió",
]

PREFIJOS_LOCALES_NEUTROS = [
    "Nomás para comentar: ",
    "Quería checar algo: ",
]

# ============================================================
# FUNCIONES DE GENERACIÓN
# ============================================================

def construir_texto(situacion, complemento):
    """
    Construye una frase combinando diferentes elementos
    lingüísticos para aumentar la variedad del dataset.
    """

    inicio = random.choice(INICIOS)
    conector = random.choice(CONECTORES)

    # La mayoría de las frases no necesitarán un cierre adicional.
    cierre = random.choices(
        population=CIERRES,
        weights=[45, 30, 10, 8, 7],
        k=1,
    )[0]

    texto = f"{inicio}{situacion}{conector}{complemento}{cierre}"

    # Limpieza básica de espacios
    texto = " ".join(texto.split())

    # Primera letra en mayúscula
    texto = texto[0].upper() + texto[1:]

    return texto
  # ============================================================
# FUNCIONES AUXILIARES
# ============================================================

def detectar_expresion_local(texto):
    """
    Detecta si el texto contiene alguna de las expresiones
    locales definidas para el contexto mexicano.
    """
    texto_minusculas = texto.lower()

    return int(
        any(
            expresion.lower() in texto_minusculas
            for expresion in EXPRESIONES_LOCALES
        )
    )


def asignar_dificultad(texto, tipo_senal):
    """
    Asigna dificultad lingüística con base en características
    observables del texto y del contexto.

    - Alta: negaciones, hipótesis, situaciones resueltas,
      lenguaje local o estructuras con contraste temporal.
    - Media: lenguaje indirecto, incertidumbre o solicitudes
      que requieren interpretación contextual.
    - Baja: intención explícita y directa.
    """

    texto_lower = texto.lower()

    marcadores_alta = [
        "no tengo",
        "no estoy",
        "no me",
        "pero ya",
        "pero el",
        "si algún día",
        "si en el futuro",
        "si perdiera",
        "si tuviera",
        "actualmente no",
        "por ahora puedo",
        "ya se estabilizó",
        "ya lo regularicé",
        "ya está al corriente",
    ]

    marcadores_media = [
        "podría",
        "probablemente",
        "me preocupa",
        "quisiera",
        "alternativa",
        "temporal",
        "no sé si",
        "comenzando a",
        "necesito revisar",
    ]

    categorias_alta = {
        "situacion_hipotetica",
        "situacion_resuelta",
        "consulta_preventiva",
    }

    # Casos contextualmente complejos
    if tipo_senal in categorias_alta:
        return "alta"

    if detectar_expresion_local(texto) == 1:
        return "alta"

    if any(marcador in texto_lower for marcador in marcadores_alta):
        return "alta"

    # Casos de interpretación intermedia
    if any(marcador in texto_lower for marcador in marcadores_media):
        return "media"

    return "baja"

# ============================================================
# GENERACIÓN DE REGISTROS POR CLASE
# ============================================================

def generar_registros_clase(
    bancos,
    distribucion,
    etiqueta,
    clase,
    nombre_complemento,
):
    """
    Genera los registros correspondientes a una clase.

    Evita textos duplicados dentro de la generación.
    """

    registros = []
    textos_generados = set()

    for tipo_senal, cantidad in distribucion.items():

        banco = bancos[tipo_senal]

        situaciones = banco["situaciones"]
        complementos = banco[nombre_complemento]

        generados_categoria = 0
        intentos = 0
        max_intentos = cantidad * 100

        while generados_categoria < cantidad:

            intentos += 1

            if intentos > max_intentos:
                raise RuntimeError(
                    f"No fue posible generar suficientes textos únicos "
                    f"para la categoría: {tipo_senal}"
                )

            situacion = random.choice(situaciones)
            complemento = random.choice(complementos)

            texto = construir_texto(
                situacion=situacion,
                complemento=complemento,
            )

            # Evitamos textos idénticos
            if texto in textos_generados:
                continue

            textos_generados.add(texto)

            registro = {
                "texto": texto,
                "etiqueta": etiqueta,
                "clase": clase,
                "tipo_senal": tipo_senal,
                "dificultad": asignar_dificultad(
                    texto=texto,    
                    tipo_senal=tipo_senal,
                    ),
                "expresion_local": detectar_expresion_local(texto),
            }

            registros.append(registro)

            generados_categoria += 1

    return registros

# ============================================================
# GENERACIÓN DEL DATASET COMPLETO
# ============================================================

def generar_dataset():
    """
    Genera el dataset completo de FinPredict NLP.
    """

    # Generación de registros con señal de riesgo
    registros_riesgo = generar_registros_clase(
        bancos=BANCOS_RIESGO,
        distribucion=DISTRIBUCION_RIESGO,
        etiqueta=1,
        clase="SEÑAL_RIESGO",
        nombre_complemento="consecuencias",
    )

    # Generación de registros sin señal de riesgo
    registros_sin_riesgo = generar_registros_clase(
        bancos=BANCOS_SIN_RIESGO,
        distribucion=DISTRIBUCION_SIN_RIESGO,
        etiqueta=0,
        clase="SIN_SEÑAL_RIESGO",
        nombre_complemento="contextos",
    )

    # Unimos ambas clases
    registros = registros_riesgo + registros_sin_riesgo

    # Mezclamos el orden de los registros
    random.shuffle(registros)

    # Creamos DataFrame
    df = pd.DataFrame(registros)

    # Creamos identificador único después de mezclar
    df.insert(
        0,
        "id",
        [f"FP{i:04d}" for i in range(1, len(df) + 1)],
    )

    return df

# ============================================================
# EJECUCIÓN
# ============================================================

if __name__ == "__main__":

    df = generar_dataset()

    # Creamos la carpeta de salida si no existe
    OUTPUT_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    # Guardamos el dataset
    df.to_csv(
        OUTPUT_PATH,
        index=False,
        encoding="utf-8-sig",
    )

    print("Dataset generado correctamente.")
    print(f"Total de registros: {len(df)}")
    print()
    print("Distribución por clase:")
    print(df["clase"].value_counts())
    print()
    print(f"Archivo guardado en: {OUTPUT_PATH}")
