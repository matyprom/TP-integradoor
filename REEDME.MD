# Trabajo Práctico Integrador 1 - Parte 1 y 2
# Alicacion datos de ciudades

## Informacion del grupo

* Nombre del grupo: Messi
* integrantes:
* Matias Ramirez
* Renzo Terraza

## Descripción del proyecto
El objetivo final de esta primera parte del proyecto es hacer un conversor de TXT a JSON.
En esta primera instacia con el programa leyo los datos en el txt y los separo en variables, luego hicimos otra archivo.py para las funciones de validar los datos del archivo.tx. El programa se ejecuta desde la consola pasando como argumentos la ruta del archivo .txt de entrada y la ruta del archivo .json de salida.


## Forma de ejecucion prevista 
El programa se ejecuta desde la consola pasando dos argumentos obligatorios por línea de comandos: la ruta del archivo de entrada (.txt) y la ruta del archivo de salida (.json).

Archivo de entrada (.txt)
El texto proviene del Servicio Meteorológico Nacional con ancho de columnas o separado por espacios, incluyendo encabezados y observaciones horarias:
datohorario.txt

```
FECHA     HORA  TEMP   HUM   PNM     DD    FF     NOMBRE
         [HOA]  [°C]   [%]  [hPa]   [gr] [km/hr]
```

##datohorario.txt
este archivo de txt es uno que contiene las observaciones horarias del Servicio Meteorológico Nacional separadas por espacios o ancho de columnas.
Columnas principales: Fecha, Hora, Temperatura (TEMP), Humedad (HUM), Presión a nivel del mar (PNM), Dirección del viento (DD), Velocidad del viento (FF) y Nombre de la estación (NOMBRE).


## validaciones del codigo(funciones)
el modulo funciones_json.py verifica que cada campo cumpla con las siguientes reglas mínimas:

Fecha: Debe tener formato de 8 dígitos (DDMMAAAA) y corresponder a una fecha válida existente en el calendario.

Hora: Debe ser un valor entero entre 0 y 23.

Conversión a número: Temperatura, humedad, presión, dirección y velocidad del viento deben ser convertibles a tipo numérico (int o float).

Humedad: Debe ser un valor numérico en el rango de 0 a 100.

Dirección del viento: Debe ser un valor numérico entre 0 y 360 grados.


## Archivos necesarios:
El script principal de procesamiento (script.py).
El módulo de validaciones (funciones.py).
El archivo de entrada con los datos principales (datohorario.txt).

El programa se ejecuta desde la consola pasando **dos argumentos obligatorios** por línea de comandos: la ruta del archivo de entrada y la ruta del archivo de salida.
python .\datos.py datohorario.txt salida.json
En Linux / macOS:
python3 datos.py datohorario.txt salida.json


##formato del json generado

```
{
    "registros_validos": [
        {
            "fecha": "",
            "hora": "",
            "temp": "",
            "humedad": "",
            "PNM": "",
            "DD": "",
            "FF": "",
            "lugar": ""
        }
    ],
    "registros_invalidos": [  ]
                                    
```

