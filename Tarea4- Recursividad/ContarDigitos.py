def ContarDigitos (numeroEntero):
    if numeroEntero ==0:
        return 0
    else:
        return 1 + ContarDigitos (numeroEntero//10)
    
numeroEntero = 57839038
resultado = ContarDigitos (numeroEntero)
print ("Cantidad de digitos: ", resultado)