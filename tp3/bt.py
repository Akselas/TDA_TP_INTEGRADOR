DEMANDA_INCUMPLIDA_SOLUCION = 1
LIBRE = '-'
HORIZONTAL = 0
VERTICAL = 1
MENOR_BARCO = -1
import sys
sys.setrecursionlimit(10000)

def barco_entra_por_demandas(dem_fil, dem_col, barcos, barco):
    tamaño_barco = barcos[barco]

    for demanda in dem_fil:
        if demanda >= tamaño_barco:
            return True

    for demanda in dem_col:
        if demanda >= tamaño_barco:
            return True

    return False

def hay_barco_adyacente(posicion, tablero, n, m):
    i,j = posicion
    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    for di, dj in direcciones:
        i_adyacente, j_adyacente = i + di, j + dj
        if 0 <= i_adyacente < n and 0 <= j_adyacente < m:
            if tablero[i_adyacente][j_adyacente] != LIBRE:
                return True

    return False

def es_posicion_valida(posicion, tablero, dem_fil, n, dem_col, m):
    i, j = posicion

    if tablero[i][j] != LIBRE:
        return False
    if dem_fil[i] == 0 or dem_col[j] == 0:
        return False
    if hay_barco_adyacente(posicion, tablero, n, m):
        return False

    return True

def proxima_posicion_valida_desde(tablero, dem_fil, n, dem_col, m, posicion):
    fila, columna = posicion
    if columna + 1 < m:
        inicio_fila, inicio_columna = fila, columna + 1
    else:
        inicio_fila, inicio_columna = fila + 1, 0

    for i in range(inicio_fila, n):
        for j in range(inicio_columna if i == inicio_fila else 0, m):
            if es_posicion_valida((i,j), tablero, dem_fil, n, dem_col, m):
                return (i, j)
            
    return None 

def proximo_barco_distinto(barcos, k, barco_actual):
    for i in range(barco_actual + 1, k):
        if barcos[i] != barcos[barco_actual]:
            return i
    return k

def puedo_ubicar_horizontal(tablero, dem_fil, n, dem_col, m, tamaño_barco, pos_inicial):
    fila, col_inicial = pos_inicial
    col_final = col_inicial + tamaño_barco-1

    if tamaño_barco > dem_fil[fila] or col_final >= m:
        return False
    for col in range(col_inicial, col_final + 1):
        if not es_posicion_valida((fila, col), tablero, dem_fil, n, dem_col, m):
            return False
    
    return True

def puedo_ubicar_vertical(tablero, dem_fil, n, dem_col, m, tamaño_barco, pos_inicial):
    fila_inicial, col = pos_inicial
    fila_final = fila_inicial + tamaño_barco-1

    if tamaño_barco > dem_col[col] or fila_final >= n:
        return False
    for fila in range(fila_inicial, fila_final + 1):
        if not es_posicion_valida((fila, col), tablero, dem_fil, n, dem_col, m):
            return False
    return True

def barco_ni_entra(dem_fil, dem_col, tamaño_barco):
    for demanda in dem_fil:
        if demanda >= tamaño_barco:
            return False
    for demanda in dem_col:
        if demanda >= tamaño_barco:
            return False

    return True

