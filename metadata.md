# Resoluciones del Ministerio de Universidades (1995-2025)

## Dataset Summary
Este dataset contiene los titulares y resoluciones publicadas por el **Ministerio de Universidades** en el **BOE (Boletín Oficial del Estado)** entre los años 1995 y 2025. Cada registro incluye información sobre la disposición, su fecha de publicación y el órgano emisor.  

**Propósito:** Permitir el análisis temporal de resoluciones oficiales, identificar patrones de publicación y estudiar la distribución de titulares a lo largo de los años.  

**Contexto:** Los datos provienen de los sumarios diarios del BOE, que se encuentran disponibles como datos abiertos.  

---

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
```

## Dataset Details

**Fuente:** BOE (Boletín Oficial del Estado), datos abiertos: https://www.boe.es/datosabiertos/

**Periodo:** 1995-2025

**Número de registros:** Depende de la ejecución completa del script de extracción (extraccion_datos_boe.py)

## Variables / Columnas:

| Columna             | Significado                                                                            |
| ------------------- | -------------------------------------------------------------------------------------- |
| `ID_Disposicion`    | Identificador único de la disposición publicada en el BOE.                             |
| `Fecha_Publicacion` | Fecha exacta en la que se publicó la resolución o disposición en el BOE.               |
| `Organo_Emisor`     | Nombre del órgano o ministerio que emitió la disposición.                              |
| `Titulo_Semantico`  | Título descriptivo o titular de la disposición, extraído del BOE.                      |
| `Año`               | Año de publicación de la disposición.                                                  |
| `Año_Semana`        | Año ISO y semana ISO correspondiente a la fecha de publicación. |
| `Bloque_3dias`      | Índice que agrupa las fechas en bloques consecutivos de 3 días para análisis temporal. |

## Proceso de recolección:
Se utilizó el script extraccion_datos_boe.py para descargar y parsear los sumarios diarios del BOE mediante su API pública (https://www.boe.es/datosabiertos/api/api.php).

## Limitaciones:

La descarga completa puede tardar varias horas dependiendo de la conexión.

Algunas fechas no tienen BOE publicado, por lo que pueden faltar registros.

## Licencia

**Código:** MIT License. Puedes usar, copiar, modificar y distribuir el código libremente.

**Datos:** Dominio Público / AAL (CC BY Compatible), según la información oficial del BOE.

## Citation / Acknowledgements

**Datos extraídos del BOE:** https://www.boe.es/datosabiertos/

Agradecimientos al equipo docente y a Hugging Face por proporcionar la plataforma para datasets FAIR.
