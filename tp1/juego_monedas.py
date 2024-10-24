import sys
from manejo_archivos import obtener_lista_monedas, dar_resultados_juego
from jugador import Jugador
from collections import deque

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

def juego_monedas(monedas, elecciones, sophia, mateo):
    for eleccion in elecciones:
        if eleccion == ELECCION_PRIMERA_MONEDA + SOPHIA:
            sophia.ganancia += monedas.popleft()
        elif eleccion == ELECCION_ULTIMA_MONEDA + SOPHIA:
            sophia.ganancia += monedas.pop()
        elif eleccion == ELECCION_PRIMERA_MONEDA + MATEO:
            mateo.ganancia += monedas.popleft()
        else:
            mateo.ganancia += monedas.pop()

def jugar(path):
    
    lista_monedas = obtener_lista_monedas(path)
    
    monedas = deque(lista_monedas)
    sophia = Jugador(SOPHIA)
    mateo = Jugador(MATEO)
    elecciones = elecciones_sophia(deque(monedas))
    juego_monedas(monedas, elecciones, sophia, mateo)

    dar_resultados_juego(path, sophia.ganancia, mateo.ganancia, elecciones)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python juego_monedas.py <path_al_archivo_de_monedas.txt>")
        sys.exit(1)

    path = sys.argv[1]
    jugar(path)