def proxima_ubicacion(tablero, dem_fil, n, dem_col, m, barcos, k, barco_actual, posicion_actual, orientacion_actual, solucion_parcial):  
    if barco_actual == k or posicion_actual is None:
        return barco_actual, posicion_actual, orientacion_actual
    
    if barco_actual != 0 and barcos[barco_actual] == barcos[barco_actual-1] and solucion_parcial[barco_actual-1] is None:
        proximo_barco = proximo_barco_distinto(barcos, k, barco_actual)
        proxima_posicion = proxima_posicion_valida_desde(tablero, dem_fil, n, dem_col, m, (0,0))
        proxima_orientacion = HORIZONTAL
    else: 
        proximo_barco = barco_actual
        proxima_orientacion = orientacion_actual
        proxima_posicion = posicion_actual
    if proximo_barco == k:
        seguir_intentando_ubicar = False
    else:
        seguir_intentando_ubicar = True
    while(seguir_intentando_ubicar):
        if proxima_orientacion == HORIZONTAL:
            if puedo_ubicar_horizontal(tablero, dem_fil, n, dem_col, m, barcos[proximo_barco], proxima_posicion):
                seguir_intentando_ubicar = False
            else:
                proxima_orientacion = VERTICAL
        elif proxima_orientacion == VERTICAL:
            if puedo_ubicar_vertical(tablero, dem_fil, n, dem_col, m, barcos[proximo_barco], proxima_posicion):
                seguir_intentando_ubicar = False
            else:
                proxima_orientacion = HORIZONTAL
                proxima_posicion = proxima_posicion_valida_desde(tablero, dem_fil, n, dem_col, m, proxima_posicion)
        if proxima_posicion == None:
            proximo_barco += 1
            proxima_posicion = proxima_posicion_valida_desde(tablero, dem_fil, n, dem_col, m, (0,0))
            proxima_orientacion = HORIZONTAL

        if proximo_barco == k or proxima_posicion is None: #no hay mas barcos o tablero está todo ocupado
            seguir_intentando_ubicar = False

    return proximo_barco, proxima_posicion, proxima_orientacion

def ubicar_barco_vertical(tablero, dem_fil, dem_col, numero_barco, tamaño_barco, pos_inicial, solucion_parcial):
    fila_inicial, col = pos_inicial
    fila_final = fila_inicial + tamaño_barco-1

    for fila in range(fila_inicial, fila_final + 1):
        tablero[fila][col] = numero_barco
        dem_fil[fila] -= 1
        dem_col[col] -= 1
    solucion_parcial[numero_barco] = (pos_inicial, (fila_final, col))

def quitar_barco_vertical(tablero, dem_fil, dem_col, numero_barco, tamaño_barco, pos_inicial, solucion_parcial):
    fila_inicial, col = pos_inicial
    fila_final = fila_inicial + tamaño_barco-1

    for fila in range(fila_inicial, fila_final + 1):
        tablero[fila][col] = LIBRE
        dem_fil[fila] += 1
        dem_col[col] += 1
    solucion_parcial[numero_barco] = None

def ubicar_barco_horizontal(tablero, dem_fil, dem_col, numero_barco, tamaño_barco, pos_inicial, solucion_parcial):
    fila, col_inicial = pos_inicial
    col_final = col_inicial + tamaño_barco-1

    for col in range(col_inicial, col_final + 1):
        tablero[fila][col] = numero_barco
        dem_fil[fila] -= 1
        dem_col[col] -= 1
    solucion_parcial[numero_barco] = (pos_inicial, (fila, col_final))

def quitar_barco_horizontal(tablero, dem_fil, dem_col, numero_barco, tamaño_barco, pos_inicial, solucion_parcial):
    fila, col_inicial = pos_inicial
    col_final = col_inicial + tamaño_barco-1

    for col in range(col_inicial, col_final + 1):
        tablero[fila][col] = LIBRE
        dem_fil[fila] += 1
        dem_col[col] += 1
    solucion_parcial[numero_barco] = None

def quitar_barco(tablero, dem_fil, dem_col, numero_barco, tamaño_barco, pos_inicial, orientacion, solucion_parcial):
    if orientacion == HORIZONTAL:
        quitar_barco_horizontal(tablero, dem_fil, dem_col, numero_barco, tamaño_barco, pos_inicial, solucion_parcial)
    elif orientacion == VERTICAL:
        quitar_barco_vertical(tablero, dem_fil, dem_col, numero_barco, tamaño_barco, pos_inicial, solucion_parcial)

def ubicar_barco(tablero, dem_fil, dem_col, numero_barco, tamaño_barco, pos_inicial, orientacion, solucion_parcial):
    if orientacion == HORIZONTAL:
        ubicar_barco_horizontal(tablero, dem_fil, dem_col, numero_barco, tamaño_barco, pos_inicial, solucion_parcial)
    elif orientacion == VERTICAL:
        ubicar_barco_vertical(tablero, dem_fil, dem_col, numero_barco, tamaño_barco, pos_inicial, solucion_parcial)

