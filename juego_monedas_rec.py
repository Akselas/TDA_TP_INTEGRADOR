from collections import deque
from jugador import Jugador

def juego_monedas_rec(monedas: deque, turno: bool, jugador_n1: Jugador, jugador_n2: Jugador):

    if(len(monedas) == 0): return
    
    if turno:
        jugador_n1.monedero += monedas.popleft() if monedas[0] > monedas[-1] else monedas.pop()
    else:
        jugador_n2.monedero += monedas.popleft() if monedas[0] < monedas[-1] else monedas.pop() 
    
    juego_monedas_rec(monedas, not turno, jugador_n1, jugador_n2)
