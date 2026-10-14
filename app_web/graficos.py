import matplotlib.pyplot as plt
<<<<<<< HEAD
=======

>>>>>>> cambios-recientes
def generar_grafica(filtrados, estacion, medicion):

    plt.plot([float(x) for x in filtrados])
    
    plt.title(f"{estacion} - {medicion}")
    
    plt.savefig("grafica.png")
    plt.close()
    return "grafica.png"