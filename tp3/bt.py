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
    return batalla_naval_bt(tablero, dem_fil, n, dem_col, m, barcos, k, barco_inicial, pos_inicial, orientacion_inicial, solucion_parcial, [], [sum(dem_fil) + sum(dem_col)])

#3,3,2 --> 7 OK
#demandas_filas = [3,1,2]
#demandas_columnas = [3,2,0]
#barcos = [1,1]

#5,5,6 --> 6 OK
#demandas_filas = [3,3,0,1,1]
#demandas_columnas = [3,1,0,3,3]
#barcos = [1,2,2,2,2,1]

# 8,7,10 --> 27 OK
#demandas_filas = [1,4,4,4,3,3,4,4]
#demandas_columnas = [6,5,3,0,6,3,3]
#barcos = [2,1,2,2,1,3,2,7,7,7]

#10,3,3 --> 8 OK
#demandas_filas = [1,0,1,0,1,0,0,1,1,1]
#demandas_columnas = [1,4,3]
#barcos = [3,3,4]

#10,10,10 --> 0 OK
#demandas_filas = [3,2,2,4,2,1,1,2,3,0]
#demandas_columnas = [1,2,1,3,2,2,3,1,5,0]
#barcos = [4,3,3,2,2,2,1,1,1,1]

#12,12,21 --> 12 OK (tarda mucho?)
#demandas_filas = [3,6,1,2,3,6,5,2,0,3,0,3]
#demandas_columnas = [3,0,1,1,3,1,0,3,3,4,1,4]
#barcos = [4,3,7,4,3,2,2,5,5,5,4,4,5,5,7,6,4,1,7,4,4]

#15-10-15 --> 27 OK
#demandas_filas = [0,3,4,1,1,4,5,0,4,5,4,2,4,3,2]
#demandas_columnas = [0,0,3,4,1,4,6,5,2,0]
#barcos = [6,2,1,8,7,2,7,2,5,8,1,8,8,1,6]

#20-20-20 --> 16
#demandas_filas = [5,0,0,6,2,1,6,3,3,1,2,4,5,5,2,5,4,0,4,5]
#demandas_columnas = [0,5,5,0,6,2,2,6,2,1,3,1,2,3,1,4,5,2,1,6]
#barcos = [5,5,6,5,1,3,1,5,1,1,1,1,2,3,1,1,6,7,7,4]

#20-25-30 --> 75 OK
#demandas_filas = [1,2,5,10,11,0,11,11,3,9,9,3,9,6,1,8,3,11,6,7]
#demandas_columnas = [5,4,5,2,10,1,0,8,7,6,0,5,4,8,4,7,4,0,8,5,6,2,4,9,7]
#barcos = [9,4,11,12,12,5,5,6,9,5,12,3,3,9,1,1,6,13,7,2,4,5,4,12,4,3,10,13,13,8]

#30-25-25 --> 158
#demandas_filas = [3,11,11,1,2,5,4,10,5,2,12,6,12,7,0,2,0,8,10,11,6,10,0,11,5,8,6,9,8,0]
#demandas_columnas = [3,12,1,5,14,15,6,11,2,10,12,10,6,2,7,1,5,11,5,10,7,11,4,0,5]
#barcos = [10,6,6,11,14,15,8,10,1,14,7,6,16,13,16,12,1,12,5,10,4,14,13,12,4]

import time

# Inicio del temporizador
start_time = time.time()

res = batalla_naval(demandas_filas, demandas_columnas, barcos)
# solucion de la forma [(pos_i_barco1, pos_f_barco1), (pos_i_barco2, pos_f_barco2), ... , (pos_i_barcok, pos_f_barcok)]
print(res)

# Fin del temporizador
end_time = time.time()

# Tiempo transcurrido
elapsed_time = end_time - start_time


print(f"Tiempo de ejecución: {elapsed_time:.4f} segundos")