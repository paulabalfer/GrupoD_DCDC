# Motivación

## 1. Objetivo General del Proyecto

El proyecto busca analizar cómo cambian los temas sobre los que el Ministerio de Universidades publica en el Boletín Oficial del Estado (BOE) a lo largo de los años.
Para ello, se procesan los titulares en español con el fin de identificar la evolución de los tópicos predominantes en el tiempo usando técnicas como zero-shot learning, así como su distribución geográfica y su posible relación con las características de cada entidad universitaria (pública o privada).

## 2. Pregunta de Investigación e Hipótesis

**Hipótesis principal:**

“La proporción de titulares relacionados con la creación o modificación de títulos universitarios aumenta significativamente entre 2008 y 2024, coincidiendo con la implantación del Espacio Europeo de Educación Superior (EEES) y la posterior expansión de los másteres oficiales.”

**Pregunta de investigación asociada:**

- ¿Existen diferencias en la distribución temática de los titulares del BOE según la comunidad autónoma o el tipo de universidad (pública/privada)?

## 3. Justificación del Dataset

**Origen y características**

- Fuente: pauDCDC/boe_universidades
- Tamaño: 162.576 ejemplos
- Periodo temporal: 1995–2024
- Idioma: Español

**Relevancia:**
El conjunto contiene todos los titulares del BOE relacionados con el Ministerio de Universidades en el periodo indicado. Cada registro incluye referencias a universidades, comunidades autónomas o provincias, lo que permite realizar análisis temáticos, sentimentales y geográficos sobre las publicaciones oficiales.

**Criterios de selección:**

Representatividad temporal adecuada (30 años de datos continuos).

Volumen suficiente para análisis estadísticos robustos.

Contenido textual adecuado para tareas de modelado de tópicos y sentimiento.

## 4. Justificación de los Indicadores Calculados

### Indicadores obligatorios

El procesamiento de los indicadores mostrados a continuación pueden encontrarse en la carpta "Indicadores obligatorios" en esta misma carpeta. 

#### 4.1 Volumen temporal de publicaciones
#### 4.2 Análisis de sentimiento
#### 4.3 Distribución de tópicos

### Indicadores opcionales

#### 4.4 Clasificación por tipo de entidad (pública o privada)
#### 4.5 Clasificación por geolocalización
#### 4.6 Clasificación temática asistida por LLM (Zero-shot)

Con el objetivo de identificar qué temática predomina en cada titular, utilizamos modelos de Zero-shot Learning los cuales están diseñados con conocimiento “general” de forma que pueden enfrentarse a un ejemplo que nunca han visto y dar resultados útiles basados en él. 

Entrenamos en un pequeño fragmento del conjunto de datos tres modelos diferentes para poder compararlos y ver cuál aparentemente funciona mejor: 

- MoritzLaurer/deberta-v3-base-zeroshot-v1.1-all-33: que funciona analizando la similitud semántica entre un texto de entrada y varias etiquetas propuestas, seleccionando la etiqueta que mejor se alinea conceptualmente con el texto. Se basa en el modelo DeBERTa, pero entrenado específicamente para tareas de clasificación múltiple (fine-tunning) comparando directamente el texto con las posibles clases que le proporciones. Está además entrenado de forma multilingüe (aunque es más fuerte en inglés) dado que ha visto ejemplos en varios idiomas durante su especialización, no solo durante el pre-entrenamiento base.
  
- MoritzLaurer/deberta-v3-large-zeroshot-v1: modelo muy similar al anterior también basado en DeBERTa y con alto rendimiento en clasificación multi-clase (trabaja con múltiples etiquetas simultáneamente), bajo la que asigna una probabilidad a cada clase y elige la más adecuada incluso si son conceptualmente similares. Está optimizado además para baja latencia equilibrando precisión y eficiencia computacional y entrenado para comprender mejor relaciones sintácticas y estructuras gramaticales complejas.

- Recognai/zeroshot_selectra_medium: modelo específicamente diseñado para el español y que interpreta las categorías basándose en su conocimiento del idioma. Basado en un modelo Selectra pre-entrenado y especificado en tareas de clasificación para aprender a relacionar textos en español con diferentes categorías; su versión “Medium” ofrece un buen equilibrio entre rendimiento y eficiencia computacional siendo más rápido pero manteniendo buena precisión. Entiende particularidades del español como modismos, dobles sentidos, y registros formales/informales típicos del idioma.
  
Con estos tres modelos creamos entonces un pequeño dataset procesado y vemos en los resultados que, aparentemente, el segundo modelo parece funcionar mejor puesto que siempre está “de acuerdo” con alguno de los otros dos (clasifican la misma temática/categoría como predominante). Usando un mecanismo de “consenso basado en triple medición” y debido a nuestra capacidad computacional limitada (no resulta viable procesar todo con los 3 modelos) decidimos procesar el conjunto entero de datos con dicho segundo modelo (“MoritzLaurer/deberta-v3-large-zeroshot-v1”) de cara a obtener un valor asociado a cada categoría para cada titular. 

Una vez obtenido el resultado creamos una columna en el conjunto de datos por cada categoría y asociamos a cada una de ellas el valor correspondiente a dicha categoría en el resultado del modelo (devuelto en forma de diccionario clave:valor - categoría:porcentaje en decimal). 


## 5.Limitaciones y Sesgos Detectados

**Limitaciones técnicas:**

- El tamaño del dataset requiere procesamiento en partes (≈54k ejemplos cada una).
- Dependencia de recursos GPU para análisis con modelos grandes.

**Limitaciones lingüísticas:**

- Los modelos pueden fallar con español administrativo o regional.
- Algunos titulares son muy breves, lo que dificulta la clasificación semántica.

**Sesgos potenciales:**

- Temporal: algunos periodos (p. ej., cambios ministeriales) tienen más publicaciones.
- De contenido: la gran mayoría de disposiciones son sobre universidades públicas.
- Lingüístico: predominio del español formal, escasa variación dialectal.

**Consideraciones éticas:**

- No se tratan datos personales ni sensibles.
- Se reconoce la posible influencia del sesgo institucional en la fuente.
