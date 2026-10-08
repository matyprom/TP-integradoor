import matplotlib.pyplot as plt


def generar_grafica(filtrados, estacion, medicion):
    valores = []
    nombre_archivo = "app_web/salidas/grafica.png"
    for dato in filtrados:
        valores.append(float(dato))

    plt.plot(valores)
    plt.title(estacion)
    plt.xlabel("Registros")
    plt.ylabel(medicion)
    plt.savefig(nombre_archivo)
    plt.close()

    return nombre_archivo

mediciones_prueba = ['0.3', '0.9', '-0.3', '1.0', '0.8', '0.4', '0.6', '1.7', '1.8', '2.7']
print(generar_grafica(mediciones_prueba, "BARILOCHE AERO", "temp"))