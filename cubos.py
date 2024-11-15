from collections import deque

# Definimos los cubos y las posiciones iniciales.
cubos = ['A', 'B', 'C']
# Definimos una estructura de estado, donde cada cubo puede estar en otro cubo o en la mesa.
estado_inicial = {
    'A': 'B',  # A está sobre B
    'B': 'C',  # B está sobre C
    'C': 'mesa'  # C está en la mesa
}

# Función para mover un cubo
def mover_cubo(estado, cubo, destino):
    nuevo_estado = estado.copy()
    nuevo_estado[cubo] = destino
    return nuevo_estado

# Función para generar movimientos válidos
def movimientos_validos(estado):
    movimientos = []
    for cubo in cubos:
        # Si el cubo está en la mesa, podemos moverlo a cualquier otro cubo
        if estado[cubo] == 'mesa':
            for otro_cubo in cubos:
                if otro_cubo != cubo and estado[otro_cubo] == 'mesa':
                    movimientos.append((cubo, otro_cubo))
        else:
            # Si el cubo está sobre otro cubo, podemos moverlo a la mesa
            movimientos.append((cubo, 'mesa'))
    return movimientos

# Función para imprimir el plan de movimientos
def imprimir_plan(plan):
    print("Plan de movimientos:")
    for mov in plan:
        print(f"Mover {mov[0]} a {mov[1]}")

# Función de búsqueda en profundidad
def resolver_cubos(estado_inicial, estado_final):
    stack = deque([(estado_inicial, [])])  # pila de búsqueda con estado y plan
    visitados = set()
    
    while stack:
        estado_actual, plan = stack.pop()
        estado_tupla = tuple(sorted(estado_actual.items()))  # convertir estado en tupla para verificación
        
        if estado_tupla in visitados:
            continue
        
        visitados.add(estado_tupla)
        
        # Verificamos si hemos llegado al estado final
        if estado_actual == estado_final:
            return plan
        
        # Generar movimientos y actualizar el plan
        for cubo, destino in movimientos_validos(estado_actual):
            nuevo_estado = mover_cubo(estado_actual, cubo, destino)
            nuevo_plan = plan + [(cubo, destino)]
            stack.append((nuevo_estado, nuevo_plan))
    
    return None

# Definir el estado final deseado
estado_final = {
    'A': 'mesa',
    'B': 'mesa',
    'C': 'mesa'
}

# Ejecutar el algoritmo para resolver el problema
plan_solucion = resolver_cubos(estado_inicial, estado_final)

# Imprimir el plan si se encontró una solución
if plan_solucion:
    imprimir_plan(plan_solucion)
else:
    print("No se encontró una solución.")
