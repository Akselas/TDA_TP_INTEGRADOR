import sys
sys.path.append("../") 
from manejo_archivos import obtener_lista_monedas, dar_resultados_juego
from jugador import Jugador

SOPHIA = 'Sophia' 
MATEO = 'Mateo'

def maximo_tras_eleccion_mateo(monedas, maximos, i, j):
    if monedas[i] >= monedas[j] and i != len(monedas)-1:
        return maximos[i+1][j]
    else:
        return maximos[i][j-1]

def max_acumulados_sophia(monedas):

    n = len(monedas)

    max_acumulados =[[0] * n for _ in range(n)]
    for i in range(n):
        max_acumulados[i][i] = monedas[i]
    for diag in range(1, n):
        for i in range(n - diag):
            j = i + diag
            max_acumulado_eligiendo_i = monedas[i] + maximo_tras_eleccion_mateo(monedas, max_acumulados, i+1, j)
            max_acumulado_eligiendo_j = monedas[j] + maximo_tras_eleccion_mateo(monedas, max_acumulados, i, j-1)
            max_acumulados[i][j] = max(max_acumulado_eligiendo_i, max_acumulado_eligiendo_j)

    return max_acumulados

#def juego_monedas(monedas, elecciones, sophia, mateo):

def jugar(path):
    
    monedas = obtener_lista_monedas(path)
    sophia = Jugador(SOPHIA)
    mateo = Jugador(MATEO)
    max_ganancias_sophia = max_acumulados_sophia(monedas)
    elecciones = recuperar_elecciones(monedas, max_ganancias_sophia)
    juego_monedas(monedas, elecciones, sophia, mateo)

    dar_resultados_juego(path, sophia.ganancia, mateo.ganancia, elecciones)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python juego_monedas.py <path_al_archivo_de_monedas.txt>")
        sys.exit(1)

    path = sys.argv[1]
    monedas = obtener_lista_monedas(path)
    max_ganancias_sophia = max_acumulados_sophia(monedas)
    for fila in max_ganancias_sophia:
        print(fila)