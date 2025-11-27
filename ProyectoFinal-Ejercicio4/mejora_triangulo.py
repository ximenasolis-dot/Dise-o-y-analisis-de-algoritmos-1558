from itertools import combinations
# función para calcular el producto cruzado
def producto_cruzado(p_origen, p_a, p_b):
    return (p_a[0] - p_origen[0]) * (p_b[1] - p_origen[1]) - (p_a[1] - p_origen[1]) * (p_b[0] - p_origen[0])

# Función que calcula el doble del área del triángulo formado por los puntos a, b, y c.
def calcular_doble_area(p_vertice1, p_vertice2, p_vertice3):
    return abs(producto_cruzado(p_vertice1, p_vertice2, p_vertice3))

# lista para almacenar las coordenadas de los postes
lista_postes = [] 
try:
    with open("campo.in", "r") as archivo_entrada:
        for linea in archivo_entrada:
            coord_x, coord_y = map(int, linea.split())
            
            if coord_x == -1 and coord_y == -1:
                break
            
            lista_postes.append((coord_x, coord_y))
except FileNotFoundError:
    print("Error: El archivo 'campo.in' no se encontró.")
    exit()

# --- CÁLCULO DE LA ENVOLTURA CONVEXA (CONVEX HULL) ---
puntos_ordenados = sorted(lista_postes)
borde_inferior = []
for poste in puntos_ordenados:

    while len(borde_inferior) >= 2 and producto_cruzado(borde_inferior[-2], 
    borde_inferior[-1], poste) <= 0:
        borde_inferior.pop()
    borde_inferior.append(poste)

borde_superior = []
# Se itera sobre los puntos en orden inverso
for poste in reversed(puntos_ordenados):
    # Se aplica la misma lógica para eliminar puntos que no forman giros a la izquierda
    while len(borde_superior) >= 2 and producto_cruzado(borde_superior[-2], 
    borde_superior[-1], poste) <= 0:
        borde_superior.pop()
    borde_superior.append(poste)

# Se excluyen el último de borde_inferior y el último de borde_superior
vertices_envoltura = borde_inferior[:-1] + borde_superior[:-1]

# --- BÚSQUEDA DEL TRIÁNGULO DE MAYOR ÁREA ---
# El triángulo de mayor área debe tener sus vértices en la envoltura convexa
area_maxima_doble = 0
vertices_maximo_triangulo = None

for p1, p2, p3 in combinations(vertices_envoltura, 3):
    # Calcular el doble del área del triángulo actual.
    area_actual_doble = calcular_doble_area(p1, p2, p3)
    # Actualizar si se encuentra un área mayor.
    if area_actual_doble > area_maxima_doble:
        area_maxima_doble = area_actual_doble
        vertices_maximo_triangulo = (p1, p2, p3)

# --- RESULTADO ---
print("Triangulo de mayor área encontrado:")
# Verificación: si no hay suficientes puntos para un triángulo.
if vertices_maximo_triangulo:
    for punto in vertices_maximo_triangulo:
        print(punto[0], punto[1])
    # El área real es la mitad del valor calculado.
    print("Área =", area_maxima_doble / 2)
else:
    print("No hay suficientes postes para formar un triángulo.")
    exit()
# Generar el archivo de salida "campo.out".
try:
    with open("campo.out", "w") as archivo_salida:
        for coord_x, coord_y in vertices_maximo_triangulo:
            archivo_salida.write(f"{coord_x} {coord_y}\n")
except Exception as e:
    print(f"Error al escribir en 'campo.out': {e}")