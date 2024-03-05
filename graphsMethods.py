def generate_complete_graph(n: int) -> list[list[int]]:
    """
    Generates a complete graph with 'n' nodes.

    Args:
        n (int): The number of nodes in the graph.

    Returns:
        list[list[int]]: The adjacency list representation of the complete graph.
    """
    G: list[list[int]] = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                G[i].append(j)
    return G


"""
Sia G un grafo completo con m archi. Descrivere un algoritmo che dato
G rappresentato tramite liste di adiacenza in O(m) ne orienta gli archi
producendo un grafo diretto aciclico
"""
def orienta_grafo_completo(G: list[list[int]]) -> list[list[int]]:
    """
    Orient the edges of a complete undirected graph.

    Args:
        G (list[list[int]]): The adjacency list representation of the graph.

    Returns:
        list[list[int]]: The adjacency list representation of the graph with oriented edges.
    """
    n = len(G)  # Numero di nodi
    archi_orientati = [[] for _ in range(len(G))]  # Lista per memorizzare gli archi orientati

    # Iteriamo su tutte le coppie di nodi distinti
    for u in range(n):
        for v in range(u + 1, n):
            # Orientiamo l'arco u -> v se u è adiacente a v
            if v in G[u]:
                archi_orientati[u].append(v)
            # Altrimenti, orientiamo l'arco v -> u
            else:
                archi_orientati[v].append(u)

    return archi_orientati


def orient_all(u:int, G: list[list[int]], V: list[int]) -> list[list[int]]:
    """
    Recursively orients all edges in the graph starting from node u.

    Args:
        u (int): The starting node.
        G (list[list[int]]): The adjacency list representation of the graph.
        V (list[int]): The visited nodes list.

    Returns:
        list[list[int]]: The updated adjacency list representation of the graph.
    """
    V[u] = 1
    for v in G[u]:
        if V[v] == 0:
            if u in G[v]:
                G[u].remove(v)
                G = orient_all(v, G, V)
            else:
                G = orient_all(v, G, V)
    return G


def conta_pozzi_da_nodo(u: int, G: list[list[int]], V: list[int]) -> int:
    """
    Counts the number of "pozzi" (i.e., nodes with no outgoing edges) starting from a given node in a graph.

    Args:
        u (int): The starting node.
        G (list[list[int]]): The adjacency list representation of the graph.
        V (list[int]): A list to keep track of visited nodes.

    Returns:
        int: The number of "pozzi" starting from the given node.
    """
    V[u] = 1
    somma_pozzi = 0
    if len(G[u]) == 0:
        return 1
    for i in G[u]:
        if V[i] == 0:
            somma_pozzi += conta_pozzi_da_nodo(i, G, V)
    return somma_pozzi

            


# Esempio
#G = generate_complete_graph(4)
#print(G)
#G = orienta_grafo_completo(G)
#print(G)


# Esempio
#G = [[1],
#     [3],
#     [1,4],
#     [4],
#     [2,3],
#     [4]]
#print(G)
#print(orient_all(0, G, [0]*6))

G = [[2,9],[0,2,5,7],[],[4,6],[10],[],[9],[8],[],[10],[3]]
print(conta_pozzi_da_nodo(1, G, [0]*11))