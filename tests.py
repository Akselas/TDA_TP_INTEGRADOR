from TP1_juego_monedas import juego_monedas
from jugador import Jugador

def pruebas():
    test_comun()
    test_numeros_grandes()

def test_comun():
    "Arrange"
    arr = [3,9,1,8,2,5]
    sofia = Jugador("Sofia")
    mateo = Jugador("Mateo")
    turno = True
    
    "Act"
    juego_monedas(arr, turno, sofia, mateo)
    
    "Assert"
    assert sofia.monedero == 22, f"No devuelve la correcta cantidad de monedas, sofia tiene: {sofia.monedero} pesos"
    assert mateo.monedero == 6, f"No devuelve la correcta cantidad de monedas, mateo tiene: {mateo.monedero} pesos"
    print("Test comun paso")

def test_numeros_grandes():
    "Arrange"
    arr = [413759, 698681, 730491, 596380, 3014, 416704, 874886, 35898, 686505, 491032]
    sofia = Jugador("Sofia")
    mateo = Jugador("Mateo")
    turno = True
    "Act"
    juego_monedas(arr, turno, sofia, mateo)
    
    "Assert"
    assert sofia.monedero == 3391470, f"No devuelve la correcta cantidad de monedas, sofia tiene: {sofia.monedero} pesos"
    assert mateo.monedero == 1555880, f"No devuelve la correcta cantidad de monedas, mateo tiene: {mateo.monedero} pesos"
    print("Tests con numeros grandes paso")


pruebas()
