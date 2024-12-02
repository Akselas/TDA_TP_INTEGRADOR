from juego_monedas import jugar
from manejo_archivos import leer_resultados_juego

def tests():
    test5()
    test10()
    test20()
    test25()
    test50()
    test100()
    test1000()
    test2000()
    test5000()
    test10000()

def test5():
    path = 'archivos_prueba/5.txt'

    jugar(path)

    resultados_path = f'archivos_resultados/resultados_5.txt'
    sophia_ganancia, mateo_ganancia = leer_resultados_juego(resultados_path)
    
    assert sophia_ganancia > mateo_ganancia, f"Test 5 monedas: Sophia no tiene mayor ganancia que Mateo"
    assert sophia_ganancia == 1483, f"Test 5 monedas: No devuelve la correcta cantidad de monedas, Sophia tiene: {sophia_ganancia} pesos"
    assert mateo_ganancia == 1268, f"Test 5 monedas: No devuelve la correcta cantidad de monedas, Mateo tiene: {mateo_ganancia} pesos"
    print("Test 5 monedas: pasó")

def test10():
    path = 'archivos_prueba/10.txt'

    jugar(path)

    resultados_path = f'archivos_resultados/resultados_10.txt'
    sophia_ganancia, mateo_ganancia = leer_resultados_juego(resultados_path)
    
    assert sophia_ganancia > mateo_ganancia, f"Test 10 monedas: Sophia no tiene mayor ganancia que Mateo"
    assert sophia_ganancia == 2338, f"Test 10 monedas: No devuelve la correcta cantidad de monedas, Sophia tiene: {sophia_ganancia} pesos"
    assert mateo_ganancia == 1780, f"Test 10 monedas: No devuelve la correcta cantidad de monedas, Mateo tiene: {mateo_ganancia} pesos"
    print("Test 10 monedas: pasó")

def test20():
    path = 'archivos_prueba/20.txt'

    jugar(path)

    resultados_path = f'archivos_resultados/resultados_20.txt'
    sophia_ganancia, mateo_ganancia = leer_resultados_juego(resultados_path)
    
    assert sophia_ganancia > mateo_ganancia, f"Test 20 monedas: Sophia no tiene mayor ganancia que Mateo"
    assert sophia_ganancia == 5234, f"Test 20 monedas: No devuelve la correcta cantidad de monedas, Sophia tiene: {sophia_ganancia} pesos"
    assert mateo_ganancia == 4264, f"Test 20 monedas: No devuelve la correcta cantidad de monedas, Mateo tiene: {mateo_ganancia} pesos"
    print("Test 20 monedas: pasó")

def test25():
    path = 'archivos_prueba/25.txt'

    jugar(path)

    resultados_path = f'archivos_resultados/resultados_25.txt'
    sophia_ganancia, mateo_ganancia = leer_resultados_juego(resultados_path)
    
    assert sophia_ganancia > mateo_ganancia, f"Test 25 monedas: Sophia no tiene mayor ganancia que Mateo"
    assert sophia_ganancia == 7491, f"Test 25 monedas: No devuelve la correcta cantidad de monedas, Sophia tiene: {sophia_ganancia} pesos"
    assert mateo_ganancia == 6523, f"Test 25 monedas: No devuelve la correcta cantidad de monedas, Mateo tiene: {mateo_ganancia} pesos"
    print("Test 25 monedas: pasó")

def test50():
    path = 'archivos_prueba/50.txt'

    jugar(path)

    resultados_path = f'archivos_resultados/resultados_50.txt'
    sophia_ganancia, mateo_ganancia = leer_resultados_juego(resultados_path)
    
    assert sophia_ganancia > mateo_ganancia, f"Test 50 monedas: Sophia no tiene mayor ganancia que Mateo"
    assert sophia_ganancia == 14976, f"Test 50 monedas: No devuelve la correcta cantidad de monedas, Sophia tiene: {sophia_ganancia} pesos"
    assert mateo_ganancia == 13449, f"Test 50 monedas: No devuelve la correcta cantidad de monedas, Mateo tiene: {mateo_ganancia} pesos"
    print("Test 50 monedas: pasó")

