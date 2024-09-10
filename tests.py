from TP1_juego_monedas import juego_monedas
from jugador import Jugador

def pruebas():

    arr = [3,9,1,8,2,5]
    sofia = Jugador("Sofia")
    mateo = Jugador("Mateo")
    turno = True
    juego_monedas(arr, turno, sofia, mateo)
    assert sofia.monedero == 22, "No devuelve la correcta cantidad de monedas, sofia tiene: {sofia.monedero} monedas"
    assert mateo.monedero == 6, "No devuelve la correcta cantidad de monedas, mateo tiene: {mateo.monedero} monedas"
    print("Tests Pasaron")

pruebas()