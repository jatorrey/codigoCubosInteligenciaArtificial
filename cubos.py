def mover_cubos_a_mesa(estado_inicial):
    # Mover todos los cubos a la mesa
    estado_actual = estado_inicial
    plan = []
    while any(estado_actual[cubo] != 'mesa' for cubo in ['A', 'B', 'C']):
        for cubo in ['C', 'A', 'B']:
            if estado_actual[cubo] != 'mesa' and not any(estado_actual[c] == cubo for c in ['A', 'B', 'C']):
                # Mover el cubo a la mesa si no tiene otro cubo encima
                estado_actual[cubo] = 'mesa'
                plan.append((cubo, 'mesa'))
                break
            else:
                # Buscar un cubo que esté encima de otro cubo y moverlo
                for c in ['A', 'B', 'C']:
                    if estado_actual[c] == cubo:
                        # Mover el cubo que está encima a la mesa
                        estado_actual[c] = 'mesa'
                        plan.append((c, 'mesa'))
                        break
    return estado_actual, plan

def mover_cubos_a_estado_final(estado_inicial, estado_final):
    # Mover todos los cubos a la mesa
    estado_mesa, plan_mesa = mover_cubos_a_mesa(estado_inicial)
    
    # Hacer los movimientos necesarios para llegar al estado final
    estado_actual = estado_mesa
    plan = plan_mesa
    while estado_actual != estado_final:
        for cubo in ['C', 'A', 'B']:
            if estado_actual[cubo] != estado_final[cubo]:
                # Mover el cubo al lugar correcto
                if estado_final[cubo] == 'mesa':
                    estado_actual[cubo] = 'mesa'
                    plan.append((cubo, 'mesa'))
                else:
                    estado_actual[cubo] = estado_final[cubo]
                    plan.append((cubo, estado_final[cubo]))
                break
    return plan

estado_inicial = {
    'C': 'A',
    'A': 'B',
    'B': 'mesa'
}

estado_final = {
    'A': 'B',
    'B': 'C',
    'C': 'mesa'
}

plan = mover_cubos_a_estado_final(estado_inicial, estado_final)

print("\nPlan de movimientos:")
for movimiento in plan:
    if movimiento[1] == 'mesa':
        print(f"Mover {movimiento[0]} a la mesa")
    else:
        print(f"Mover {movimiento[0]} a {movimiento[1]}")

print("\nEstado final:")
for cubo, posicion in estado_final.items():
    if posicion == 'mesa':
        print(f"{cubo} | --- | mesa")
    else:
        print(f"{cubo} | --- | {posicion}")