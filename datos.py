import sys
import json
    
archivo_txt = sys.argv[1]

try:
    with open(archivo_txt, "r") as datohorario:
            for i, linea in enumerate(datohorario):
                if i > 1:
                    datos = linea.split()
                if len(datos) < 8:
                    continue
                datos=linea.split()
                fecha=datos[0]
                hora=datos[1]
                temp=datos[2]
                humedad=datos[3]
                PNM=datos[4]
                DD=datos[5]
                FF=datos[6]
                lugar=" ".join(datos[7:])
except FileNotFoundError:
    print(f"Error: No se encontró el archivo '{archivo_txt}' en la carpeta actual.")
    sys.exit(1)
