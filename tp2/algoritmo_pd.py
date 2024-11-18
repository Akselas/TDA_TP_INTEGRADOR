SOPHIA = 'Sophia' 
MATEO = 'Mateo'
PRIMERA = True
ULTIMA = False
ELECCION_ULTIMA_MONEDA = ' agarra la ultima'
ELECCION_PRIMERA_MONEDA = ' agarra la primera'

def primera_moneda_tras_eleccion_mateo(monedas, i, j):
    if monedas[i] >= monedas[j]:
        return i+1
    else:
        return i
    
def max_acumulados_sophia_desde(monedas, n, max_acumulados, k_inicial):
    for k_actual in range(k_inicial, n+1, 2): 
        max_acumulados_k_actual = []
        for i in range(n - k_actual + 1):
            j = i + k_actual - 1

            sig_i_eligiendo_i = primera_moneda_tras_eleccion_mateo(monedas, i+1, j)
            max_acumulado_eligiendo_i = monedas[i] + max_acumulados[len(max_acumulados) - 1][sig_i_eligiendo_i]
            sig_i_eligiendo_j = primera_moneda_tras_eleccion_mateo(monedas, i, j-1)
            max_acumulado_eligiendo_j = monedas[j] + max_acumulados[len(max_acumulados) - 1][sig_i_eligiendo_j]

            max_acumulados_k_actual.append(max(max_acumulado_eligiendo_i, max_acumulado_eligiendo_j))
        max_acumulados.append(max_acumulados_k_actual)
    
def max_acumulados_sophia_n_par(monedas, n, max_acumulados):
    max_acumulados.append([monedas[i] if monedas[i] >= monedas[i+1] else monedas[i+1] for i in range(n-1)]) # k = 2
    k_inicial = 4
    max_acumulados_sophia_desde(monedas, n, max_acumulados, k_inicial)
    return max_acumulados

def max_acumulados_sophia_n_impar(monedas, n, max_acumulados):
    max_acumulados.append([monedas[i] for i in range(n)]) # k = 1
    k_inicial = 3
    max_acumulados_sophia_desde(monedas, n, max_acumulados, k_inicial)
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
        return elegir_moneda(elecciones, i, j, PRIMERA, nombre_hermano)
    else:
        return elegir_moneda(elecciones,i, j, ULTIMA, nombre_hermano)
    
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
                i, j = elegir_moneda(elecciones, i, j, PRIMERA, SOPHIA)
            else:
                i, j = elegir_moneda(elecciones, i, j, ULTIMA, SOPHIA)
            tam -= 1
        else:
            i, j = elegir_mejor_moneda(elecciones, monedas, i, j, MATEO)
        turno_sophia = not turno_sophia

    return elecciones

def elecciones_hermanos(monedas):

    max_ganancias_sophia = max_acumulados_sophia(monedas)
    return recuperar_elecciones(monedas, max_ganancias_sophia)