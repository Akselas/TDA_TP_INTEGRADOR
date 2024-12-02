import sys
sys.path.append("../") 
from bt import batalla_naval
from algoritmo_john import batalla_naval_aprox
from manejo_archivos import obtener_barcos_y_demandas, dar_resultados_juego_tp3

def jugar(path):

    barcos, demandas_filas, demandas_columnas = obtener_barcos_y_demandas(path)
    demanda_a_cumplir = sum(demandas_filas) + sum(demandas_columnas)
    ubicaciones_barcos_solucion, demanda_incumplida_solucion = batalla_naval(demandas_filas, demandas_columnas, barcos)
    
    #ubicaciones_barcos_solucion, demanda_incumplida_solucion = batalla_naval_aprox(demandas_filas, demandas_columnas, barcos)
    demanda_cumplida =  demanda_a_cumplir - demanda_incumplida_solucion
    dar_resultados_juego_tp3(path, ubicaciones_barcos_solucion, demanda_a_cumplir, demanda_cumplida)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python juego_batalla_naval.py <path_al_archivo_de_x_y_z.txt>")
        sys.exit(1)

    path = sys.argv[1]
    jugar(path)