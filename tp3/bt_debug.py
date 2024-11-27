DEMANDA_CUMPLIDA_SOLUCION = 1
LIBRE = '-'
import sys
sys.setrecursionlimit(10000)

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

def ubicar_barco_horizontal(dem_fil, n, dem_col, m, numero_barco, tamaño_barco, tablero, pos_inicial, solucion_parcial):
    fila, col_inicial = pos_inicial
    col_final = col_inicial + tamaño_barco-1

    if tamaño_barco > dem_fil[fila]:
        return False

    for col in range(col_inicial, col_final + 1):
        if col >= m or not es_posicion_valida((fila, col), tablero, dem_fil, n, dem_col, m):
            return False
        
    for col in range(col_inicial, col_final + 1):
        tablero[fila][col] = numero_barco
        dem_fil[fila] -= 1
        dem_col[col] -= 1
    solucion_parcial[numero_barco] = (pos_inicial, (fila, col_final))
    
    return True

def ubicar_barco_vertical(dem_fil, n, dem_col, m, numero_barco, tamaño_barco, tablero, pos_inicial, solucion_parcial):
    fila_inicial, col = pos_inicial
    fila_final = fila_inicial + tamaño_barco-1

    if tamaño_barco > dem_col[col]:
        return False

    for fila in range(fila_inicial, fila_final + 1):
        if fila >= n or not es_posicion_valida((fila, col), tablero, dem_fil, n, dem_col, m):
            return False

    for fila in range(fila_inicial, fila_final + 1):
        tablero[fila][col] = numero_barco
        dem_fil[fila] -= 1
        dem_col[col] -= 1
    solucion_parcial[numero_barco] = (pos_inicial, (fila_final, col))
    
    return True

def quitar_barco_vertical(dem_fil, dem_col, numero_barco, tamaño_barco, tablero, pos_inicial, solucion_parcial):
    fila_inicial, col = pos_inicial
    fila_final = fila_inicial + tamaño_barco-1

    for fila in range(fila_inicial, fila_final + 1):
        tablero[fila][col] = LIBRE
        dem_fil[fila] += 1
        dem_col[col] += 1
    solucion_parcial[numero_barco] = None

def quitar_barco_horizontal(dem_fil, dem_col, numero_barco, tamaño_barco, tablero, pos_inicial, solucion_parcial):
    fila, col_inicial = pos_inicial
    col_final = col_inicial + tamaño_barco-1

    for col in range(col_inicial, col_final + 1):
        tablero[fila][col] = LIBRE
        dem_fil[fila] += 1
        dem_col[col] += 1
    solucion_parcial[numero_barco] = None


def proxima_posicion_libre_desde(posicion, tablero, dem_fil, n, dem_col, m):

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

def menor_demanda_incumplida_posible(barcos, barco_actual, demanda_incumplida_actual):

    demanda_incumplida_posible = demanda_incumplida_actual

    for i in range(barco_actual, len(barcos)):
        demanda_incumplida_posible -= barcos[i] * 2

    print(demanda_incumplida_posible)
    return demanda_incumplida_posible

def barco_entra_por_demandas(dem_fil, dem_col, barcos, barco):
    print("\n barco " + str(barco) + "de tamaño " + str(barcos[barco]))
    print(dem_fil)
    print(dem_col)
    
    if barcos[barco] < max(dem_fil):
        print("barco entra en alguna fila")
        return True
    if barcos[barco] < max(dem_col):
        print("barco entra en alguna columna")
        return True
    return False
    #return tamaño_barco < max(dem_fil) or tamaño_barco < max(dem_col)


