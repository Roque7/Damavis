def juego_laberinto(laberinto):  # Función que calcula los movimientos necesarios en el laberinto
    filas = len(laberinto)  # Guardo la cantidad de filas del laberinto
    columnas = len(laberinto[0])  # Guardo la cantidad de columnas del laberinto

    inicio = (0, 0, 'h')  # Posición de inicio con orientación horizontal
    cola = [(inicio, 0)]  # Lista para almacenar las posiciones y movimientos
    visitado = []  # Lista para registrar las posiciones visitadas


    while cola:
        posicion, movimientos = cola.pop(0)  # Uso pop(0) para eliminar el primer elemento (como cola)

        x, y, orientacion = posicion  # Extraigo las coordenadas y la orientación

