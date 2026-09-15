# Trabajo Practico Integrador 1 - Parte 1 y 2
# Alicacion datos de ciudades

## Informacion del grupo

* Nombre del grupo: Messi
* integrantes:
* Matias Ramirez
* Renzo Terraza

## Descripcion del proyecto
El objetivo final del proyecto es hacer un conversor de TXT a JSON.
El programa lee los datos del txt y los separa en variables, luego con otro archivo .py donde estan las funciones de validar los datos del archivo.txt, se validan esa variables para que no de error al compilar el programa. El programa se ejecuta desde la consola pasando como argumentos la ruta del archivo .txt de entrada y la ruta del archivo .json de salida.


## Forma de ejecucion prevista 
El programa se ejecuta desde la consola pasando dos argumentos obligatorios por linea de comandos: la ruta del archivo de entrada (.txt) y la ruta del archivo de salida (.json). Por ejemplo: "python datos.py datohorario.txt, janson.json"

Archivo de entrada (.txt)
El texto proviene del Servicio Meteorologico Nacional con ancho de columnas o separado por espacios, incluyendo encabezados y observaciones horarias:
datohorario.txt

```
FECHA     HORA  TEMP   HUM   PNM     DD    FF     NOMBRE
         [HOA]  [°C]   [%]  [hPa]   [gr] [km/hr]
```

##datohorario.txt
este archivo de txt es uno que contiene las observaciones horarias del Servicio Meteorologico Nacional separadas por espacios o ancho de columnas.
Columnas principales: Fecha, Hora, Temperatura (TEMP), Humedad (HUM), Presión a nivel del mar (PNM), Direccion del viento (DD), Velocidad del viento (FF) y Nombre del lugar (NOMBRE).


## validaciones del codigo(funciones)
el modulo funciones_json.py verifica que cada campo cumpla con las siguientes reglas minimas:

Fecha: Debe tener formato de 8 digitos (DDMMAAAA) 

Hora: Debe tener un formato de 2 digitos.

Humedad: Debe ser un valor numerico en el rango de 0 a 100.

Direccion del viento: Debe ser un valor numerico entre 0 y 360 grados.

Temperatura: Debe ser un valor numerico entre -90.0 y 60.0 °C.

Presión (PNM): Debe ser un valor numerico entre 800.0 y 1100.0 hPa.

Velocidad del viento: Debe ser un valor numerico mayor o igual a 0 km/h.

lugar: Debe ser una cadena de texto no vacia.


## Archivos necesarios:
El script principal de procesamiento (script.py).
El módulo de validaciones (funciones.py).
El archivo de entrada con los datos principales (datohorario.txt).

El programa se ejecuta desde la consola pasando **dos argumentos obligatorios** por linea de comandos: la ruta del archivo de entrada y la ruta del archivo de salida.
python .\datos.py datohorario.txt salida.json
En Linux / macOS:
python3 datos.py datohorario.txt salida.json


##formato del json generado
```
{
    "registros_validos": {
        "Lugar de las mediciones": [
            {
                "fecha": "",
                "hora": "",
                "temp": "",
                "humedad": "",
                "PNM": "",
                "DD": "",
                "FF": ""
            },
        ]
    }
}
            "registros_invalidos": [  ]
```