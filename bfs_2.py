from collections import deque

def bfs(grafo, inicio, objetivos):
    fila = deque([(inicio, [inicio])])
    profundidade = {inicio: 0}
    ramificacao = {inicio: 0}
    explorados = set()

    while fila:
        no_atual, caminho = fila.popleft()

        if no_atual in objetivos:
            custo = len(caminho) - 1
            profundidade_objetivo = len(caminho) - 1
            ramificacao_objetivo = len(grafo[vizinho])
            print(f"Caminho para o objetivo (nó '{no_atual}'): {caminho}")
            print(f"Custo da solução: {custo}")
            print(f"Profundidade do objetivo: {profundidade_objetivo}")
            print(f"Ramificação máxima: {ramificacao_objetivo}")
            print(f"Ramificação média: {sum(ramificacao.values()) / len(ramificacao):.2f}")
            print(f"Nós explorados: {explorados}")
            return caminho

        for vizinho in grafo[no_atual]:
            if vizinho not in caminho:
                fila.append((vizinho, caminho + [vizinho]))
                profundidade[vizinho] = profundidade[no_atual] + 1
                ramificacao[vizinho] = len(grafo[vizinho])
                explorados.add(vizinho)
    return None


if __name__ == "__main__":
    grafo = {
        '6': ['1', '7', '9'],
        '1': ['2', '6'],
        '9': ['6', '10'],
        '7': ['6', '2', '10'],
        '2': ['1', '3', '7'],
        '10': ['7', '9'],
        '3': ['2', '4'],
        '4': ['3', '5', '8'],
        '5': ['4'],
        '8': ['4', '11'],
        '11': ['8', '12', '13'],
        '12': ['11'],
        '13': ['11', '17'],
        '17': ['13', '16', '18'],
        '16': ['15', '17'],
        '15': ['14', '16'],
        '14': ['15'],
        '18': ['17']
    }

    inicio = '6'
    objetivos = ['14', '18']

    caminho_objetivo = bfs(grafo, inicio, objetivos)
    if not caminho_objetivo:
        print("Não há caminho para nenhum dos objetivos a partir do nó inicial.")

