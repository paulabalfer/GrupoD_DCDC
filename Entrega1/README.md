---
license: cc-by-4.0
task_categories:
- text-classification
language:
- es
tags:
- legal
pretty_name: Resoluciones del Ministerio de Universidades (1995-2025)
size_categories:
- 1K<n<10K
---

# Dataset Card for Resoluciones del Ministerio de Universidades (1995-2025)

## Dataset Details

### Dataset Description

Este dataset contiene los titulares y resoluciones publicadas por el Ministerio de Universidades en el BOE (Boletín Oficial del Estado) entre 1995 y 2025. Cada registro incluye información sobre la disposición, su fecha de publicación, el órgano emisor y un índice que agrupa las fechas en bloques consecutivos de 3 días para análisis temporal.

- **Curated by:** Paula Ballesteros, Irene Palomares y Julia Sáenz
- **Language(s) (NLP):** Español
- **License:** Datos: Dominio Público / AAL (CC BY Compatible). Código: MIT License

### Dataset Sources

- **Repository:** [https://github.com/paulabalfer/GrupoD_DCDC](https://github.com/paulabalfer/GrupoD_DCDC)
- **Source:** BOE – sumarios diarios vía API pública

## Uses

### Direct Use

- Análisis temporal de resoluciones oficiales
- Estudios de patrones de publicación del Ministerio de Universidades
- Agrupación por bloques de 3 días para análisis de frecuencia temporal

### Out-of-Scope Use

- Datos personales o información privada (no contiene)
- Uso comercial sin respetar la licencia de los datos del BOE

## Dataset Structure

- **Formato:** CSV
- **Número de columnas:** 7
- **Número de registros:** Depende de la ejecución completa del script `extraccion_datos_boe.py`

### Columns / Features

| Columna          | Tipo     | Descripción |
|-----------------|---------|-------------|
| ID_Disposicion  | string  | Identificador único de la disposición publicada en el BOE. |
| Fecha_Publicacion | datetime | Fecha exacta en la que se publicó la resolución o disposición. |
| Organo_Emisor   | string  | Nombre del órgano o ministerio que emitió la disposición. |
| Titulo_Semantico | string  | Título descriptivo o titular de la disposición. |
| Año             | int     | Año de publicación de la disposición. |
| Año_Semana      | string  | Año ISO y semana ISO correspondiente a la fecha de publicación. |
| Bloque_3dias    | int     | Índice que agrupa las fechas en bloques consecutivos de 3 días. |

## Dataset Creation

### Curation Rationale

Se creó para analizar la distribución temporal de resoluciones del Ministerio de Universidades y estudiar patrones de publicación.

### Source Data

- **Data Collection and Processing:** Se utilizó el script `extraccion_datos_boe.py` que descarga y parsea los sumarios diarios del BOE mediante su API pública. Los datos se filtraron para el Ministerio de Universidades.
- **Source data producers:** BOE (sumarios oficiales publicados diariamente)

### Annotations

No aplica, los datos son extraídos directamente del BOE sin anotaciones manuales.

### Personal and Sensitive Information

No contiene datos personales ni sensibles.

## Bias, Risks, and Limitations

- Algunas fechas pueden no tener publicaciones, por lo que faltan registros.
- El dataset solo incluye el Ministerio de Universidades.

### Recommendations

- Puede tardar varias horas en descargarse completo.
- Ajustar las fechas en el script si se interrumpe la descarga.

## Citation / Acknowledgements

- Datos: BOE – Dominio Público / AAL (CC BY Compatible)
- Código: MIT License

## Reproducibility
Para recrear este dataset, ejecuta el archivo `extraccion_datos_boe.py`:

```bash
# Clonar el repositorio
git clone https://github.com/paulabalfer/GrupoD_DCDC.git
cd GrupoD_DCDC

# Crear un entorno virtual
python -m venv venv

# Activar el entorno virtual
source venv/Scripts/activate   # Windows Git Bash
# source venv/bin/activate     # Mac/Linux

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar el script de extracción
python extraccion_datos_boe.py
````

Esto generará un archivo csv: dataset_boe_universidades.csv.


## How to use

Para cargar y explorar el dataset en Python:

```python
import pandas as pd

# Cargar el dataset
df = pd.read_csv("dataset_boe_universidades.csv")

# Ver los primeros registros
print(df.head())

# Información general del dataset
print(df.info())

# Agrupar por bloque de 3 días para realizar análisis temporal
bloques = df.groupby('Bloque_3dias')
for bloque, datos in bloques:
    print(f"Bloque {bloque} contiene {len(datos)} registros")
    print(datos.head())
```
