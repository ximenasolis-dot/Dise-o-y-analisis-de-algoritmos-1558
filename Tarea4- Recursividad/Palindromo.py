def esPalindromo (cadena):
    if len (cadena) <= 1:
        return "es palíndromo"

        
    if cadena[0] != cadena[-1]:
        return "no es palíndromo"
        
    return esPalindromo(cadena[1:-1])  


palabra1 = "seres"
palabra2 = "manzana"
palabra3 = "radar"
palabra4 = "mariposa"

print(palabra1, "->", esPalindromo(palabra1))
print(palabra2, "->", esPalindromo(palabra2))  
print(palabra3, "->", esPalindromo(palabra3))  
print(palabra4, "->", esPalindromo(palabra4))  