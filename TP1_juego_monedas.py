
def juego_monedas(monedas, turno, primero, segundo):
    """El algoritmo resuelve el problema haciendo que el primer jugador siempre gane""" 

    if(len(monedas)==0): return
    
    if turno:
        primero.monedero += monedas.pop(0) if monedas[0]> monedas[-1] else monedas.pop(-1)
    else:
        segundo.monedero += monedas.pop(0) if monedas[0]< monedas[-1] else monedas.pop(-1) 
    
    juego_monedas(monedas, not turno, primero, segundo)
