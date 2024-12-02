Se tiene una carpeta distinta para cada sección del trabajo.

En las carpetas tp1 y tp2 hay un archivo `juego_monedas.py`, que tiene un main que recibe un archivo por parametro. El archivo debe ser un .txt con formato como en los archivos provistos por la cátedra como casos de prueba.

Para ejecutarlos, ejecutar por terminal 

```bash
$ python3 juego_monedas.py archivos_prueba/archivo.txt
```

y se generará la salida esperada en una carpeta llamada `archivos_resultados` dentro de la sección que corresponda.

Para la tercera parte, la forma de ejecutar es la misma pero se tiene un archivo `juego_batalla_naval.py` y se debe respetar el formato de archivos de los juegos de batalla naval. Si se quiere ejecutar el algoritmo de aproximación en lugar del de backtracking, descomentar la linea comentada en la función `jugar()` y comentar la correspondiente al algoritmo de bt en el archivo.

Además, hay archivos llamado `tests.py` en tp1 y tp2 que simula juegos de monedas con distintos archivos .txt y testea que Sophia sea la ganadora (o haya empate en el caso de todas las monedas iguales) y que las ganancias de monedas sean las esperadas si se siguió el algoritmo propuesto. Esto es más que nada para comprobar que no se rompe nada al modificar cosas en los algoritmos. 


Las mediciones de tiempo y casos de prueba con grandes volumenes para el algoritmo de aproximación se encuentran en el notebook y están divididos por las secciones correspondientes. 
