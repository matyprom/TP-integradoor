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



def generar_csv(filtrados, estacion, medicion, nombre_archivo="salida.csv"):
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        # 1. Escribimos el encabezado
        archivo.write("estacion,medicion,valor\n")

        # 2. Escribimos cada fila usando las variables pasadas por parámetro
        for valor in filtrados:
            archivo.write(f"{estacion},{medicion},{valor}\n")