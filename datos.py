import sys
import json
from datetime import datetime, timedelta
import funciones
    
archivo_txt = sys.argv[1]

try:
    with open(archivo_txt, "r") as datohorario:
            for i, linea in enumerate(datohorario):
                if i <= 1:
                    continue
                datos = linea.split()
                if len(datos)<9:
                    fecha = datos[0]
                    hora = datos[1]
                    temp = datos[2]
                    humedad = datos[3]
                    PNM = "925"
                    DD = datos[4]
                    FF = datos[5]
                    lugar = " ".join(datos[6:])
                if len(datos)>8:
                    fecha = datos[0]
                    hora = datos[1]
                    temp = datos[2]
                    humedad = datos[3]
                    PNM = datos[4]
                    DD = datos[5]
                    FF = datos[6]
                    lugar = " ".join(datos[7:])
                print(len(datos), PNM, lugar)

                fecha_valida = funciones.validar_fecha(fecha)
                hora_valida = funciones.validar_hora(hora)
                temperatura_ok = funciones.validar_temperatura(temp)
                humedad_ok = funciones.validar_humedad(humedad)
                PNM_ok = funciones.validar_presion(PNM)
                dd_ok = funciones.validar_direccion_viento(DD)
                ff_ok = funciones.validar_velocidad_viento(FF)
                lugar_ok = funciones.validar_estacion(lugar)


except FileNotFoundError:
    print(f"Error: No se encontró el archivo '{archivo_txt}' en la carpeta actual.")
    sys.exit(1)

