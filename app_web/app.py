import streamlit as st
import sys
import pandas as pd
import streamlit as st
jason=sys.argv[1]
# jason="conversor/janson.json"
st.title("Aplicacion equipo Messi")


estacion = st.selectbox("Estacion", ["AEROPARQUE AERO", "AZUL AERO", "BAHIA BLANCA AERO", "BASE BELGRANO II, BARILOCHE AERO"])
medicion = st.selectbox("Medicion", ["temp", "humedad", "PNM", "PNM", "DD", "FF"])

from datos_json import cargar_json, filtrar_datos
from estadisticas import calcular_estadisticas, generar_csv
from graficos import generar_grafica

datos = cargar_json(jason)
filtrados = filtrar_datos(datos, estacion, medicion)
estadisticas = calcular_estadisticas(filtrados)
ruta_grafica = generar_grafica(filtrados, estacion, medicion)
generar_csv(filtrados, estacion, medicion, nombre_archivo="app_web/salidas/salida.csv")

st.title("Panel de Observaciones Meteorológicas")
st.subheader("tablita de datos filtrados")
df_tabla = pd.DataFrame({
    "estacion": [estacion] * len(filtrados),
    "medicion": [medicion] * len(filtrados),
    "valor": filtrados
})
st.dataframe(df_tabla)


st.title("Gráfico de Evolución")

st.image(
    "app_web/salidas/grafica.png",
    caption="grafica"
)



