# Resoluciones del Ministerio de Universidades (1995-2025)

## Dataset Summary
Este dataset contiene los titulares y resoluciones publicadas por el **Ministerio de Universidades** en el **BOE (Boletín Oficial del Estado)** entre los años 1995 y 2025. Cada registro incluye información sobre la disposición, su fecha de publicación y el órgano emisor.  

**Propósito:** Permitir el análisis temporal de resoluciones oficiales, identificar patrones de publicación y estudiar la distribución de titulares a lo largo de los años.  

**Contexto:** Los datos provienen de los sumarios diarios del BOE, que se encuentran disponibles como datos abiertos.  

---

## Dataset Structure
- Formato: CSV
- Número de columnas: 7
- Número de registros: depende de la ejecución completa del script `extraccion_datos_boe.py`

**Features / Columnas:**

| Columna           | Tipo     | Descripción |
|------------------|---------|------------|
| `ID_Disposicion` | string  | Identificador único de la disposición publicada en el BOE. |
| `Fecha_Publicacion` | datetime | Fecha exacta en la que se publicó la resolución o disposición en el BOE. |
| `Organo_Emisor`  | string  | Nombre del órgano o ministerio que emitió la disposición. |
| `Titulo_Semantico` | string | Título descriptivo o titular de la disposición, extraído del BOE. |
| `Año`            | int     | Año de publicación de la disposición. |
| `Año_Semana`     | string  | Año ISO y semana ISO correspondiente a la fecha de publicación (por ejemplo, 2025-42). |
| `Bloque_3dias`   | int     | Índice que agrupa las fechas en bloques consecutivos de 3 días para análisis temporal. |

---

## Reproducción
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


## Collection and Preprocessing

Se utilizó el script extraccion_datos_boe.py para descargar y parsear los sumarios diarios del BOE mediante su API pública.

### Notas sobre la recolección:

- La descarga completa puede tardar varias horas dependiendo de la conexión.

- Algunas fechas no tienen BOE publicado, por lo que pueden faltar registros.

- Los datos fueron filtrados para el Ministerio de Universidades únicamente.

## Licencia

	- Código: MIT License; Puedes usar, copiar, modificar y distribuir el código libremente.
	- Datos extraídos del BOE: Dominio Público / AAL (CC BY Compatible) según la información oficial del BOE.
## Notas
	- La descarga completa (1995-2025) puede tardar varias horas dependiendo de la conexión.
	- Si se interrumpe la ejecución puedes ajustar las fechas de inicio y fin en el script para reanudar la descarga.
