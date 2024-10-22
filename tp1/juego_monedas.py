import os, sys
from jugador import Jugador
from collections import deque

def juego_monedas(monedas: deque, jugador_n1: Jugador, jugador_n2: Jugador):

    turno_jugador_n1 = True

    while monedas:
        if turno_jugador_n1:
            jugador_n1.ganancia += monedas.popleft() if monedas[0] > monedas[-1] else monedas.pop()
        else:
            jugador_n2.ganancia += monedas.popleft() if monedas[0] < monedas[-1] else monedas.pop()
        
        turno_jugador_n1 = not turno_jugador_n1

def main(path):
    
    with open(path, 'r') as archivo_monedas:
        archivo_monedas.readline() #ingnorar comentario
        linea_valores_monedas = archivo_monedas.readline().strip()
        lista_monedas = list(map(int, linea_valores_monedas.split(';')))
    
    monedas = deque(lista_monedas)
    sophia = Jugador("Sophia")
    mateo = Jugador("Mateo")
    juego_monedas(monedas, sophia, mateo)

    carpeta_resultados = 'archivos_resultados'
    os.makedirs(carpeta_resultados, exist_ok=True)

    nombre_archivo_prueba = os.path.basename(path)
    nombre_sin_extension = os.path.splitext(nombre_archivo_prueba)[0]

    nombre_archivo_resultados = f'resultados_{nombre_sin_extension}.txt'

    with open(os.path.join('archivos_resultados', nombre_archivo_resultados), 'w') as archivo_resultados:
        archivo_resultados.write(f"Ganancia de Sophia: {sophia.ganancia}\n")
        archivo_resultados.write(f"Ganancia de Mateo: {mateo.ganancia}\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python juego_monedas.py <path_al_archivo_de_monedas.txt>")
        sys.exit(1)

    path = sys.argv[1]
    main(path)