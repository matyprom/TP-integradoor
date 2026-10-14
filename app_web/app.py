import streamlit as st
import sys
import pandas as pd
from datos_json import cargar_json, filtrar_datos
from estadisticas import calcular_estadisticas
from graficos import generar_grafica
# jason=sys.argv
jason = "conversor/janson.json"
st.title("Aplicacion del equipo messi")

estacion = st.selectbox("Estacion", ["AEROPARQUE AERO", "AZUL AERO", "BAHIA BLANCA AERO"])
medicion = st.selectbox("Medicion", ["temp", "humedad", "PNM"])


datos = cargar_json(jason)
filtrados = filtrar_datos(datos, estacion, medicion)
estadisticas = calcular_estadisticas(filtrados)
ruta_grafica = generar_grafica(filtrados, estacion, medicion)

st.title("Panel de Observaciones Meteorológicas")
st.subheader("tablita de datos filtrados")
st.subheader("tablita de datos filtrados")
df_tabla = pd.DataFrame({
    "estacion": [estacion] * len(filtrados),
    "medicion": [medicion] * len(filtrados),
    "valor": filtrados
})
st.dataframe(df_tabla)

st.title("Grafico de Evolucion")
st.image(
    "app_web/salidas/grafica.png",
    caption="grafica"
)

