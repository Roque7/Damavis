def juego_laberinto(laberinto):  # Función que calcula los movimientos necesarios en el laberinto
    filas = len(laberinto)  # Guardo la cantidad de filas del laberinto
    columnas = len(laberinto[0])  # Guardo la cantidad de columnas del laberinto

    inicio = (0, 0, 'h')  # Posición de inicio con orientación horizontal
    cola = [(inicio, 0)]  # Lista para almacenar las posiciones y movimientos
    visitado = []  # Lista para registrar las posiciones visitadas


    while cola:
        posicion, movimientos = cola.pop(0)  # Uso pop(0) para eliminar el primer elemento (como cola)

        x, y, orientacion = posicion  # Extraigo las coordenadas y la orientación

        if x == filas - 1 and y == columnas - 1:  # Si llegué al final, retorno la cantidad de movimientos
            return movimientos

        visitado.append((x, y, orientacion))  # Agrego la posición actual a la lista de visitadas

        # Explorar movimientos horizontales
        if orientacion == 'h':{}
        #nuevo_x, nuevo_y

        # Explorar movimientos verticales
        elif orientacion == 'v':{}
        # nuevo_x, nuevo_y


        # Cambiar la orientación del rod
        nueva_orientacion = 'v' if orientacion == 'h' else 'h'


    return -1  # Si no puede llegar al final, retorno -1
