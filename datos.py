import sys
import json
from datetime import datetime, timedelta
import funciones
    
archivo_txt = sys.argv[1]
archivo_json = sys.argv[2]

validos = []
invalidos = []

try:
    with open(archivo_txt, "r") as datohorario:
            for i, linea in enumerate(datohorario):
                if i <= 1:
                    continue
                linea_limpia = linea.strip()
                
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

            if (fecha_valida and hora_valida and temperatura_ok and 
                        humedad_ok and PNM_ok and dd_ok and ff_ok and lugar_ok):
                        
                        validos.append({
                            "fecha": fecha,
                            "hora": hora,
                            "temp": temp,
                            "humedad": humedad,
                            "PNM": PNM,
                            "DD": DD,
                            "FF": FF,
                            "lugar": lugar
                        })
            else:
                invalidos.append(linea_limpia)
    resultado = {
            "registros_validos": validos,
            "registros_invalidos": invalidos
        }

    with open(archivo_json, "w",) as f_json:
            json.dump(resultado, f_json,)
    print(f"Válidos: {len(validos)} | Inválidos: {len(invalidos)}")

except FileNotFoundError:
    print(f"Error: No se encontró el archivo '{archivo_txt}' en la carpeta actual.")
sys.exit(1)