def menor_demanda_incumplida_posible(barcos, barco_actual, demanda_incumplida_actual):
    demanda_incumplida_posible = demanda_incumplida_actual

    for i in range(barco_actual, len(barcos)):
        demanda_incumplida_posible -= barcos[i] * 2

    return demanda_incumplida_posible

def batalla_naval_bt(tablero, dem_fil, n, dem_col, m, barcos, k, barco_actual, pos_actual, orientacion_actual, solucion_parcial, mejor_solucion, menor_demanda_incumplida):
    
    if pos_actual is None or barco_actual == k: #probe con todos los barcos o no hay lugar en tablero
        if sum(dem_fil) + sum(dem_col) < menor_demanda_incumplida[0]:
            mejor_solucion[:] = solucion_parcial.copy()
            menor_demanda_incumplida[0] = sum(dem_fil) + sum(dem_col)
        return mejor_solucion, menor_demanda_incumplida

    if sum(dem_fil) < barcos[-1] or sum(dem_col) < barcos[-1]: #no puedo meter ni el barco mas chico 
        if sum(dem_fil) + sum(dem_col) < menor_demanda_incumplida[0]:
            mejor_solucion[:] = solucion_parcial.copy()
            menor_demanda_incumplida[0] = sum(dem_fil) + sum(dem_col)
        return mejor_solucion, menor_demanda_incumplida

    if menor_demanda_incumplida[0] <= menor_demanda_incumplida_posible(barcos, barco_actual, sum(dem_fil) + sum(dem_col)): #no puedo mejorar solucion con los barcos que quedan
        return mejor_solucion, menor_demanda_incumplida 

    ubicar_barco(tablero, dem_fil, dem_col, barco_actual, barcos[barco_actual], pos_actual, orientacion_actual, solucion_parcial)
    proximo_barco, proxima_posicion, proxima_orientacion = proxima_ubicacion(tablero, dem_fil, n, dem_col, m, barcos, k, barco_actual+1, (0,0), HORIZONTAL, solucion_parcial)
    sol_ubicando = batalla_naval_bt(tablero, dem_fil, n, dem_col, m, barcos, k, proximo_barco, proxima_posicion, proxima_orientacion, solucion_parcial, mejor_solucion, menor_demanda_incumplida)
    quitar_barco(tablero, dem_fil, dem_col, barco_actual, barcos[barco_actual], pos_actual, orientacion_actual, solucion_parcial)

    posible_proxima_posicion = proxima_posicion_valida_desde(tablero, dem_fil, n, dem_col, m, pos_actual)
    proximo_barco, proxima_posicion, proxima_orientacion = proxima_ubicacion(tablero, dem_fil, n, dem_col, m, barcos, k, barco_actual, posible_proxima_posicion, orientacion_actual, solucion_parcial) 
    sol_sin_ubicar = batalla_naval_bt(tablero, dem_fil, n, dem_col, m, barcos, k, proximo_barco, proxima_posicion, proxima_orientacion, solucion_parcial, mejor_solucion, menor_demanda_incumplida)

    return sol_ubicando if sol_ubicando[DEMANDA_INCUMPLIDA_SOLUCION] < sol_sin_ubicar[DEMANDA_INCUMPLIDA_SOLUCION] else sol_sin_ubicar

def batalla_naval(dem_fil, dem_col, barcos):
    
    n = len(dem_fil)
    m = len(dem_col)
    k = len(barcos)
    tablero = [[LIBRE for _ in range(m)] for _ in range(n)]
    barcos.sort(reverse=True)
    solucion_parcial = [None]*k
    barco_inicial, pos_inicial, orientacion_inicial = proxima_ubicacion(tablero, dem_fil, n, dem_col, m, barcos, k, 0, (0,0), HORIZONTAL, solucion_parcial)
    res = batalla_naval_bt(tablero, dem_fil, n, dem_col, m, barcos, k, barco_inicial, pos_inicial, orientacion_inicial, solucion_parcial, [], [sum(dem_fil) + sum(dem_col)])
    return res[0], res[1][0]