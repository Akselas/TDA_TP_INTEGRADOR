import os

CARPETA_RESULTADOS = 'archivos_resultados'

def obtener_lista_monedas(path):
    with open(path, 'r') as archivo_monedas:
        archivo_monedas.readline() #ignorar comentario
        linea_valores_monedas = archivo_monedas.readline().strip()
        return list(map(int, linea_valores_monedas.split(';')))
    
def carpeta_resultados_juego():
    path = os.getcwd()
    carpeta_resultados = os.path.join(path, 'archivos_resultados')
    os.makedirs(carpeta_resultados, exist_ok=True)
    return carpeta_resultados

def archivo_resultados_juego(path):
    nombre_archivo_prueba = os.path.basename(path)
    nombre_sin_extension = os.path.splitext(nombre_archivo_prueba)[0]
    nombre_archivo_resultados = f'resultados_{nombre_sin_extension}.txt'
    return nombre_archivo_resultados

def dar_resultados_juego(path, ganancia_sophia, ganancia_mateo, elecciones):
    nombre_carpeta_resultados = carpeta_resultados_juego()
    nombre_archivo_resultados = archivo_resultados_juego(path)
    with open(os.path.join(nombre_carpeta_resultados, nombre_archivo_resultados), 'w') as archivo_resultados:
        archivo_resultados.write(f"Ganancia de Sophia: {ganancia_sophia}\n")
        archivo_resultados.write(f"Ganancia de Mateo: {ganancia_mateo}\n")
        archivo_resultados.write("\n")
        archivo_resultados.write(f"Elecciones: {'; '.join(elecciones)}")