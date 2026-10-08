def calcular_estadisticas(filtrados):
    cantidad= len(filtrados)

    primer_valor=float(filtrados[0])
    minimo=primer_valor
    maximo=primer_valor
    promedio=0

    for datos in filtrados:
        valor=float(datos)
        if minimo>valor:
            minimo=valor
        if maximo<valor:
            maximo=valor
        promedio+=valor
    promedio_final=promedio/cantidad

    return(cantidad, minimo, maximo, promedio_final)


mediciones_prueba = ['0.3', '0.9', '-0.3', '1.0', '0.8', '0.4', '0.6', '1.7', '1.8', '2.7']
def generar_csv(filtrados, estacion, medicion, nombre_archivo="salida.csv"):
    with open(nombre_archivo, "w") as archivo:

        archivo.write("estacion,medicion,valor\n")
        for valor in filtrados:
            archivo.write(f"{estacion},{medicion},{valor}\n")

print(generar_csv(mediciones_prueba,"AEROPARQUE AERO","temp","app_web/salidas/aeroparque_temp.csv"))