# Estructura del Repositorio

El repositorio está organizado en dos entregas principales:

- **Entrega 1:** Preparación del dataset, extracción de datos y documentación técnica.  
- **Entrega 2:** Cálculo de indicadores (obligatorios y opcionales), limpieza de datos y análisis motivacional.  

Cada carpeta contiene tanto los **notebooks de análisis** como los **documentos de apoyo y resultados**.

La estructura sería:

```text
Proyecto_Universidades_BOE/
│
├── Entrega1/
│   ├── LICENSE
│   ├── README.md
│   ├── extraccion_datos_boe.py         # Script para la extracción y descarga de datos del BOE
│   ├── metadata.md                     # Descripción técnica del dataset y su estructura
│   └── requirements.txt                # Librerías necesarias para ejecutar el proyecto
│
├── Entrega2/
│   ├── Indicadores obligatorios/
│   │   ├── DCDC_Análisis_Volumen.ipynb       # Análisis del volumen temporal de publicaciones
│   │   ├── DCDC_Análisis_de_tópicos.ipynb    # Modelado de tópicos (LDA)
│   │   └── DCDC_Análisis_sentimiento.ipynb   # Análisis de sentimiento con modelos en español
│   │
│   ├── Indicadores opcionales/
│   │   └── DCDC_Pública_Privada.ipynb        # Clasificación y análisis por tipo de universidad
|   |   └── DCDC_Provincias.ipynb             # Clasificación y análisis por pertenencia a provincia
│   │
│   ├── Limpieza de datos/
│   │   └── DCDC_E2_EDA.ipynb             # Exploración y limpieza de datos
│   │
│   └── img_e2/                           # Carpeta con imágenes y gráficos generados 
|   └── data_cleaning.md                  # Documentación del proceso de limpieza
│   └── motivation.md                         # Documento de motivación, hipótesis y justificación
│
└── README.md                                 # Descripción general del proyecto y estructura del repo
```
