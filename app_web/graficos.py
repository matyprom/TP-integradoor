import matplotlib.pyplot as plt
def generar_grafica(filtrados, estacion, medicion):
   
    plt.plot(horas, potencia)
    plt.title("Potencia generada")
    plt.xlabel("Hora")
    plt.ylabel("Potencia (W)")
    plt.savefig("grafica.png")
    plt.close()