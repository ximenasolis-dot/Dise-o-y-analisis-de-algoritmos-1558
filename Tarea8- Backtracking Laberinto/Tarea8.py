def cargar_tablero(nombre_archivo):
    """
    Lee la estructura del laberinto desde un archivo .txt.
    Línea 1: Filas. Línea 2: Columnas.
    Contenido: '1' (pared), '0' (pasillo), 'E' (entrada), 'S' (salida).
    """
    try:
        # Se abre el archivo
        with open(nombre_archivo, 'r') as archivo:
            # Lee las dimensiones del laberinto
            num_filas = int(archivo.readline().strip())
            num_columnas = int(archivo.readline().strip())
            mapa_laberinto = []

            for _ in range(num_filas):
                linea = [celda.strip() for celda in archivo.readline().strip().split(',')]
                mapa_laberinto.append(linea)

        return mapa_laberinto, num_filas, num_columnas
    
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{nombre_archivo}'.")
        # Retorna valores nulos para indicar el fallo
        return None, 0, 0
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return None, 0, 0

def encontrar_coordenadas(tablero, simbolo_buscado):
    """Encuentra la posición (fila, columna) de un símbolo ('E' o 'S') en el laberinto."""
    
    for r in range(len(tablero)):
        for c in range(len(tablero[0])):
            if tablero[r][c] == simbolo_buscado:
                # Retorna las coordenadas (fila, columna)
                return (r, c)
    # Retorna None si el símbolo no se encuentra
    return None

def es_movimiento_valido(tablero, matriz_visitados, fila_destino, columna_destino):
    """Verifica si el movimiento a la celda de destino es permitido."""
    alto = len(tablero)
    ancho = len(tablero[0])

    if fila_destino < 0 or fila_destino >= alto or columna_destino < 0 or columna_destino >= ancho:
        return False
    
    valor_celda = tablero[fila_destino][columna_destino]

    if valor_celda in ('0', 'E', 'S') and not matriz_visitados[fila_destino][columna_destino]:
        return True

    return False

##Función Principal de Solución
def buscar_solucion_laberinto(tablero):
    """
    Resuelve el laberinto usando el algoritmo de Búsqueda en Profundidad (DFS).
    Emplea una pila para gestionar las rutas a explorar.
    """
    pos_inicio = encontrar_coordenadas(tablero, 'E')
    pos_final = encontrar_coordenadas(tablero, 'S')

    if pos_inicio is None or pos_final is None:
        print("Error: El laberinto debe contener una Entrada (E) y una Salida (S).")
        return

    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Arriba, Abajo, Izquierda, Derecha

    pila_dfs = [(pos_inicio, [pos_inicio])]
    matriz_visitados = [[False for _ in range(len(tablero[0]))] for _ in range(len(tablero))]

    # Bucle principal de DFS
    while pila_dfs:
        # Aqui se extrae el último elemento de la pila (comportamiento LIFO))
        pos_actual, camino_actual = pila_dfs.pop()      
        fila_actual, columna_actual = pos_actual

        if pos_actual == pos_final:
            print("\n¡Ruta de solución encontrada (de E a S)!")
            # Imprimir la ruta encontrada
            for paso in camino_actual:
                print(f"Fila: {paso[0]}, Columna: {paso[1]}")
            return

        if not matriz_visitados[fila_actual][columna_actual]:
            matriz_visitados[fila_actual][columna_actual] = True

            # Se explora las 4 direcciones posibles
            for df, dc in movimientos:
                nueva_fila = fila_actual + df
                nueva_columna = columna_actual + dc

                # Se verifica si el movimiento al vecino es válido
                if es_movimiento_valido(tablero, matriz_visitados, nueva_fila, nueva_columna):
                    nueva_posicion = (nueva_fila, nueva_columna)
                    nuevo_camino = camino_actual + [nueva_posicion]
                    pila_dfs.append((nueva_posicion, nuevo_camino))

    # Si la pila se vacía, significa que no se encontró ninguna ruta
    print("\nNo existe ninguna ruta desde E hasta S en este laberinto.")

##Punto de Inicio
if __name__ == "__main__":
    # Nombre del archivo del laberinto
    archivo_laberinto = "entrada.txt" 
    datos_tablero = cargar_tablero(archivo_laberinto)
    
    if datos_tablero[0] is not None:
        mapa_laberinto, num_filas, num_columnas = datos_tablero
        
        print(f"Tablero del Laberinto ({num_filas}x{num_columnas}):")
        for fila in mapa_laberinto:
            print(' '.join(fila))
            
        # Inicia la búsqueda de la solución :)
        buscar_solucion_laberinto(mapa_laberinto)