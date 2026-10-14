import streamlit as st
import sys
print(sys.argv)
import streamlit as st

st.title("Mi primera aplicación")
st.write("Hola desde Streamlit")

estacion = st.selectbox("Estacion", ["AEROPARQUE AERO", "AZUL AERO", "BAHIA BLANCA AERO"])
medicion = st.selectbox("Medicion", ["temp", "humedad", "PNM"])



