# Estructura del Repositorio

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