def test100():
    path = 'archivos_prueba/100.txt'

    jugar(path)

    resultados_path = f'archivos_resultados/resultados_100.txt'
    sophia_ganancia, mateo_ganancia = leer_resultados_juego(resultados_path)
    
    assert sophia_ganancia > mateo_ganancia, f"Test 100 monedas: Sophia no tiene mayor ganancia que Mateo"
    assert sophia_ganancia == 28844, f"Test 100 monedas: No devuelve la correcta cantidad de monedas, Sophia tiene: {sophia_ganancia} pesos"
    assert mateo_ganancia == 22095, f"Test 100 monedas: No devuelve la correcta cantidad de monedas, Mateo tiene: {mateo_ganancia} pesos"
    print("Test 100 monedas: pasó")

def test1000():
    path = 'archivos_prueba/1000.txt'

    jugar(path)

    resultados_path = f'archivos_resultados/resultados_1000.txt'
    sophia_ganancia, mateo_ganancia = leer_resultados_juego(resultados_path)
    
    assert sophia_ganancia > mateo_ganancia, f"Test 1000 monedas: Sophia no tiene mayor ganancia que Mateo"
    assert sophia_ganancia == 1401590, f"Test 1000 monedas: No devuelve la correcta cantidad de monedas, Sophia tiene: {sophia_ganancia} pesos"
    assert mateo_ganancia == 1044067, f"Test 1000 monedas: No devuelve la correcta cantidad de monedas, Mateo tiene: {mateo_ganancia} pesos"
    print("Test 1000 monedas: pasó")

def test2000():
    path = 'archivos_prueba/2000.txt'

    jugar(path)

    resultados_path = f'archivos_resultados/resultados_2000.txt'
    sophia_ganancia, mateo_ganancia = leer_resultados_juego(resultados_path)
    
    assert sophia_ganancia > mateo_ganancia, f"Test 2000 monedas: Sophia no tiene mayor ganancia que Mateo"
    assert sophia_ganancia == 2869340, f"Test 2000 monedas: No devuelve la correcta cantidad de monedas, Sophia tiene: {sophia_ganancia} pesos"
    assert mateo_ganancia == 2155520, f"Test 2000 monedas: No devuelve la correcta cantidad de monedas, Mateo tiene: {mateo_ganancia} pesos"
    print("Test 2000 monedas: pasó")

def test5000():
    path = 'archivos_prueba/5000.txt'

    jugar(path)

    resultados_path = f'archivos_resultados/resultados_5000.txt'
    sophia_ganancia, mateo_ganancia = leer_resultados_juego(resultados_path)
    
    assert sophia_ganancia > mateo_ganancia, f"Test 5000 monedas: Sophia no tiene mayor ganancia que Mateo"
    assert sophia_ganancia == 9939221, f"Test 5000 monedas: No devuelve la correcta cantidad de monedas, Sophia tiene: {sophia_ganancia} pesos"
    assert mateo_ganancia == 7617856, f"Test 5000 monedas: No devuelve la correcta cantidad de monedas, Mateo tiene: {mateo_ganancia} pesos"
    print("Test 5000 monedas: pasó")

def test10000():
    path = 'archivos_prueba/10000.txt'

    jugar(path)

    resultados_path = f'archivos_resultados/resultados_10000.txt'
    sophia_ganancia, mateo_ganancia = leer_resultados_juego(resultados_path)
    
    assert sophia_ganancia > mateo_ganancia, f"Test 10000 monedas: Sophia no tiene mayor ganancia que Mateo"
    assert sophia_ganancia == 34107537, f"Test 10000 monedas: No devuelve la correcta cantidad de monedas, Sophia tiene: {sophia_ganancia} pesos"
    assert mateo_ganancia == 25730392, f"Test 10000 monedas: No devuelve la correcta cantidad de monedas, Mateo tiene: {mateo_ganancia} pesos"
    print("Test 10000 monedas: pasó")

if __name__ == "__main__":
    tests()