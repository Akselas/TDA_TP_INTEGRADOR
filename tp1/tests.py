from juego_monedas import juego_monedas
from jugador import Jugador
from collections import deque

def pruebas():
    test1()
    test2_numeros_grandes()

def test1():
    "Arrange"
    arr = deque([3,9,1,8,2,5])
    sofia = Jugador("Sofia")
    mateo = Jugador("Mateo")
    turno = True
    
    "Act"
    juego_monedas(arr, sofia, mateo)
    
    "Assert"
    assert sofia.monedero == 22, f"Test 1: No devuelve la correcta cantidad de monedas, sofia tiene: {sofia.monedero} pesos"
    assert mateo.monedero == 6, f"Test 1: No devuelve la correcta cantidad de monedas, mateo tiene: {mateo.monedero} pesos"
    print("Test 1: pasó")

def test2_numeros_grandes():
    "Arrange"
    arr = deque([413759, 698681, 730491, 596380, 3014, 416704, 874886, 35898, 686505, 491032])
    sofia = Jugador("Sofia")
    mateo = Jugador("Mateo")
    turno = True

    "Act"
    juego_monedas(arr, sofia, mateo)
    
    "Assert"
    assert sofia.monedero == 3391470, f"Test 2 - Números grandes: No devuelve la correcta cantidad de monedas, sofia tiene: {sofia.monedero} pesos"
    assert mateo.monedero == 1555880, f"Test 2 - Números grandes: No devuelve la correcta cantidad de monedas, mateo tiene: {mateo.monedero} pesos"
    print("Test 2 - Números grandes: pasó")


pruebas()
