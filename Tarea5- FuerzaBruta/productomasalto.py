def encontrar_maximo_producto(numeros):
    """Encuentra el producto más grande de un par de numeros en una lista"""
    
    max_producto = float('-inf')

    #las variables para guardar los 2 numeros que generan el producto mas alto
    iMayor = 0
    jMayor = 0

    #itera sobre cada numeros de la lista con un indice
    for i in range(len(numeros)):
        for j in range(i + 1, len(numeros)):
            producto = numeros[i] * numeros[j]
            if producto > max_producto:
                max_producto = producto
                iMayor = numeros[i]
                jMayor = numeros[j]

    #imprime el resultado 
    print("El producto más alto es:", max_producto, "que es la multiplicación de:", iMayor, "y", jMayor)

# Lista de números de entrada
datos = [-9, 3, 5, -2, 9, -7, 4, 8, 6]

encontrar_maximo_producto (datos)