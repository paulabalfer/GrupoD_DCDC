# Resoluciones del Ministerio de Universidades de 1995 a 2025

## Descripción
El conjunto de datos contiene los titulares publicados por el Ministerio de Universidades en el BOE (Boletín Oficial del Estado) entre los años 1995 y 2025. Cada dato incluye:

- ID de disposición en el BOE
- Fecha de publicación exacta
- Órgano emisor
- Título semántico
- Información de la semana ISO y año
- Bloques de 3 días consecutivos para análisis temporal

Este dataset permite estudiar la distribución temporal de las resoluciones y publicaciones oficiales del Ministerio de Universidades.

## Reproducción
Para recrear este dataset, ejecuta el archivo `extraccion_datos_boe.py`:

```bash
# Clonar el repositorio
git clone https://github.com/paulabalfer/GrupoD_DCDC.git
cd GrupoD_DCDC

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar el script de extracción
python extraccion_datos_boe.py
````

Esto generará un archivo csv: dataset_boe_universidades.csv.

## Licencia

	- Código: MIT License; Puedes usar, copiar, modificar y distribuir el código libremente.
	- Datos extraídos del BOE: Dominio Público / AAL (CC BY Compatible) según la información oficial del BOE.
## Notas
	- La descarga completa (1995-2025) puede tardar varias horas dependiendo de la conexión.
	- Si se interrumpe la ejecución puedes ajustar las fechas de inicio y fin en el script para reanudar la descarga.
