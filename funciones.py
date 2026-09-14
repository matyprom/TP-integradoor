from datetime import datetime, timedelta
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
def validar_presion(pnm_valido):
    try:
        pnm = float(pnm_valido)
        if 800 <= pnm <= 1100:
            return pnm
        return False
    except (ValueError, TypeError):
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
    try:
        hora_str = str(hora_valida).zfill(2)
        return datetime.strptime(hora_str, "%H").time()
    except ValueError:
        return False


def validar_fecha(fecha):
    try:
        fecha_str = str(fecha)
        if len(fecha_str) == 8:
            return datetime.strptime(fecha_str, "%d%m%Y").date()
        return False
    except ValueError:
        return False

def validar_temperatura(temp_valida):
    try:
        temp = float(temp_valida)
        if -90 <= temp <= 60:
            return temp
        return False
    except (ValueError, TypeError):
        return False
