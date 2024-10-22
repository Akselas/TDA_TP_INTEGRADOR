from jugador import Jugador
from collections import deque

def juego_monedas(monedas: deque, jugador_n1: Jugador, jugador_n2: Jugador):

    turno_jugador_n1 = True

    while monedas:
        if turno_jugador_n1:
            jugador_n1.monedero += monedas.popleft() if monedas[0] > monedas[-1] else monedas.pop()
        else:
            jugador_n2.monedero += monedas.popleft() if monedas[0] < monedas[-1] else monedas.pop()
        
        turno_jugador_n1 = not turno_jugador_n1

