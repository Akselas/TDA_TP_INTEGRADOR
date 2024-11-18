import sys
sys.path.append("../") 
from algoritmo_pd import elecciones_hermanos
from manejo_archivos import obtener_lista_monedas, dar_resultados_juego
from jugador import Jugador
from collections import deque

SOPHIA = 'Sophia' 
MATEO = 'Mateo'
ELECCION_ULTIMA_MONEDA = ' agarra la ultima'
ELECCION_PRIMERA_MONEDA = ' agarra la primera'

def juego_monedas(monedas, elecciones, sophia, mateo):
    for eleccion in elecciones:
        if eleccion == SOPHIA + ELECCION_PRIMERA_MONEDA:
            sophia.ganancia += monedas.popleft()
        elif eleccion == SOPHIA + ELECCION_ULTIMA_MONEDA:
            sophia.ganancia += monedas.pop()
        elif eleccion == MATEO + ELECCION_PRIMERA_MONEDA:
            mateo.ganancia += monedas.popleft()
        else:
            mateo.ganancia += monedas.pop()

def jugar(path):
    
    monedas = obtener_lista_monedas(path)
    sophia = Jugador(SOPHIA)
    mateo = Jugador(MATEO)
    elecciones = elecciones_hermanos(monedas)
    juego_monedas(deque(monedas), elecciones, sophia, mateo)
    dar_resultados_juego(path, sophia.ganancia, mateo.ganancia, elecciones)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python juego_monedas.py <path_al_archivo_de_monedas.txt>")
        sys.exit(1)

    path = sys.argv[1]
    jugar(path)