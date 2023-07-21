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
    objetivo1 = '14'
    objetivo2 = '18'

    caminho_para_objetivo1 = bfs(grafo, inicio, objetivo1)
    caminho_para_objetivo2 = bfs(grafo, inicio, objetivo2)

    if caminho_para_objetivo1:
        print(f"Caminho para o objetivo 1 (nó '14'): {caminho_para_objetivo1}")
    else:
        print("Não há caminho para o objetivo 1 a partir do nó inicial.")

    if caminho_para_objetivo2:
        print(f"Caminho para o objetivo 2 (nó '18'): {caminho_para_objetivo2}")
    else:
        print("Não há caminho para o objetivo 2 a partir do nó inicial.")
