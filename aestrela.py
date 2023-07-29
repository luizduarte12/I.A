from collections import deque

def manhattan_distance(atual, objetivo):
    x1, y1 = atual
    x2, y2 = objetivo
    return (abs(x1 - x2) + abs(y1 - y2))

def imprimir_no(no):
    return f'no {no}'

def get_cost(no_atual, vizinho):
    # Custo para cada movimento é 2, exceto se for para a célula 18, que custa 4
    return 4 if vizinho == (2, 2) else 2

def astar(grafo, inicio, objetivos):
    fila = deque([(inicio, [inicio], 0, 0)])

    while fila:
        no_atual, caminho, custo_acumulado, custo = fila.popleft()

        if no_atual in objetivos:
            return caminho, custo_acumulado

        for vizinho in grafo[no_atual]:
            novo_custo = custo + get_cost(no_atual, vizinho)
            distancia_objetivos = [manhattan_distance(vizinho, objetivo) for objetivo in objetivos]
            heuristica = min(distancia_objetivos)
            prioridade = novo_custo + heuristica
            fila.append((vizinho, caminho + [vizinho], custo_acumulado + novo_custo, novo_custo))

        # Ordena a fila com base na prioridade (custo + heurística)
        fila = deque(sorted(fila, key=lambda x: x[2] + min(manhattan_distance(x[0], objetivo) for objetivo in objetivos)))

    return None, None

# Exemplo de utilização
if __name__ == "__main__":
    grafo = {
        (0, 0): [(0, 1), (1, 0)],
        (0, 1): [(0, 0), (0, 2)],
        (0, 2): [(0, 1), (1, 2)],
        (1, 0): [(0, 0), (1, 1)],
        (1, 1): [(1, 0), (1, 2), (2, 1)],
        (1, 2): [(0, 2), (1, 1)],
        (2, 1): [(1, 1), (2, 2)],
        (2, 2): [(2, 1)]
    }

    inicio = (0, 0)  # Nó inicial
    objetivos = [(2, 2), (1, 4)]  # Nós objetivos

    resultado, custo_acumulado = astar(grafo, inicio, objetivos)

    if resultado:
        caminho_str = ', '.join(imprimir_no(no) for no in resultado)
        print(f"Caminho encontrado: {caminho_str}")
        print(f"Custo acumulado: {custo_acumulado}")
    else:
        print("Não há caminho para nenhum dos nós objetivos a partir do nó inicial.")
