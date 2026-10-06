import json


def cargar_json(json):
    with open(json, "r") as archivo:
        datos = json.load(archivo)
    return datos
# 
def filtrar_datos(datos, estacion, medicion):
    resultado=[]
    for clave, valor in datos.items():
        for lugar, dato in valor.items():
                if lugar == estacion:
                    for lectura in dato:
                        if medicion in lectura:
                            resultado.append(lectura[medicion])
    return(resultado)
        

datos= {"registros_validos": {
            "AEROPARQUE AERO": [
                {
                    "fecha": "23082026",
                    "hora": "0",
                    "temp": "10.7",
                    "humedad": "44",
                    "PNM": "1023.9",
                    "DD": "260",
                    "FF": "6"
                },
                {
                    "fecha": "23082026",
                    "hora": "1",
                    "temp": "10.3",
                    "humedad": "43",
                    "PNM": "1024.1",
                    "DD": "250",
                    "FF": "6"
                }]
        }
}

print(filtrar_datos(datos, "AEROPARQUE AERO", "FF"))