import requests
import pandas as pd
import time
import xml.etree.ElementTree as ET
from datetime import date, timedelta, datetime

# Configuración
FECHA_INICIO = date(1995, 1, 1)
FECHA_FIN = date(2025, 1, 1)
URL_API_BASE = "https://www.boe.es/datosabiertos/api/boe/sumario/"
HEADERS = {"Accept": "application/xml"}
DATOS = []



# Descarga de datos
def obtener_xml_sumario(fecha_str):
    """Descarga el XML del sumario del BOE para una fecha dada."""
    url = f"{URL_API_BASE}{fecha_str}"
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.content
    except requests.exceptions.HTTPError as e:
        if response.status_code != 404:
            print(f"Error HTTP en {fecha_str}: {e}")
        return None
    except Exception as e:
        print(f"Error de conexión en {fecha_str}: {e}")
        return None


def parsear_y_extraer_datos(xml_content, fecha_formato_iso):
    """Parsea el XML y extrae datos relevantes."""
    try:
        root = ET.fromstring(xml_content)
    except ET.ParseError:
        print(f"Error al parsear XML en {fecha_formato_iso}")
        return

    for departamento in root.findall('.//seccion/departamento'):
        organo_emisor = departamento.get('nombre') or 'N/A'

        for item in departamento.findall('.//item'):
            def get_text(tag_name):
                tag = item.find(tag_name)
                return tag.text.strip() if tag is not None and tag.text else 'N/A'

            datos = {
                'ID_Disposicion': get_text('identificador'),
                'Fecha_Publicacion': fecha_formato_iso,
                'Organo_Emisor': organo_emisor,
                'Titulo_Semantico': get_text('titulo'),
                'URL_PDF': item.findtext('url_pdf', default='N/A'),
                'URL_XML_Diario': item.findtext('url_xml', default='N/A'),
                'Licencia_Reutilizacion': 'Dominio Público/AAL (CC BY Compatible)'
            }
            DATOS.append(datos)


def recolectar_datos_por_rango():
    """Descarga todos los sumarios del rango configurado."""
    fecha_actual = FECHA_INICIO
    delta = timedelta(days=1)
    total_dias = (FECHA_FIN - FECHA_INICIO).days
    procesados = 0

    print(f"Iniciando descarga desde {FECHA_INICIO} hasta {FECHA_FIN}...")

    while fecha_actual <= FECHA_FIN:
        fecha_str_api = fecha_actual.strftime("%Y%m%d")
        fecha_str_iso = fecha_actual.strftime("%Y-%m-%d")

        xml_data = obtener_xml_sumario(fecha_str_api)
        if xml_data:
            parsear_y_extraer_datos(xml_data, fecha_str_iso)

        fecha_actual += delta
        procesados += 1

        if procesados % 100 == 0 or fecha_actual > FECHA_FIN:
            print(f"  → Progreso: {procesados}/{total_dias} días. Registros: {len(DATOS)}")

        time.sleep(0.5)

    print(f"\n Descarga completada. Registros totales: {len(DATOS)}")



# Procesamiento de datos

def analizar_datos():
    """Realiza análisis estadísticos sobre el dataset generado."""
    df = pd.DataFrame(DATOS)
    df.drop_duplicates(subset=['ID_Disposicion', 'Fecha_Publicacion'], inplace=True)
    df['Fecha_Publicacion'] = pd.to_datetime(df['Fecha_Publicacion'])

    # Filtrar por ministerio de universidades
    df_min = df[df['Organo_Emisor'].str.contains("UNIVERSIDADES", na=False)].copy()
    df_min['Fecha_Publicacion'] = pd.to_datetime(df_min['Fecha_Publicacion'])
    df_min['Año'] = df_min['Fecha_Publicacion'].dt.year

    # Crear bloques de 3 días para análisis temporal
    # Asegurarse de que la columna esté en formato datetime
    df_min['Fecha_Publicacion'] = pd.to_datetime(df_min['Fecha_Publicacion'])

    # Crear el rango completo de fechas
    fecha_inicio = df_min['Fecha_Publicacion'].min()
    fecha_fin = df_min['Fecha_Publicacion'].max()
    rango_completo = pd.date_range(start=fecha_inicio, end=fecha_fin, freq='D')

    # Crear DataFrame con todas las fechas y asignar bloque de 3 días
    fechas_completas = pd.DataFrame({'Fecha_Publicacion': rango_completo})
    fechas_completas['Bloque_3dias'] = ((fechas_completas['Fecha_Publicacion'] - fecha_inicio).dt.days // 3)

    # Unir con el dataset original para asignar el bloque correspondiente
    df_min = df_min.merge(fechas_completas, on='Fecha_Publicacion', how='left')
    df_min = df_min.drop(columns=['URL_PDF', 'URL_XML_Diario', 'Licencia_Reutilizacion'])

    df_min.to_csv('dataset_boe_universidades.csv', index=False, encoding='utf-8')

    print("Archivo guardado")




if __name__ == "__main__":
    recolectar_datos_por_rango()
    if DATOS:
        analizar_datos()
    else:
        print(" No se obtuvieron datos. Revisa tu conexión o el rango de fechas.")