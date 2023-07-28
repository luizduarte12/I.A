import heapq

def distancia_manhattan(no1, no2):
    x1, y1 = int(no1), 0  # Para simplificar, definimos as coordenadas x e y como apenas o valor do nó.
    x2, y2 = int(no2), 0  # Como o grafo é unidimensional, y será sempre 0.
    return abs(x1 - x2) + abs(y1 - y2)

def a_estrela(grafo, no_inicio, nos_objetivo):
    fila_prioridade = [(0, no_inicio)]
    visitados = set()
    custo_acumulado = {no_inicio: 0}
    caminho_anterior = {no_inicio: None}

    while fila_prioridade:
        (custo_atual, no_atual) = heapq.heappop(fila_prioridade)

        if no_atual in visitados:
            continue

        visitados.add(no_atual)

        if no_atual in nos_objetivo:
            caminho = reconstituir_caminho(caminho_anterior, no_atual)
            return caminho, custo_acumulado[no_atual]

        for vizinho, custo in grafo[no_atual].items():
            if vizinho not in visitados:
                novo_custo = custo_acumulado[no_atual] + custo
                if vizinho not in custo_acumulado or novo_custo < custo_acumulado[vizinho]:
                    custo_acumulado[vizinho] = novo_custo
                    custo_total = novo_custo + distancia_manhattan(vizinho, nos_objetivo[0])
                    heapq.heappush(fila_prioridade, (custo_total, vizinho))
                    caminho_anterior[vizinho] = no_atual

    return None, None

def reconstituir_caminho(caminho_anterior, no):
    caminho = []
    while no is not None:
        caminho.insert(0, no)
        no = caminho_anterior[no]
    return caminho

if __name__ == "__main__":
    grafo = {
        '6': {'1': 2, '9': 2, '7': 2},
        '1': {'2': 2, '6': 2},
        '9': {'10': 2, '6': 2},
        '7': {'10': 2, '2': 2, '6': 2},
        '2': {'3': 2, '7': 2, '1': 2},
        '10': {'9': 2, '7': 2},
        '3': {'2': 2, '4': 2},
        '4': {'5': 2, '8': 2, '3': 2},
        '5': {'4': 2},
        '8': {'11': 2, '4': 2},
        '11': {'12': 2, '13': 2, '8': 2},
        '12': {'11': 2},
        '13': {'17': 2, '11': 2},
        '17': {'18': 4, '16': 2, '13': 2},
        '16': {'15': 2, '17': 2},
        '15': {'14': 2, '16': 2},
        '14': {'15': 2},
        '18': {'17': 4}
    }

    no_inicio = '6'
    nos_objetivo = ['18', '14']

    caminho, custo = a_estrela(grafo, no_inicio, nos_objetivo)

    if caminho and custo is not None:
        print(f"Caminho encontrado: {caminho}")
        print(f"Custo acumulado da solução: {custo}")
    else:
        print("Não foi possível encontrar um caminho até o nó objetivo.")
