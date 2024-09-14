def juego_monedas_iterativo(monedas, primero, segundo):

    turno = True  # True para el turno de Sophia, False para el de Mateo

    while monedas:
        if turno:
            primero.monedero += monedas.pop(0) if monedas[0] > monedas[-1] else monedas.pop(-1)
        else:
            segundo.monedero += monedas.pop(0) if monedas[0] < monedas[-1] else monedas.pop(-1)
        
        turno = not turno 
