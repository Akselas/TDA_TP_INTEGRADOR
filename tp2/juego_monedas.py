import sys
sys.path.append("../") 
from manejo_archivos import obtener_lista_monedas, dar_resultados_juego
from jugador import Jugador
from collections import deque

SOPHIA = 'Sophia' 
MATEO = 'Mateo'
ELECCION_ULTIMA_MONEDA = ' agarra la ultima'
ELECCION_PRIMERA_MONEDA = ' agarra la primera'

def primera_moneda_tras_eleccion_mateo(monedas, i, j):
    if monedas[i] >= monedas[j]:
        return i+1
    else:
        return i
    
def max_acumulados_sophia_desde_inicio(monedas, n, max_acumulados, tamaño_inicial):
    for tamaño_actual in range(tamaño_inicial, n+1, 2): 
        max_acumulados_tamaño_actual = []
        for i in range(n - tamaño_actual + 1):
            j = i + tamaño_actual - 1

            sig_i_eligiendo_i = primera_moneda_tras_eleccion_mateo(monedas, i+1, j)
            max_acumulado_eligiendo_i = monedas[i] + max_acumulados[len(max_acumulados) - 1][sig_i_eligiendo_i]
            sig_i_eligiendo_j = primera_moneda_tras_eleccion_mateo(monedas, i, j-1)
            max_acumulado_eligiendo_j = monedas[j] + max_acumulados[len(max_acumulados) - 1][sig_i_eligiendo_j]

            max_acumulados_tamaño_actual.append(max(max_acumulado_eligiendo_i, max_acumulado_eligiendo_j))
        max_acumulados.append(max_acumulados_tamaño_actual)
    
def max_acumulados_sophia_n_par(monedas, n, max_acumulados):
    max_acumulados.append([monedas[i] if monedas[i] >= monedas[i+1] else monedas[i+1] for i in range(n-1)]) # tamaño = 2
    tamaño_inicial = 4
    max_acumulados_sophia_desde_inicio(monedas, n, max_acumulados, tamaño_inicial)
    return max_acumulados

def max_acumulados_sophia_n_impar(monedas, n, max_acumulados):
    max_acumulados.append([monedas[i] for i in range(n)]) # tamaño = 1
    tamaño_inicial = 3
    max_acumulados_sophia_desde_inicio(monedas, n, max_acumulados, tamaño_inicial)
    return max_acumulados

def max_acumulados_sophia(monedas):
    n = len(monedas)
    max_acumulados = []
    if n % 2 == 0:
        return max_acumulados_sophia_n_par(monedas, n, max_acumulados)
    else:
        return max_acumulados_sophia_n_impar(monedas, n, max_acumulados)
    
def elegir_moneda(elecciones, i, j, primera, nombre_hermano):
    if primera:
        elecciones.append(nombre_hermano + ELECCION_PRIMERA_MONEDA)
        i += 1
    else: 
        elecciones.append(nombre_hermano + ELECCION_ULTIMA_MONEDA)
        j -= 1
    return i, j

def elegir_mejor_moneda(elecciones, monedas, i, j, nombre_hermano):
    if monedas[i] >= monedas[j]:
        return elegir_moneda(elecciones, i, j, True, nombre_hermano)
    else:
        return elegir_moneda(elecciones,i, j, False, nombre_hermano)
    
def recuperar_elecciones(monedas, max_ganancias_sophia):
    elecciones = []
    turno_sophia = True

    i = 0
    j = len(monedas) - 1
    tam = len(max_ganancias_sophia) - 1
    while i <= j:
        if turno_sophia:
            if tam == 0:
                i, j = elegir_mejor_moneda(elecciones, monedas, i, j, SOPHIA)
            elif monedas[i] + max_ganancias_sophia[tam-1][primera_moneda_tras_eleccion_mateo(monedas, i+1, j)] == max_ganancias_sophia[tam][i]:
                i, j = elegir_moneda(elecciones, i, j, True, SOPHIA)
            else:
                i, j = elegir_moneda(elecciones, i, j, False, SOPHIA)
            tam -= 1
        else:
            i, j = elegir_mejor_moneda(elecciones, monedas, i, j, MATEO)
        turno_sophia = not turno_sophia

    return elecciones

def juego_monedas(monedas, elecciones, sophia, mateo):
    for eleccion in elecciones:
        if eleccion == SOPHIA + ELECCION_PRIMERA_MONEDA:
            sophia.ganancia += monedas.popleft()
        elif eleccion == SOPHIA + ELECCION_ULTIMA_MONEDA:
            sophia.ganancia += monedas.pop()
        elif eleccion == MATEO + ELECCION_PRIMERA_MONEDA:
            mateo.ganancia += monedas.popleft()
        else:
            mateo.ganancia += monedas.pop()

def jugar(path):
    
    monedas = obtener_lista_monedas(path)
    sophia = Jugador(SOPHIA)
    mateo = Jugador(MATEO)
    max_ganancias_sophia = max_acumulados_sophia(monedas)
    elecciones = recuperar_elecciones(monedas, max_ganancias_sophia)
    juego_monedas(deque(monedas), elecciones, sophia, mateo)
    dar_resultados_juego(path, sophia.ganancia, mateo.ganancia, elecciones)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python juego_monedas.py <path_al_archivo_de_monedas.txt>")
        sys.exit(1)

    path = sys.argv[1]
    jugar(path)