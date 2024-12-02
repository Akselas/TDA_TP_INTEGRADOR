import sys
sys.path.append("../") 
from bt import batalla_naval
from manejo_archivos import obtener_barcos_y_demandas, dar_resultados_juego_tp3

def jugar(path):

    barcos, demandas_filas, demandas_columnas = obtener_barcos_y_demandas(path)
    res = batalla_naval(demandas_filas, demandas_columnas, barcos)
    print(res)
    ubicaciones_barcos_solucion = res[0]
    demanda_a_cumplir = sum(demandas_filas) + sum(demandas_columnas)
    demanda_incumplida_solucion = res[1][0]
    demanda_cumplida =  demanda_a_cumplir - demanda_incumplida_solucion
    dar_resultados_juego_tp3(path, ubicaciones_barcos_solucion, demanda_a_cumplir, demanda_cumplida)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python juego_batalla_naval.py <path_al_archivo_de_x_y_z.txt>")
        sys.exit(1)

    path = sys.argv[1]
    jugar(path)