def suma (lista):
    if lista == []:
        print ("Lista vacia")
        return 0
    else: 
        print ("suma", lista [0], "con los numeros que faltan", lista [1:])
        return lista [0] + suma (lista [1:])

numeros = [10, 20, 30, 40, 50]
resultado = suma (numeros)
print ("resultado final de la suma:", resultado) 
