def validar_estacion(lugar):
    if lugar.strip() != "":
        return True
    return False

def validar_humedad(humedad_valido):
    try:
        humedad = float(humedad_valido)
        if 0 <= humedad <= 100:
            return True
        return False
    except ValueError:
        return False

def validar_direccion_viento(dd_valido):  
    try:
        DD = float(dd_valido)
        if 0 <= DD <= 360:
            return True
        return False
    except ValueError:
        return False

def validar_velocidad_viento(ff_valido):
    try:
        FF = float(ff_valido)
        if FF >= 0:
            return True
        return False
    except ValueError:
        return False


def validar_hora(hora_valida):
    if hora_valida.isdigit():
        try:
            hora = int(hora_valida)
            if 0 <= hora <= 23:
                return True
        except ValueError:
            return False
    return False


def validar_fecha(fecha):
    try:
        if len(fecha) == 8:
            anio = int(fecha[0:2])
            mes = int(fecha[2:4])
            dia = int(fecha[4:8])
            if 1 <= dia <= 31:
                if 1 <= mes <= 12:
                    if anio<2030:
                        return True
        return False
    except ValueError:
        print("el dato no es un numero") 
        exit(1)
fecha="20552000"
print (validar_fecha(fecha))