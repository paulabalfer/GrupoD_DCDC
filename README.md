# Estructura del Repositorio y Reproducibilidad

## Descripción del proyecto

AQUÏ EL ABSTRACR PAULA

## Instrucciones de Reproducción

Para reproducir este proyecto desde cero, sigue este orden de ejecución:

## Acceso a los Datos (Hugging Face)

El dataset completo y procesado está disponible públicamente en Hugging Face. Esto permite replicar los notebooks de análisis sin necesidad de ejecutar nuevamente la extracción de datos crudos.

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/pauDCDC/boe_universidades)

🔗 **Enlace directo:** [pauDCDC/boe_universidades](https://huggingface.co/datasets/pauDCDC/boe_universidades)

---

### 1. Configuración del Entorno
Clona el repositorio e instala las dependencias necesarias:

```bash
git clone [https://github.com/paulabalfer/GrupoD_DCDC.git](https://github.com/paulabalfer/GrupoD_DCDC.git)
cd GrupoD_DCDC
pip install -r requirements.txt
python -m nltk.downloader stopwords punkt wordnet omw-1.4 vader_lexicon
```

### 2. Generación del Dataset (Entrega 1 y 2)
> **Nota:** Si has descargado los datos de Hugging Face, puedes saltar al paso 3.

1.  **Extracción:** Ejecuta `Extracción de datos y creación de dataset/extraccion_datos_boe.py` para descargar los datos crudos.
2.  **Limpieza:** Ejecuta `Indicadores e hipótesis/Limpieza de datos/DCDC_E2_EDA.ipynb`.

### 3. Generación de Indicadores (Entrega 2)
Una vez tengas los datos procesados, ejecuta los notebooks para generar las métricas:

1.  **Indicadores Obligatorios:** Ejecuta los notebooks dentro de `Indicadores e hipótesis/Indicadores obligatorios/` (Volumen, Sentimiento, Tópicos).
2.  **Consolidación:** Ejecuta `Indicadores e hipótesis/DCDC_Preparacion_conjunto_final.ipynb` para unir todas las métricas en el dataset final.

### 4. Modelos Temporales (Entrega 3)
Con el dataset final listo, ejecuta los modelos predictivos:

1.  **Preprocesado temporal:** Ejecuta `Análisis temporal/DCDC_P3_Preprocesado_Datos.ipynb`.
2.  **Modelos:** Ejecuta los notebooks `Análisis temporal/DCDC_P3_ARIMA_SARIMAX_PROPHET.ipynb` y `Análisis temporal/DCDC_P3_GARCH.ipynb`.

## Estructura del repositorio
El repositorio está organizado en dos entregas principales:

- **Extracción de datos y creación de dataset:** Preparación del dataset, extracción de datos y documentación técnica.  
- **Indicadores e hipótesis:** Cálculo de indicadores (obligatorios y opcionales), limpieza de datos y análisis motivacional.
- **Análisis temporal:** Análisis de volatilidad y tendencias temporales.

Cada carpeta contiene tanto los **notebooks de análisis** como los **documentos de apoyo y resultados**.

La estructura sería:

```text
Proyecto_Universidades_BOE/
│
├── data/
|   ├── raw/
|   |   └── dataset_boe_universidades.csv               # Conjunto de datos original (Resultado de la entrega 1) 
|   └── processed/
|   |   └── dataset_boe_universidades_processed.csv     # Conjunto de datos procesado y exclusivamente numérico (Resultado de la entrega 2)
|   └── indicators/
|       └── indicators_madrid_daily.csv                 # Conjunto de datos con variable temporal diaria procesada (Archivo intermedio necesario en la entrega 3)
|       └── indicators_madrid_annual.csv                # Conjunto de datos con variable temporal anual procesada (Archivo intermedio necesario en la entrega 3)
|
├── Extracción de datos y creación de dataset/
│   ├── LICENSE
│   ├── README.md
│   ├── extraccion_datos_boe.py         # Script para la extracción y descarga de datos del BOE
│   └── metadata.md                     # Descripción técnica del dataset y su estructura
│    
│
├── Indicadores e hipótesis/
│   ├── Indicadores obligatorios/
│   │   ├── DCDC_Análisis_Volumen.ipynb          # Análisis del volumen temporal de publicaciones
│   │   └── DCDC_Análisis_sentimiento.ipynb      # Análisis de sentimiento con modelos en español
│   │   └── DCDC_Análisis_de_tópicos_LDA.ipynb   # Modelado de tópicos con LDA
│   │
│   ├── Indicadores opcionales/
│   │   └── DCDC_Pública_Privada.ipynb              # Clasificación y análisis por tipo de universidad
|   |   └── DCDC_Provincias.ipynb                   # Clasificación y análisis por pertenencia a provincia
|   |   └── DCDC_Modelos_Zeroshot_Learning.ipynb    # Clasificación y análisis por temática con modelos asistidos por LLMs
│   │
│   ├── Limpieza de datos/
│   │   └── DCDC_E2_EDA.ipynb                     # Exploración y limpieza de datos
│   │
│   └── img_e2/                                   # Carpeta con imágenes y gráficos generados 
│   └── DCDC_Preparacion_conjunto_final.ipynb     # Unión de todos los análisis y reconstrucción del dataset final + análisis de hipótesis
|   └── data_cleaning.md                          # Documentación del proceso de limpieza
│   └── motivation.md                             # Documento de motivación, hipótesis y justificación
├── Análisis temporal/
│   ├── imgs/                                    # Carpeta con imágenes y gráficos generados 
│   ├── analysis.md                              # Memoria de la entrega 3
│   ├── DCDC_P3_Preprocesado_Datos.ipynb         # Notebook con visualizaciones y preparación de los datos
│   ├── DCDC_P3_ARIMA_SARIMAX_PROPHET.ipynb      # Notebook con análisis ARIMAX y SARIMAX
│   └── DCDC_P3_GARCH.ipynb                      # Notebook con análisis de volatilidad con ARCH  y GARCH
│
├── .gitignore                                   # Archivos excluidos del control de versiones
├── LICENSE                                      # Licencia del proyecto
├── README.md                                    # Descripción general del proyecto y estructura del repositorio
├── requirements.txt                             # Librerías necesarias para ejecutar el proyecto
└── Report.pdf                                   # Entrega 4. Descripción del proyecto final completo.
```
