from juego_batalla_naval import jugar

def tests():
    test3_3_2()
    test5_5_6()
    test8_7_10()
    test10_10_10()  
    test12_12_21()
    test15_10_15()
    test20_20_20()
    test20_25_30()
    test30_25_25()

def leer_resultados_juego(archivo_resultados):

    posiciones_barcos = []
    demanda_incumplida = 0

    return posiciones_barcos, demanda_incumplida

def test3_3_2():
    path = 'archivos_prueba/3_3_2.txt'

    jugar(path)

    resultados_path = f'archivos_resultados/resultados_3_3_2.txt'
    leer_resultados_juego(resultados_path)
    
    
    print("Test 3_3_2: pasó")

def test5_5_6():
    path = 'archivos_prueba/5_5_6.txt'

    jugar(path)

    resultados_path = f'archivos_resultados/resultados_5_5_6.txt'
    leer_resultados_juego(resultados_path)
    
    
    print("Test 5_5_6: pasó")

def test8_7_10():
    path = 'archivos_prueba/8_7_10.txt'

    jugar(path)

    resultados_path = f'archivos_resultados/resultados_8_7_10.txt'
    leer_resultados_juego(resultados_path)
    
    print("Test 8_7_10: pasó")

def test10_10_10():
    path = 'archivos_prueba/10_10_10.txt'

    jugar(path)

    resultados_path = f'archivos_resultados/resultados_10_10_10.txt'
    leer_resultados_juego(resultados_path)
    
    print("Test 10_10_10: pasó")

def test12_12_21():
    path = 'archivos_prueba/12_12_21.txt'

    jugar(path)

    resultados_path = f'archivos_resultados/resultados_12_12_21.txt'
    leer_resultados_juego(resultados_path)
    
    print("Test 12_12_21: pasó")

def test15_10_15():
    path = 'archivos_prueba/15_10_15.txt'

    jugar(path)

    resultados_path = f'archivos_resultados/resultados_15_10_15.txt'
    leer_resultados_juego(resultados_path)
    
    print("Test 15_10_15: pasó")

def test20_20_20():
    path = 'archivos_prueba/20_20_20.txt'

    jugar(path)

    resultados_path = f'archivos_resultados/resultados_20_20_20.txt'
    leer_resultados_juego(resultados_path)

    print("Test 20_20_20: pasó")

def test20_25_30():
    path = 'archivos_prueba/20_25_30.txt'

    jugar(path)

    resultados_path = f'archivos_resultados/resultados_20_25_30.txt'
    leer_resultados_juego(resultados_path)
    
    print("Test 20_25_30: pasó")

def test30_25_25():
    path = 'archivos_prueba/30_25_25.txt'

    jugar(path)

    resultados_path = f'archivos_resultados/resultados_30_25_2.txt'
    leer_resultados_juego(resultados_path)
    
    print("Test 30_25_25: pasó")
