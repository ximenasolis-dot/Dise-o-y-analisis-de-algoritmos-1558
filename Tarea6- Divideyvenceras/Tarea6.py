# Definición de la función principal de Merge Sort
def merge_sort(lista_a_ordenar):
    if len(lista_a_ordenar) <= 1:
        return lista_a_ordenar

    punto_medio = len(lista_a_ordenar) // 2
    
    mitad_izquierda = lista_a_ordenar[:punto_medio]
    
    mitad_derecha = lista_a_ordenar[punto_medio:]

    lista_ordenada_izquierda = merge_sort(mitad_izquierda)
    lista_ordenada_derecha = merge_sort(mitad_derecha)
    
    lista_resultado = []
    
    # Inicializar índices para iterar sobre las sub-listas ordenadas
    indice_izq = 0
    indice_der = 0

    while indice_izq < len(lista_ordenada_izquierda) and indice_der < len(lista_ordenada_derecha):
        if lista_ordenada_izquierda[indice_izq] <= lista_ordenada_derecha[indice_der]:
            lista_resultado.append(lista_ordenada_izquierda[indice_izq])
            indice_izq += 1  
        else:
            lista_resultado.append(lista_ordenada_derecha[indice_der])
            indice_der += 1 
    while indice_izq < len(lista_ordenada_izquierda):
        lista_resultado.append(lista_ordenada_izquierda[indice_izq])
        indice_izq += 1
    while indice_der < len(lista_ordenada_derecha):
        lista_resultado.append(lista_ordenada_derecha[indice_der])
        indice_der += 1
    return lista_resultado

# --- Ejemplo de Uso ---

# Lista inicial desordenada
lista_original = [3, 6, 8, 2, 11, 4, 16, 23, 7, 10]

# Llamada a la función para ordenar la lista
lista_ordenada_final = merge_sort(lista_original)

# Impresión de resultados
print("El arreglo original es:", lista_original)
print("="*60)
print("El arreglo acomodado es:", lista_ordenada_final)