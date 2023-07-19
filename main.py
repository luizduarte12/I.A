from collections import deque

def bfs(grafo, inicio, objetivo):
    fila = deque([(inicio, [inicio])])

    while fila:
        no_atual, caminho = fila.popleft()

        if no_atual == objetivo:
            return caminho

        for vizinho in grafo[no_atual]:
            if vizinho not in caminho:
                fila.append((vizinho, caminho + [vizinho]))

    return None

# Exemplos de utilização
if __name__ == "__main__":
    grafo = {
        '6': ['1', '9', '7'],
        '1': ['2'],
        '9': ['10'],
        '7': ['10', '2'],
        '2': ['3'],
        '10': [],
        '3': ['4', '8'],
        '4': ['5'],
        '5': [],
        '8': ['11'],
        '11': ['12', '13'],
        '12': [],
        '13': ['17'],
        '17': ['18', '16'],
        '16': ['15'],
        '15': ['14'],
        '14': [],
        '18': []
    }

    inicio = '6'
    objetivo1 = '18'
    objetivo2 = '14'

    caminho_para_objetivo1 = bfs(grafo, inicio, objetivo1)
    caminho_para_objetivo2 = bfs(grafo, inicio, objetivo2)

    if caminho_para_objetivo1:
        print(f"Caminho para o objetivo 1 (nó '18'): {caminho_para_objetivo1}")
    else:
        print("Não há caminho para o objetivo 1 a partir do nó inicial.")

    if caminho_para_objetivo2:
        print(f"Caminho para o objetivo 2 (nó '14'): {caminho_para_objetivo2}")
    else:
        print("Não há caminho para o objetivo 2 a partir do nó inicial.")
