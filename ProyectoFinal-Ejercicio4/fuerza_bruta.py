# la función calcula el doble del área del triángulo usando la fórmula del determinante
def area2(p1, p2, p3):
    return abs(
        p1[0] * (p2[1] - p3[1]) +
        p2[0] * (p3[1] - p1[1]) +
        p3[0] * (p1[1] - p2[1])
    )

# lee las coordenadas del archivo campo.in
postes = []
try:
    with open("campo.in", "r") as f:
        for line in f:
            x, y = map(int, line.split())
            if x == -1 and y == -1:
                break
            postes.append((x, y))
except FileNotFoundError:
    print("Error: El archivo 'campo.in' no se encontró.")
    exit()

n = len(postes)
max_area_doble = 0  # Almacena el doble del área máxima
mejor_trio = None

# busca por fuerza bruta (O(N^3))
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            area_actual_doble = area2(postes[i], postes[j], postes[k])

            # Compara con el área máxima actual y actualiza si es mayor
            if area_actual_doble > max_area_doble:
                max_area_doble = area_actual_doble
                mejor_trio = (postes[i], postes[j], postes[k])

print("Triángulo de mayor área (Fuerza Bruta):")
if mejor_trio:
    for p in mejor_trio:
        print(p[0], p[1])
    
    # El área real es la mitad del valor calculado
    print("Área =", max_area_doble / 2)
else:
    # Esto ocurre si n < 3
    print("No hay suficientes postes para formar un triángulo.")