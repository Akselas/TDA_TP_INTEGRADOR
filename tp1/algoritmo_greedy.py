ELECCION_ULTIMA_MONEDA = 'Última moneda para '
ELECCION_PRIMERA_MONEDA = 'Primera moneda para '
PRIMERA = True
ULTIMA = False
SOPHIA = 'Sophia' 
MATEO = 'Mateo'

def elegir_moneda(elecciones, monedas, primera, nombre_hermano):
    if primera:
        elecciones.append(ELECCION_PRIMERA_MONEDA + nombre_hermano)
        monedas.popleft()
    else: 
        elecciones.append(ELECCION_ULTIMA_MONEDA + nombre_hermano)
        monedas.pop()

def elecciones_sophia(monedas):
    elecciones = []
    turno_sophia = True

    while monedas:
        if turno_sophia:
            elegir_moneda(elecciones, monedas, PRIMERA, SOPHIA) if monedas[0] > monedas[-1] else elegir_moneda(elecciones, monedas, ULTIMA, SOPHIA)    
        else:
            elegir_moneda(elecciones, monedas, PRIMERA, MATEO) if monedas[0] < monedas[-1] else elegir_moneda(elecciones, monedas, ULTIMA, MATEO)
        turno_sophia = not turno_sophia

    return elecciones