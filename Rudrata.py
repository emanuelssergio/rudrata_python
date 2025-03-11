def hamiltonian_path(graph, path, visited):
    # A função tenta construir um caminho hamiltoniano (um caminho que passa por
    #todos os vértices exatamente uma vez). Ela faz isso explorando cada vizinho
    #possível de maneira recursiva, retrocedendo (backtracking) caso um caminho válido não seja encontrado.


    if len(path) == len(graph):
        return path
    last_vertex = path[-1]
    for neighbor in graph[last_vertex]:
        #busca entre os vertices não visitados recurcivamentes ate encontrar um caminho

        if not visited[neighbor]:
            visited[neighbor] = True
            path.append(neighbor)
            result = hamiltonian_path(graph, path, visited)
            if result:
                return result  # Se encontrou um caminho válido, retorna


            path.pop() #desfaz o caminho
            visited[neighbor] = False

    return None  # Não há caminho hamiltoniano a partir dessa configuração


def find_hamiltonian_path(graph):
    for start_vertex in graph:
        path = [start_vertex]
        visited = {v: False for v in graph}
        visited[start_vertex] = True
        result = hamiltonian_path(graph, path, visited)
        if result:
            return result

    return None  # Nenhum caminho Hamiltoniano encontrado


# Exemplo de uso
graph = {
    0: [1, 2, 4],
    1: [0, 2, 4,5],
    2: [0, 1, 3],
    3: [0, 2,1,5],
    4: [0, 2, 3,5],
    5: [2,0,1,6],
    6: [2,3,4],
    7: [0,3,5],


}


path = find_hamiltonian_path(graph)
if path:
    print("Caminho Hamiltoniano encontrado:", path)
else:
    print("Nenhum caminho Hamiltoniano encontrado.")
