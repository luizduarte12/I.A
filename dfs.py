def dfs(grafo, inicio, objetivos):
    pilha = [(inicio, [inicio])]
    profundidade = {inicio: 0}
    ramificacao = {inicio: 0}

    while pilha:
        no_atual, caminho = pilha.pop()

        if no_atual in objetivos:
            custo = len(caminho) - 1
            profundidade_objetivo = len(caminho) - 1
            ramificacao_objetivo = len(grafo[no_atual])
            print(f"Caminho para o objetivo (nó '{no_atual}'): {caminho}")
            print(f"Custo da solução: {custo}")
            print(f"Profundidade do objetivo: {profundidade_objetivo}")
            print(f"Ramificação máxima: {ramificacao_objetivo}")
            print(f"Ramificação média: {sum(ramificacao.values()) / len(ramificacao):.2f}")
            return caminho

        for vizinho in grafo[no_atual]:
            if vizinho not in caminho:
                pilha.append((vizinho, caminho + [vizinho]))
                profundidade[vizinho] = profundidade[no_atual] + 1
                ramificacao[vizinho] = len(grafo[vizinho])

    return None

if __name__ == "__main__":
    grafo = {
        '6': ['1', '9', '7'],
        '1': ['2', '6'],
        '9': ['10', '6'],
        '7': ['10', '2', '6'],
        '2': ['3', '7', '1'],
        '10': ['9', '7'],
        '3': ['2', '4'],
        '4': ['5', '8', '3'],
        '5': ['4'],
        '8': ['11', '4'],
        '11': ['12', '13', '8'],
        '12': ['11'],
        '13': ['17', '11'],
        '17': ['18', '16', '13'],
        '16': ['15', '17'],
        '15': ['14', '16'],
        '14': ['15'],
        '18': ['17']
    }

    inicio = '6'
    objetivos = ['14', '18']

    caminho_objetivo = dfs(grafo, inicio, objetivos)

    if not caminho_objetivo:
        print("Não há caminho para nenhum dos objetivos a partir do nó inicial.")
