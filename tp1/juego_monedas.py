import sys
sys.path.append("../") 
from manejo_archivos import obtener_lista_monedas, dar_resultados_juego
from algoritmo_greedy import elecciones_sophia
from jugador import Jugador
from collections import deque

ELECCION_ULTIMA_MONEDA = 'Última moneda para '
ELECCION_PRIMERA_MONEDA = 'Primera moneda para '
SOPHIA = 'Sophia' 
MATEO = 'Mateo'

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