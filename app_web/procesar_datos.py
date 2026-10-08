import sys

from app_web.datos_json import cargar_json, filtrar_datos
from estadisticas import calcular_estadisticas
from graficos import generar_grafica


def main():
    ruta_json = sys.argv[1]
    estacion = sys.argv[2]
    medicion = sys.argv[3]

    try:
        datos = cargar_json(ruta_json)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{ruta_json}'. Verifica la ruta.")
        return
    except Exception:
        print("Error: Hubo un problema al leer el archivo JSON.")
        return

    if len(filtrados) == 0:
        print(f"Error: No hay datos para la estación '{estacion}' y medición '{medicion}'.")
        return
    

    datos = cargar_json(ruta_json)
    filtrados = filtrar_datos(datos, estacion, medicion)
    estadisticas = calcular_estadisticas(filtrados)
    ruta_grafica = generar_grafica(filtrados, estacion, medicion)

    print(estadisticas)
    print(f"Grafica guardada en: {ruta_grafica}")


main()