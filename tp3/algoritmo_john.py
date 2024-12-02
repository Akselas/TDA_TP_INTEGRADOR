LIBRE = '-'

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

def ubicar_barco_vertical(tablero, dem_fil, dem_col, numero_barco, tamaño_barco, pos_inicial, solucion):
    fila_inicial, col = pos_inicial
    fila_final = fila_inicial + tamaño_barco-1

    for fila in range(fila_inicial, fila_final + 1):
        tablero[fila][col] = numero_barco
        dem_fil[fila] -= 1
        dem_col[col] -= 1
    solucion[numero_barco] = (pos_inicial, (fila_final, col))

def ubicar_barco_horizontal(tablero, dem_fil, dem_col, numero_barco, tamaño_barco, pos_inicial, solucion):
    fila, col_inicial = pos_inicial
    col_final = col_inicial + tamaño_barco-1

    for col in range(col_inicial, col_final + 1):
        tablero[fila][col] = numero_barco
        dem_fil[fila] -= 1
        dem_col[col] -= 1
    solucion[numero_barco] = (pos_inicial, (fila, col_final))

def aproximacion_john_jellicoe(n, m, barcos, demandas_filas, demandas_columnas, tablero):
    
    numero_barco = 0
    solucion = [None]*len(barcos)

    def puede_colocar_barco(fila, columna, longitud, horizontal):
        if horizontal:
            return puedo_ubicar_horizontal(tablero, demandas_filas, n, demandas_columnas, m, longitud, (fila,columna))
        else:
            return puedo_ubicar_vertical(tablero, demandas_filas, n, demandas_columnas, m, longitud, (fila,columna))
        
    def colocar_barco(tablero, demandas_filas, demandas_columnas, barco, longitud, posicion, solucion, horizontal):
        if horizontal:
            ubicar_barco_horizontal(tablero, demandas_filas, demandas_columnas, barco, longitud, posicion, solucion)
        else:
            ubicar_barco_vertical(tablero, demandas_filas, demandas_columnas, barco, longitud, posicion, solucion)

    while numero_barco < len(barcos):
        long_barco = barcos[numero_barco]

        max_demanda_fila = max(demandas_filas)
        filas_con_max_demanda = [i for i, d in enumerate(demandas_filas) if d == max_demanda_fila]
        
        max_demanda_columna = max(demandas_columnas)
        columnas_con_max_demanda = [i for i, d in enumerate(demandas_columnas) if d == max_demanda_columna]
        colocado = False

        for fila in filas_con_max_demanda:
            for columna in range(m):
                if not colocado and puede_colocar_barco(fila, columna, long_barco, horizontal=True):
                    colocar_barco(tablero, demandas_filas, demandas_columnas, numero_barco, long_barco, (fila, columna), solucion, horizontal=True)
                    colocado = True

        for columna in columnas_con_max_demanda:
            for fila in range(n):
                if not colocado and puede_colocar_barco(fila, columna, long_barco, horizontal=False):
                    colocar_barco(tablero, demandas_filas, demandas_columnas, numero_barco, long_barco, (fila, columna), solucion, horizontal=False)
                    break 

        numero_barco += 1

    demanda_incumplida = sum(demandas_filas) + sum(demandas_columnas)

    return solucion, demanda_incumplida

def batalla_naval_aprox(dem_fil, dem_col, barcos):
    
    n = len(dem_fil)
    m = len(dem_col)
    tablero = [[LIBRE for _ in range(m)] for _ in range(n)]
    barcos.sort(reverse=True)
    solucion = aproximacion_john_jellicoe(n, m, barcos, dem_fil, dem_col, tablero)
    return solucion