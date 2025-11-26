def encontrar_todos_caminos_backtracking(n, m):
    """
    Encuentra todos los caminos desde (0, 0) hasta (n-1, m-1)
    usando Backtracking.
    """
    caminos_encontrados = []
    # Función recursiva de Backtracking
    def buscar(r, c, camino_actual):
        if not (0 <= r < n and 0 <= c < m):
            return
        
        if r == n - 1 and c == m - 1:
            # Añade el camino completo a la lista de soluciones
            caminos_encontrados.append(list(camino_actual))
            return

        camino_actual.append((r, c + 3))
        buscar(r, c + 3, camino_actual)
        # BACKTRACK: aqui se elimina la casilla para probar otra opcion
        camino_actual.pop()

        camino_actual.append((r + 2, c))
        buscar(r + 2, c, camino_actual)
        # BACKTRACK: Elimina la casilla para terminar de explorar la rama
        camino_actual.pop()
        
    # se inicia la búsqueda desde el origen (0, 0)
    buscar(0, 0, [(0, 0)])
    return caminos_encontrados

# Ejemplo de uso:
# Tablero 5x7: Origen (0,0) a Destino (4,6)
caminos = encontrar_todos_caminos_backtracking(5, 7)
print(f"Total de caminos: {len(caminos)}")
for i, camino in enumerate(caminos):
    print(f"Camino {i+1}: {camino}")