def batalla_naval_bt(dem_fil, n, dem_col, m, barcos, k, barco_actual, tablero, pos_actual, solucion_parcial, mejor_solucion, menor_demanda_incumplida):
    
    if barco_actual == k:
        print("ya analice todos los barcos. menor demanda incumplida hasta ahora: " + str(menor_demanda_incumplida) + ". mejor solucion hasta ahora: " + str(mejor_solucion))
        if sum(dem_fil) + sum(dem_col) < menor_demanda_incumplida[0]:
            mejor_solucion[:] = solucion_parcial.copy()
            menor_demanda_incumplida[0] = sum(dem_fil) + sum(dem_col)
            print("la mejor solucion hasta ahora es: " + str(mejor_solucion) + " con demanda incumplida: " + str(menor_demanda_incumplida) + ". mejor solucion hasta ahora: " + str(mejor_solucion))
    
        return mejor_solucion, menor_demanda_incumplida
    
    if pos_actual is None:
        print("me fui de la matriz para el barco " + str(barco_actual) + ". menor demanda incumplida hasta ahora: " + str(menor_demanda_incumplida) + ". mejor solucion hasta ahora: " + str(mejor_solucion))
        if sum(dem_fil) + sum(dem_col) < menor_demanda_incumplida[0]:
            mejor_solucion[:] = solucion_parcial.copy()
            menor_demanda_incumplida[0] = sum(dem_fil) + sum(dem_col)
            print("la mejor solucion hasta ahora es: " + str(mejor_solucion) + " con demanda incumplida: " + str(menor_demanda_incumplida))
        return mejor_solucion, menor_demanda_incumplida

    if sum(dem_fil) == 0 or sum(dem_col) == 0:
        print("no puedo ubicar mas barcos habiendo llegado al barco " + str(barco_actual) + ". menor demanda incumplida hasta ahora: " + str(menor_demanda_incumplida))
        if sum(dem_fil) + sum(dem_col) < menor_demanda_incumplida[0]:
            mejor_solucion[:] = solucion_parcial.copy()
            menor_demanda_incumplida[0] = sum(dem_fil) + sum(dem_col)
            print("la mejor solucion hasta ahora es: " + str(mejor_solucion) + " con demanda incumplida: " + str(menor_demanda_incumplida))

        return mejor_solucion, menor_demanda_incumplida

    if menor_demanda_incumplida[0] <= menor_demanda_incumplida_posible(barcos, barco_actual, sum(dem_fil) + sum(dem_col)):
        print("no puedo mejorar la solucion. la menor demanda incumplida es: " + str(menor_demanda_incumplida) + ". tengo dem incumplida actual: " + str(sum(dem_fil) + sum(dem_col)) + " y tenngo barcos: " + str(barcos))
        print(dem_fil)
        print(dem_col)
        return mejor_solucion, menor_demanda_incumplida 
    
    if not barco_entra_por_demandas(dem_fil, dem_col, barcos, barco_actual):
        return batalla_naval_bt(dem_fil, n, dem_col, m, barcos, k, barco_actual+1, tablero, pos_actual, solucion_parcial, mejor_solucion, menor_demanda_incumplida)

    sol_horizontal = None 
    sol_vertical = None
   
    print("\nestoy analizando para el barco " + str(barco_actual) + " en la posicion " + str(pos_actual))
    print("tablero actual ")
    for fil in tablero:
        print(fil)
    if ubicar_barco_horizontal(dem_fil, n, dem_col, m, barco_actual, barcos[barco_actual], tablero, pos_actual, solucion_parcial):
        print("pude ubicar el barco horizontalmente. sigo desde el principio con el siguiente")
        prox_pos = proxima_posicion_libre_desde((0,0), tablero, dem_fil, n, dem_col, m)
        sol_horizontal = batalla_naval_bt(dem_fil, n, dem_col, m, barcos, k, barco_actual+1, tablero, prox_pos, solucion_parcial, mejor_solucion, menor_demanda_incumplida)
        quitar_barco_horizontal(dem_fil, dem_col, barco_actual, barcos[barco_actual], tablero, pos_actual, solucion_parcial)
    if barcos[barco_actual] != 1 and ubicar_barco_vertical(dem_fil, n, dem_col, m, barco_actual, barcos[barco_actual], tablero, pos_actual, solucion_parcial):
        print("pude ubicar el barco verticalmente. sigo desde el principio con el siguiente ")
        prox_pos = proxima_posicion_libre_desde((0,0), tablero, dem_fil, n, dem_col, m)
        sol_vertical = batalla_naval_bt(dem_fil, n, dem_col, m, barcos, k, barco_actual+1, tablero, prox_pos, solucion_parcial, mejor_solucion, menor_demanda_incumplida)
        quitar_barco_vertical(dem_fil, dem_col, barco_actual, barcos[barco_actual], tablero, pos_actual, solucion_parcial)
    
    prox_pos = proxima_posicion_libre_desde(pos_actual, tablero, dem_fil, n, dem_col, m)
    print("pos_actual: " + str(pos_actual) + ". barco actual: " + str(barco_actual) + ". pruebo con el mismo barco pero desde " + str(prox_pos))
    sol_prox_pos = batalla_naval_bt(dem_fil, n, dem_col, m, barcos, k, barco_actual, tablero, prox_pos, solucion_parcial, mejor_solucion, menor_demanda_incumplida)
    print("pruebo sin el barco desde el principio ")
    sol_sin = batalla_naval_bt(dem_fil, n, dem_col, m, barcos, k, barco_actual+1, tablero, (0,0), solucion_parcial, mejor_solucion, menor_demanda_incumplida)

    soluciones = [t for t in [sol_horizontal, sol_vertical, sol_prox_pos, sol_sin] if t is not None] 
    mejor_sol = min(soluciones, key=lambda x: x[1])
    print("devuelvo la mejor solucion " + str(mejor_sol))
    return mejor_sol

def batalla_naval(dem_fil, dem_col, barcos):
    
    n = len(dem_fil)
    m = len(dem_col)
    k = len(barcos)
    tablero = [[LIBRE for _ in range(m)] for _ in range(n)]
    barcos.sort(reverse=True)
    solucion_parcial = [None]*k
    return batalla_naval_bt(dem_fil, n, dem_col, m, barcos, k, 0, tablero, (0,0), solucion_parcial, [], [sum(dem_fil) + sum(dem_col)])

#3,3,2
#demandas_filas = [3,1,2]
#demandas_columnas = [3,2,0]
#barcos = [1,1]

#5,5,6
#demandas_filas = [3,3,0,1,1]
#demandas_columnas = [3,1,0,3,3]
#barcos = [1,2,2,2,2,1]

# 8,7,10
#demandas_filas = [1,4,4,4,3,3,4,4]
#demandas_columnas = [6,5,3,0,6,3,3]
#barcos = [2,1,2,2,1,3,2,7,7,7]

#10,3,3
#demandas_filas = [1,0,1,0,1,0,0,1,1,1]
#demandas_columnas = [1,4,3]
#barcos = [3,3,4]

#10,10,10
demandas_filas = [3,2,2,4,2,1,1,2,3,0]
demandas_columnas = [1,2,1,3,2,2,3,1,5,0]
barcos = [4,3,3,2,2,2,1,1,1,1]

#12,12,21 ---------------------------------
#demandas_filas = [3,6,1,2,3,6,5,2,0,3,0,3]
#demandas_columnas = [3,0,1,1,3,1,0,3,3,4,1,4]
#barcos = [4,3,7,4,3,2,2,5,5,5,4,4,5,5,7,6,4,1,7,4,4]

res = batalla_naval(demandas_filas, demandas_columnas, barcos)
# solucion de la forma [(pos_i_barco1, pos_f_barco1), (pos_i_barco2, pos_f_barco2), ... , (pos_i_barcok, pos_f_barcok)]
print(res)