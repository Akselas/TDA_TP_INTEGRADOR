import sys
from manejo_archivos import obtener_lista_monedas, dar_resultados_juego
from jugador import Jugador
from collections import deque

def juego_monedas(monedas: deque, jugador_n1: Jugador, jugador_n2: Jugador):

    turno_jugador_n1 = True

    while monedas:
        if turno_jugador_n1:
            jugador_n1.ganancia += monedas.popleft() if monedas[0] > monedas[-1] else monedas.pop()
        else:
            jugador_n2.ganancia += monedas.popleft() if monedas[0] < monedas[-1] else monedas.pop()
        
        turno_jugador_n1 = not turno_jugador_n1

def jugar(path):
    
    lista_monedas = obtener_lista_monedas(path)
    
    monedas = deque(lista_monedas)
    sophia = Jugador("Sophia")
    mateo = Jugador("Mateo")
    juego_monedas(monedas, sophia, mateo)

    dar_resultados_juego(path, sophia.ganancia, mateo.ganancia)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python juego_monedas.py <path_al_archivo_de_monedas.txt>")
        sys.exit(1)

    path = sys.argv[1]
    jugar(path)