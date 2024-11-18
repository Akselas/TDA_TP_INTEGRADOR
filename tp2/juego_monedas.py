import sys
import time
sys.path.append("../") 
from manejo_archivos import obtener_lista_monedas, dar_resultados_juego
from jugador import Jugador

SOPHIA = 'Sophia' 
MATEO = 'Mateo'

def primera_moneda_tras_eleccion_mateo(monedas, i, j):
    if monedas[i] >= monedas[j] and i != len(monedas)-1:
        return i+1
    else:
        return i
    
def max_acumulados_sophia_desde(monedas, n, max_acumulados, inicio):
    for diferencia_j_i in range(inicio, n, 2): 
        diferencia_j_i_actual = []
        for i in range(n - diferencia_j_i):
            j = i + diferencia_j_i

            sig_i_eligiendo_i = primera_moneda_tras_eleccion_mateo(monedas, i+1, j)
            max_acumulado_eligiendo_i = monedas[i] + max_acumulados[len(max_acumulados) - 1][sig_i_eligiendo_i]
            sig_i_eligiendo_j = primera_moneda_tras_eleccion_mateo(monedas, i, j-1)
            max_acumulado_eligiendo_j = monedas[j] + max_acumulados[len(max_acumulados) - 1][sig_i_eligiendo_j]

            diferencia_j_i_actual.append(max(max_acumulado_eligiendo_i, max_acumulado_eligiendo_j))

        max_acumulados.append(diferencia_j_i_actual)
    
def max_acumulados_sophia_n_par(monedas, n, max_acumulados):
    max_acumulados.append([monedas[i] if monedas[i] >= monedas[i+1] else monedas[i+1] for i in range(n-1)]) # j-i = 1
    inicio = 3
    max_acumulados_sophia_desde(monedas, n, max_acumulados, inicio)
    return max_acumulados

def max_acumulados_sophia_n_impar(monedas, n, max_acumulados):
    max_acumulados.append([monedas[i] for i in range(n)]) # j-i = 0
    inicio = 2
    max_acumulados_sophia_desde(monedas, n, max_acumulados, inicio)
    return max_acumulados

def max_acumulados_sophia(monedas):
    n = len(monedas)
    max_acumulados = []
    if n % 2 == 0:
        return max_acumulados_sophia_n_par(monedas, n, max_acumulados)
    else:
        return max_acumulados_sophia_n_impar(monedas, n, max_acumulados)

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
    inicio_time = time.time()
    max_ganancias_sophia = max_acumulados_sophia(monedas)
    end_time = time.time()
    elapsed_time = end_time - inicio_time
    print(f"Tiempo de ejecución: {elapsed_time:.6f} segundos")
    print(max_ganancias_sophia[-1][-1])