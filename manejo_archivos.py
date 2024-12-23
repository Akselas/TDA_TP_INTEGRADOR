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

def leer_resultados_juego(archivo_resultados):
    with open(archivo_resultados, 'r') as f:
        sophia_ganancia = int(f.readline().split(': ')[1])
        mateo_ganancia = int(f.readline().split(': ')[1])
    return sophia_ganancia, mateo_ganancia
    
def obtener_barcos_y_demandas(path):
    
    with open(path, 'r') as archivo:
        # omite las dos primeras líneas
        contenido = archivo.readlines()[2:]

    contenido_filtrado = ''.join(contenido).strip()
    secciones = contenido_filtrado.split("\n\n")

    demandas_filas = list(map(int, secciones[0].splitlines()))
    demandas_columnas = list(map(int, secciones[1].splitlines()))
    largos_barcos = list(map(int, secciones[2].splitlines()))

    return largos_barcos, demandas_filas, demandas_columnas

def dar_resultados_juego_tp3(path, ubicaciones_barcos_solucion, demanda_a_cumplir, demanda_cumplida):
    nombre_carpeta_resultados = carpeta_resultados_juego()
    nombre_archivo_resultados = archivo_resultados_juego(path)
    # Escribir las posiciones de los barcos en orden de mayor a menor tamaño
    with open(os.path.join(nombre_carpeta_resultados, nombre_archivo_resultados), 'w') as archivo_resultados:
        archivo_resultados.write("Posiciones barcos (ordenados de mayor a menor tamaño):\n")
        for i, ubicacion in enumerate(ubicaciones_barcos_solucion):
            if ubicacion is None:
                archivo_resultados.write(f"{i}: None\n")
            else:
                archivo_resultados.write(f"{i}: {ubicacion[0]} - {ubicacion[1]}\n")
        
        # Escribir la demanda cumplida y total
        archivo_resultados.write(f"Demanda cumplida: {demanda_cumplida}\n")
        archivo_resultados.write(f"Demanda total: {demanda_a_cumplir}\n")
