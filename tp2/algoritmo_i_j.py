def maximo_tras_eleccion_mateo(monedas, maximos, i, j):
    if monedas[i] >= monedas[j] and i != len(monedas)-1:
        return maximos[i+1][j]
    else:
        return maximos[i][j-1]

def max_acumulados_sophia(monedas):
    n = len(monedas)

    max_acumulados =[[0] * n for _ in range(n)]
    
    if n % 2 != 0:
        for i in range(n):
            max_acumulados[i][i] = monedas[i]
    
    if n % 2 == 0:
        start = 1
    else:
        start = 2
    
    for diag in range(start, n, 2):
        for i in range(n - diag):
            j = i + diag
            max_acumulado_eligiendo_i = monedas[i] + maximo_tras_eleccion_mateo(monedas, max_acumulados, i+1, j)
            max_acumulado_eligiendo_j = monedas[j] + maximo_tras_eleccion_mateo(monedas, max_acumulados, i, j-1)
            max_acumulados[i][j] = max(max_acumulado_eligiendo_i, max_acumulado_eligiendo_j)

    return max_acumulados