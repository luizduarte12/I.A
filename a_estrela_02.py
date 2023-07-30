import heapq
def manhattan_heuristica(p1, p2):
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])
def a_estrela(grafo, inicio, objetivos):
    fila = [(0, inicio)]
    explorados = set()
    caminho_anterior = {}
    custos = {nodo: float('inf') for nodo in grafo}
    custos[inicio] = 0
    ramificacao = {nodo: 0 for nodo in grafo}

    while fila:
        atual_custo, no_atual = heapq.heappop(fila)
        if no_atual in explorados:
            continue
        explorados.add(no_atual)

        if no_atual in objetivos:
            caminho = [no_atual]
            custo_acumulado = 0
            while no_atual in caminho_anterior:
                pai = caminho_anterior[no_atual]
                caminho.append(pai)
                custo_acumulado += grafo[pai]['arestas'][no_atual]
                no_atual = pai

            caminho.reverse()
            profundidade = len(caminho) - 1
            ramificacao_media = sum(ramificacao.values()) / len(ramificacao)
            ##ramificacao_objetivo = len(grafo[vizinho])
            print(f"Caminho para o objetivo encontrado: {caminho}")
            print(f"Custo acumulado do caminho: {custo_acumulado}")
            print(f"Nós explorados: {explorados}")
            print(f"Profundidade do caminho: {profundidade}")
            print(f"Ramificação máxima: {max(ramificacao.values())}")
            print(f"Ramificação média: {ramificacao_media:.2f}")
            return caminho

        for vizinho, custo_aresta in grafo[no_atual]['arestas'].items():
            novo_custo = custos[no_atual] + custo_aresta
            if novo_custo < custos[vizinho]:
                custos[vizinho] = novo_custo
                heapq.heappush(fila, (novo_custo + manhattan_heuristica(grafo[vizinho]['coordenadas'], grafo[objetivos[0]]['coordenadas']),
                vizinho))
                caminho_anterior[vizinho] = no_atual
                ramificacao[no_atual] += 1
    return None

if __name__ == "__main__":
    grafo = {
        '6': {'coordenadas': (0, 0), 'arestas': {'1': 2, '7': 2, '9': 2}},
        '1': {'coordenadas': (1, 0), 'arestas': {'2': 2}},
        '9': {'coordenadas': (0, 1), 'arestas': {'10': 2}},
        '7': {'coordenadas': (1, 1), 'arestas': {'10': 2, '2': 2}},
        '2': {'coordenadas': (2, 1), 'arestas': {'3': 2}},
        '10': {'coordenadas': (1, 2), 'arestas': {}},
        '3': {'coordenadas': (3, 1), 'arestas': {'4': 2}},
        '4': {'coordenadas': (4, 1), 'arestas': {'5': 2, '8': 2}},
        '5': {'coordenadas': (5, 1), 'arestas': {}},
        '8': {'coordenadas': (3, 2), 'arestas': {'11': 2}},
        '11': {'coordenadas': (3, 3), 'arestas': {'12': 2, '13': 2}},
        '12': {'coordenadas': (3, 4), 'arestas': {}},
        '13': {'coordenadas': (4, 3), 'arestas': {'17': 2}},
        '17': {'coordenadas': (4, 4), 'arestas': {'18': 4, '16': 2}},
        '16': {'coordenadas': (5, 4), 'arestas': {'15': 2}},
        '15': {'coordenadas': (5, 3), 'arestas': {'14': 2}},
        '14': {'coordenadas': (6, 3), 'arestas': {}},
        '18': {'coordenadas': (5, 5), 'arestas': {}}
    }


    inicio = '6'
    objetivos = ['18', '14']

    caminho_objetivo = a_estrela(grafo, inicio, objetivos)

    if not caminho_objetivo:
        print("Não há caminho para nenhum dos objetivos a partir do nó inicial.")
