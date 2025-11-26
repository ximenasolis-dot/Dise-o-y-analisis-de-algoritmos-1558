def existe_camino_pd(n, m):
    """
    Determina si existe un camino desde (0, 0) hasta (n-1, m-1)
    usando Programación Dinámica
    n: número de filas, m: número de columnas
    """
    if n <= 0 or m <= 0:
        return False
    # Inici la tabla DP de tamaño n x m
    # dp[i][j] será True si (i, j) es alcanzable
    dp = [[False] * m for _ in range(n)]
    dp[0][0] = True

    # recorre la tabla de arriba a abajo y de izquierda a derecha
    for i in range(n):
        for j in range(m):
            # comprueba si se puede llegar desde 'tres a la izquierda'
            if j >= 3:
                # Si dp[i][j-3] es True, entonces dp[i][j] también lo es
                if dp[i][j - 3]:
                    dp[i][j] = True
            
            # comprueba si se puede llegar desde 'dos hacia arriba'
            if i >= 2:
                # Si dp[i-2][j] es True, entonces dp[i][j] también lo es
                if dp[i - 2][j]:
                    dp[i][j] = True

    # El resultado final está en la casilla destino
    return dp[n - 1][m - 1]

# Ejemplo de uso:
# Tablero 5x7: Origen (0,0) a Destino (4,6)
print(f"¿Existe camino valido? {existe_camino_pd(5, 7)}")