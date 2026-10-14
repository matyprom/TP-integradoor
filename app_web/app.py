
import pandas as pd
import sys
import streamlit as st

st.title("Mi primera aplicación")
st.write("Hola desde Streamlit")

estacion = st.selectbox("Estacion", ["AEROPARQUE AERO", "AZUL AERO", "BAHIA BLANCA AERO"])
medicion = st.selectbox("Medicion", ["temp", "humedad", "PNM"])

from datos_json import cargar_json, filtrar_datos
from estadisticas import calcular_estadisticas, generar_csv
from graficos import generar_grafica

if len(sys.argv) > 1:
    json_path = sys.argv[1]
else:
    json_path = "conversor/janson.json"

datos = cargar_json(json_path)
filtrados = filtrar_datos(datos, estacion, medicion)
estadisticas = calcular_estadisticas(filtrados)
ruta_grafica = generar_grafica(filtrados, estacion, medicion)

try:
    datos = cargar_json(json_path)
except FileNotFoundError:
    st.error(f"Error: No se encontró el archivo '{json_path}'. Verifica la ruta.")
    datos = None
except Exception:
    st.error("Error: Hubo un problema al leer el archivo JSON.")
    datos = None


st.title("Panel de Observaciones Meteorológicas")

st.title("Gráfico de Evolución")


