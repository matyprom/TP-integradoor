from datetime import datetime, timedelta
def validar_lugar(lugar):
    if lugar.strip() != "":
        return True
    return False

def validar_humedad(humedad):
    try:
        humedad_validad = float(humedad)
        if 0 <= humedad_validad <= 100:
            return True
        return False
    except ValueError:
        return False
def validar_presion(pnm):
    try:
        pnm_valido= float(pnm)
        if 800 <= pnm_valido <= 1100:
            return True
        return False
    except (ValueError, TypeError):
        return False

def validar_direccion_viento(dd):  
    try:
        DD_valido = float(dd)
        if 0 <= DD_valido <= 360:
            return True
        return False
    except ValueError:
        return False

def validar_velocidad_viento(ff):
    try:
        FF_valido = float(ff)
        if FF_valido >= 0:
            return True
        return False
    except ValueError:
        return False


def validar_hora(hora):
    try:
        if len(hora)<=2:
            return datetime.strptime(hora, "%H").time()
    except ValueError:
        return False


def validar_fecha(fecha):
    try:
        if len(fecha) == 8:
            return datetime.strptime(fecha, "%d%m%Y").date()
        return False
    except ValueError:
        return False

def validar_temperatura(temp):
    try:
        temp_valida = float(temp)
        if -90 <= temp_valida <= 60:
            return temp_valida
        return False
    except (ValueError, TypeError):
        return False
