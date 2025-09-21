def EliminarValorDePosicionMedia (pila, medio, actual = 0):
    if actual == medio:
        pila.pop()
        return

    tope = pila.pop()

    EliminarValorDePosicionMedia (pila, medio, actual + 1)

    pila.append (tope)


pila = [1, 2, 3, 4, 5, 6, 7]   
medio = (len(pila)-1)// 2

print ("Pila original:", pila)
EliminarValorDePosicionMedia (pila, medio)
print ("Pila sin el valor de posicion media :", pila)
