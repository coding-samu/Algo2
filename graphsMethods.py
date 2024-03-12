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

def DFSMatrix(u,M):
    """
    Performs a Depth-First Search (DFS) on a given matrix representation of a graph.

    Parameters:
    u (int): The starting vertex for the DFS.
    M (list): The adjacency matrix representing the graph.

    Returns:
    list: A list of boolean values indicating whether each vertex was visited during the DFS.
    """
    def DFSr(u,M,visitati):
        visitati[u] = True
        for i in range(len(M)):
            if M[u][i] and not visitati[i]:
                DFSr(i,M,visitati)
    visitati = [False]*len(M)
    DFSr(u,M,visitati) 
    return visitati

def DFSList(u, G):
    """
    Performs a Depth-First Search (DFS) starting from a given vertex in a graph.

    Parameters:
    u (int): The starting vertex for the DFS.
    G (list): The adjacency list representation of the graph.

    Returns:
    list: A list indicating which vertices have been visited during the DFS.
    """
    def DFSr(u, G, visitati):
        visitati[u] = True
        for i in G[u]:
            if not visitati[i]:
                DFSr(i, G, visitati)
    visitati = [False] * len(G)
    DFSr(u, G, visitati) 
    return visitati

def padri(u, G):
    """
    Finds the parent nodes of each node in a graph using Depth-First Search (DFS).

    Args:
        u (int): The starting node.
        G (list): The adjacency list representation of the graph.

    Returns:
        list: A list containing the parent nodes of each node in the graph.
    """
    def DFSr(x, G, P):
        for y in G[x]:
            if P[y] == -1:
                P[y] = x
                DFSr(y, G, P)
    
    P = [-1] * len(G)
    P[u] = u
    DFSr(u, G, P)
    return P

def cammino(u, P):
    """
    Returns the path from vertex u to the source vertex in a graph represented by the predecessor array P.

    Parameters:
    u (int): The vertex to find the path from.
    P (list): The predecessor array representing the graph.

    Returns:
    list: The path from vertex u to the source vertex.
    """
    if P[u] == -1: return []
    path = []
    while P[u] != u:
        path.append(u)
        u = P[u]
    path.append(u)
    path.reverse()
    return path

def camminoRicorsivo(u, P):
    """
    Returns the recursive path from node u to the root node in a graph.

    Args:
        u (int): The starting node.
        P (list): The list of parent nodes.

    Returns:
        list: The path from node u to the root node.
    """
    if P[u] == -1: return []
    if P[u] == u: return [u]
    return camminoRicorsivo(P[u], P) + [u]


def pozzo(M):
    """
    Determines if a given graph represented by an adjacency matrix is a sink (pozzo) or not.

    Args:
        M (list): The adjacency matrix representing the graph.

    Returns:
        bool: True if the graph is a sink, False otherwise.
    """
    L = [x for x in range(len(M))]
    while len(L) > 1:
        a = L.pop()
        b = L.pop()
        if M[a][b]:
            L.append(b)
        else:
            L.append(a)
    x = L.pop()
    for j in range(len(M)):
        if M[x][j]:
            return False
    for i in range(len(M)):
        if M[i][x] and i != x:
            return False
    return True

def sortTopologico(G):
    """
    Performs a topological sort on a directed acyclic graph (DAG).

    Args:
        G (list): The adjacency list representation of the graph.

    Returns:
        list: The topologically sorted order of the vertices in the graph.

    """
    def DFSr(u, G, V, lista):
        V[u] = 1
        for v in G[u]:
            if V[v] == 0:
                DFSr(v, G, V, lista)
        lista.append(u)

    V = [0]*len(G)
    lista = []
    for i in range(len(G)):
        if V[i] == 0:
            DFSr(i, G, V, lista)
    lista.reverse()
    return lista

def subtree(P,x):
    # P = [3,4,3,5,3,4,5,1]
    # x = 5
    subtree = []
    for i in range(len(P)):
        if P[i] != -1:
            path, is_sub = path_to_root(P, i, x)
            if not is_sub:
                for u in path:
                    P[u] = -1
    for i in range(len(P)):
        if P[i] != -1:
            subtree.append(i+1)
    return subtree

def path_to_root(P, u, x):
    path = []
    is_sub = False
    path.append(u)
    if u == x:
        is_sub = True
        return path, is_sub
    while P[u] != u:
        if P[u] == -1:
            is_sub = False
            break
        path.append(P[u])
        u = P[u]
        if u == x: 
            is_sub = True
            break
    return path, is_sub

print(subtree([2,3,2,4,2,3,4,0],4))

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

#G = [[2,9],[0,2,5,7],[],[4,6],[10],[],[9],[8],[],[10],[3]]
#print(conta_pozzi_da_nodo(1, G, [0]*11))
            
#G = [[1,5,6],[2,6],[],[2,4,6],[5,6],[],[2,5]]
#print(sortTopologico(G))