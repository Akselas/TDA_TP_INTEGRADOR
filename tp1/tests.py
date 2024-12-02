from juego_monedas import jugar
from manejo_archivos import leer_resultados_juego


def tests():
    test6()
    test20()
    test25()
    test50()
    test100()
    test1000()
    test10000()
    test20000()
    test_valores_grandes()
    test_empate()
    test_casi_empate()

def test6():
    path = 'archivos_prueba/6.txt'

    jugar(path)

    resultados_path = f'archivos_resultados/resultados_6.txt'
    sophia_ganancia, mateo_ganancia = leer_resultados_juego(resultados_path)
    
    assert sophia_ganancia > mateo_ganancia, f"Test 6 monedas: Sophia no tiene mayor ganancia que Mateo"
    assert sophia_ganancia == 22, f"Test 6 monedas: No devuelve la correcta cantidad de monedas, Sophia tiene: {sophia_ganancia} pesos"
    assert mateo_ganancia == 6, f"Test 6 monedas: No devuelve la correcta cantidad de monedas, Mateo tiene: {mateo_ganancia} pesos"
    print("Test 6 monedas: pasó")

def test20():
    path = 'archivos_prueba/20.txt'

    jugar(path)

    resultados_path = f'archivos_resultados/resultados_20.txt'
    sophia_ganancia, mateo_ganancia = leer_resultados_juego(resultados_path)
    
    assert sophia_ganancia > mateo_ganancia, f"Test 20 monedas: Sophia no tiene mayor ganancia que Mateo"
    assert sophia_ganancia == 7165, f"Test 20 monedas: No devuelve la correcta cantidad de monedas, Sophia tiene: {sophia_ganancia} pesos"
    print("Test 20 monedas: pasó")

def test25():
    path = 'archivos_prueba/25.txt'

    jugar(path)

    resultados_path = f'archivos_resultados/resultados_25.txt'
    sophia_ganancia, mateo_ganancia = leer_resultados_juego(resultados_path)
    
    assert sophia_ganancia > mateo_ganancia, f"Test 25 monedas: Sophia no tiene mayor ganancia que Mateo"
    assert sophia_ganancia == 9635, f"Test 25 monedas: No devuelve la correcta cantidad de monedas, Sophia tiene: {sophia_ganancia} pesos"
    print("Test 25 monedas: pasó")

def test50():
    path = 'archivos_prueba/50.txt'

    jugar(path)

    resultados_path = f'archivos_resultados/resultados_50.txt'
    sophia_ganancia, mateo_ganancia = leer_resultados_juego(resultados_path)
    
    assert sophia_ganancia > mateo_ganancia, f"Test 50 monedas: Sophia no tiene mayor ganancia que Mateo"
    assert sophia_ganancia == 17750, f"Test 50 monedas: No devuelve la correcta cantidad de monedas, Sophia tiene: {sophia_ganancia} pesos"
    print("Test 50 monedas: pasó")

def test100():
    path = 'archivos_prueba/100.txt'

    jugar(path)

    resultados_path = f'archivos_resultados/resultados_100.txt'
    sophia_ganancia, mateo_ganancia = leer_resultados_juego(resultados_path)
    
    assert sophia_ganancia > mateo_ganancia, f"Test 100 monedas: Sophia no tiene mayor ganancia que Mateo"
    assert sophia_ganancia == 35009, f"Test 100 monedas: No devuelve la correcta cantidad de monedas, Sophia tiene: {sophia_ganancia} pesos"
    print("Test 100 monedas: pasó")

def test1000():
    path = 'archivos_prueba/1000.txt'

    jugar(path)

    resultados_path = f'archivos_resultados/resultados_1000.txt'
    sophia_ganancia, mateo_ganancia = leer_resultados_juego(resultados_path)
    
    assert sophia_ganancia > mateo_ganancia, f"Test 1000 monedas: Sophia no tiene mayor ganancia que Mateo"
    assert sophia_ganancia == 357814, f"Test 1000 monedas: No devuelve la correcta cantidad de monedas, Sophia tiene: {sophia_ganancia} pesos"
    print("Test 1000 monedas: pasó")

def test10000():
    path = 'archivos_prueba/10000.txt'

    jugar(path)

    resultados_path = f'archivos_resultados/resultados_10000.txt'
    sophia_ganancia, mateo_ganancia = leer_resultados_juego(resultados_path)
    
    assert sophia_ganancia > mateo_ganancia, f"Test 10000 monedas: Sophia no tiene mayor ganancia que Mateo"
    assert sophia_ganancia == 3550307, f"Test 10000 monedas: No devuelve la correcta cantidad de monedas, Sophia tiene: {sophia_ganancia} pesos"
    print("Test 10000 monedas: pasó")

def test20000():
    path = 'archivos_prueba/20000.txt'

    jugar(path)

    resultados_path = f'archivos_resultados/resultados_20000.txt'
    sophia_ganancia, mateo_ganancia = leer_resultados_juego(resultados_path)
    
    assert sophia_ganancia > mateo_ganancia, f"Test 20000 monedas: Sophia no tiene mayor ganancia que Mateo"
    assert sophia_ganancia == 7139357, f"Test 20000 monedas: No devuelve la correcta cantidad de monedas, Sophia tiene: {sophia_ganancia} pesos"
    print("Test 20000 monedas: pasó")

def test_valores_grandes():
    path = 'archivos_prueba/valores_grandes.txt'

    jugar(path)

    resultados_path = f'archivos_resultados/resultados_valores_grandes.txt'
    sophia_ganancia, mateo_ganancia = leer_resultados_juego(resultados_path)
    
    assert sophia_ganancia > mateo_ganancia, f"Test valores grandes monedas: Sophia no tiene mayor ganancia que Mateo"
    assert sophia_ganancia == 339147000000, f"Test valores grandes monedas: No devuelve la correcta cantidad de monedas, Sophia tiene: {sophia_ganancia} pesos"
    assert mateo_ganancia == 155588000000, f"Test valores grandes monedas: No devuelve la correcta cantidad de monedas, Mateo tiene: {mateo_ganancia} pesos"
    print("Test valores grandes monedas: pasó")

def test_empate():
    path = 'archivos_prueba/empate.txt'

    jugar(path)

    resultados_path = f'archivos_resultados/resultados_empate.txt'
    sophia_ganancia, mateo_ganancia = leer_resultados_juego(resultados_path)
    
    assert sophia_ganancia == mateo_ganancia, f"Test empate monedas: Mateo y Sophia no tienen la misma ganancia"
    assert sophia_ganancia == 50, f"Test empate monedas: No devuelve la correcta cantidad de monedas, Sophia tiene: {sophia_ganancia} pesos"
    assert mateo_ganancia == 50, f"Test empate monedas: No devuelve la correcta cantidad de monedas, Mateo tiene: {mateo_ganancia} pesos"
    print("Test empate monedas: pasó")

def test_casi_empate():
    path = 'archivos_prueba/casi_empate.txt'

    jugar(path)

    resultados_path = f'archivos_resultados/resultados_casi_empate.txt'
    sophia_ganancia, mateo_ganancia = leer_resultados_juego(resultados_path)
    
    assert sophia_ganancia > mateo_ganancia, f"Test casi empate monedas: Sophia no tiene mayor ganancia que Mateo"
    print("Test casi empate monedas: pasó")

if __name__ == "__main__":
    tests()