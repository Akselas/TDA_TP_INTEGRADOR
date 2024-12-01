import sys
sys.path.append("../") 
from bt import res
from manejo_archivos import obtener_barcos_y_demandas, dar_resultados_juego_tp3
from jugador import Jugador
from collections import deque


def juego_barcos(barcos, demandas_filas, demandas_columnas):
    pass

def jugar(path):

    barcos = obtener_barcos_y_demandas[0]
    demandas_filas= obtener_barcos_y_demandas[1]
    demandas_columnas= obtener_barcos_y_demandas[2]
    demanda_incumplida = res[1]
    juego_barcos(barcos, demandas_filas, demandas_columnas)
    dar_resultados_juego_tp3(path, barcos, demanda_incumplida)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python juego_monedas.py <path_al_archivo_de_x_y_z.txt>")
        sys.exit(1)

    path = sys.argv[1]
    jugar(path)