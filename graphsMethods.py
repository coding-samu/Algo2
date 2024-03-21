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

def parent(u, G):
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

def subtree(P, x):
    """
    Returns the subtree of a given node in a tree represented by a parent array.

    Args:
        P (list): The parent array representing the tree.
        x (int): The node for which the subtree is to be found.

    Returns:
        list: The list of nodes in the subtree of the given node.

    Example:
        >>> P = [3, 4, 3, 5, 3, 4, 5, 1]
        >>> x = 5
        >>> subtree(P, x)
        [4, 5, 6, 7]
    """
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
    """
    Returns the path from node `u` to the root node in the graph represented by the parent array `P`.
    
    Args:
        P (list): The parent array representing the graph.
        u (int): The starting node.
        x (int): The target node.
    
    Returns:
        tuple: A tuple containing the path from `u` to the root node and a boolean indicating if `x` is a sub-node of `u`.
    """
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

#print(subtree([2,3,2,4,2,3,4,0],4))

def ordinamento_topologico(G: list[list[int]]) -> list[list[int]]:
    """
    Perform topological sorting on a directed acyclic graph (DAG).

    Args:
        G (list[list[int]]): The adjacency list representation of the graph.

    Returns:
        list[list[int]]: The topologically sorted order of the vertices in the graph.

    """
    gradoEnt = [0 for _ in G]
    for u in G:
        for v in G[u]:
            gradoEnt[v] += 1
    sorgenti = [u for u in range(len()) if gradoEnt[u] == 0]
    ST = []
    while sorgenti:
        u = sorgenti.pop()
        ST.append(u)
        for v in G[u]:
            gradoEnt[v] -= 1
            if gradoEnt[v] == 0:
                sorgenti.append(v)
    if len(ST) == len(G):
        return ST
    return []

def ordinamento_topologico_dfs(G: list[list[int]]) -> list[list[int]]:
    """
    Performs a depth-first search (DFS) on a directed acyclic graph (DAG) to obtain a topological ordering of its vertices.

    Args:
        G (list[list[int]]): The adjacency list representation of the DAG.

    Returns:
        list[list[int]]: The topological ordering of the vertices.

    """
    def dfs(u, G, V, ST):
        V[u] = 1
        for v in G[u]:
            if V[v] == 0:
                dfs(v, G, V, ST)
        ST.append(u)
    
    V = [0 for _ in G]
    ST = []
    
    for u in range(len(G)):
        if V[u] == 0:
            dfs(u, G, V, ST)
    
    ST.reverse()
    return ST

def verifica_ciclo_grafo_non_diretto_da_nodo(u:int, G: list[list[int]]) -> bool:
    """
    Checks if there is a cycle in an undirected graph starting from a given node.

    Parameters:
    u (int): The starting node.
    G (list[list[int]]): The adjacency list representation of the graph.

    Returns:
    bool: True if a cycle is found, False otherwise.
    """

    def DFSr(u, padre, G, visitati):
        visitati[u] = 1
        for v in G[u]:
            if visitati[v] == 1:
                if v != padre:
                    return True
            else:
                if DFSr(v, u, G, visitati):
                    return True
        return False
    
    visitati = [0] * len(G)
    return DFSr(u, u, G, visitati)

def verifica_ciclo_grafo_non_diretto(G: list[list[int]]) -> bool:
    """
    Checks if a non-directed graph contains a cycle.

    Args:
        G (list[list[int]]): The adjacency list representation of the graph.

    Returns:
        bool: True if the graph contains a cycle, False otherwise.
    """
    def DFSr(u, padre, G, visitati):
        visitati[u] = 1
        for v in G[u]:
            if visitati[v] == 1:
                if v != padre:
                    return True
            else:
                if DFSr(v, u, G, visitati):
                    return True
        return False
    
    visitati = [0] * len(G)

    for u in range(len(G)):
        if DFSr(u, u, G, visitati): return True
    
    return False

def verifica_ciclo_grafo_diretto_da_nodo(u: int, G: list[list[int]]) -> bool:
    """
    Checks if there is a cycle in a directed graph starting from a given node.

    Args:
        u (int): The starting node.
        G (list[list[int]]): The adjacency list representation of the directed graph.

    Returns:
        bool: True if a cycle is found, False otherwise.
    """
    def DFSr(u, G, visitati):
        visitati[u] = 1
        for v in G[u]:
            if visitati[v] == 1:
                return True
            if visitati[v] == 0:
                if DFSr(v, G, visitati):
                    return True
        visitati[u] = 2
        return False
    
    visitati = [0] * len(G)
    return DFSr(u, G, visitati)

def verifica_ciclo_grafo_diretto_da_nodo(G: list[list[int]]) -> bool:
    """
    Verifies if a directed graph contains a cycle starting from a given node.

    Args:
        G (list[list[int]]): The adjacency list representation of the directed graph.

    Returns:
        bool: True if a cycle is found, False otherwise.
    """
    def DFSr(u, G, visitati):
        visitati[u] = 1
        for v in G[u]:
            if visitati[v] == 1:
                return True
            if visitati[v] == 0:
                if DFSr(v, G, visitati):
                    return True
        visitati[u] = 2
        return False
    
    visitati = [0] * len(G)
    
    for u in range(len(G)):
        if DFSr(u, G, visitati): return True

    return False


"""
Dato in input un grafo G rappresentato tramite liste di adiacenza, devo scorrerlo tramite DFS partendo dal nodo 0 e devo contare gli archi in avanti (ossia gli archi da un antenato a un discendente), gli archi all'indietro (ossia gli archi da un discendente a un antenato) e gli archi di attraversamento (cioè gli archi che vanno da destra verso sinistra).

Per esempio, dato il grafo G = [[1,2],[3],[3],[4,5],[5],[6],[1]]
L'output sarà (1,1,1)
Arco in avanti: 3-5
Arco all'indietro: 6-1
Arco di attraversamento: 2-3
"""
def count_edges(G):
    """
    Counts the number of forward, backward, and cross edges in a directed graph.

    Args:
        G (list): The adjacency list representation of the directed graph.

    Returns:
        tuple: A tuple containing the count of forward, backward, and cross edges.

    """
    # Rest of the code...
def count_edges(G):
    # Numero di nodi nel grafo
    n = len(G)
    
    # Inizializzazione delle liste per tenere traccia delle visite e dei tempi di scoperta e completamento
    visited = [False] * n  # Segna se un nodo è stato visitato durante la DFS
    discovery = [0] * n    # Memorizza il tempo di scoperta di ciascun nodo
    finish = [0] * n       # Memorizza il tempo di completamento di ciascun nodo
    
    # Utilizziamo una lista per tenere traccia del tempo corrente nella DFS
    time = [0]
    
    # Contatori per gli archi in avanti, all'indietro e di attraversamento
    forward = backward = cross = 0

    # Funzione di ricerca in profondità (DFS)
    def dfs(v):
        nonlocal forward, backward, cross
        
        # Segna il nodo come visitato e registra il tempo di scoperta
        visited[v] = True
        discovery[v] = time[0]
        time[0] += 1
        
        # Iterazione sui vicini del nodo corrente
        for u in G[v]:
            if not visited[u]:  # Se il vicino non è stato visitato, visitarlo
                dfs(u)
            elif discovery[v] < discovery[u]:  # Se l'arco è in avanti
                forward += 1
                print(f"forward: {v}-{u}")
            elif finish[u] == 0:  # Se l'arco è all'indietro
                backward += 1
                print(f"backward: {v}-{u}")
            else:  # Se l'arco è di attraversamento
                cross += 1
                print(f"cross: {v}-{u}")
        
        # Dopo aver esplorato tutti i vicini, registra il tempo di completamento
        finish[v] = time[0]
        time[0] += 1

    # Avvia la DFS a partire dal nodo 0
    dfs(0)
    
    # Restituisce il conteggio degli archi in avanti, all'indietro e di attraversamento
    return forward, backward, cross

def find_path_all(u, G):
    """
    Finds all paths from a given node 'u' in a graph 'G'.

    Parameters:
    - u: The starting node.
    - G: The graph represented as an adjacency list.

    Returns:
    - path: A list of paths from 'u' to all other nodes in 'G'.
    """

    def dfs(u, parent, G, path, D, time):
        path.append(u)
        time[0] += 1
        D[u] = time[0]
        for v in G[u]:
            if v != parent:
                if D[v] == 0 or D[v] > D[u]:
                    dfs(v, u, G, path, D, time)
                    path.append(u)
        return path

    D = [0] * len(G)
    time = [0]
    path = []
    return dfs(u, u, G, path, D, time)

def find_bridges(G):
    """
    Finds all the bridges in a given graph.

    Args:
        G (list): The adjacency list representation of the graph.

    Returns:
        list: A list of tuples representing the bridges in the graph. Each tuple contains two vertices (x, y),
              indicating that there is a bridge between vertex x and vertex y.
    """
    def dfs(x, t, G, height, bridges):
        from math import inf
        height[x] = t
        ret = inf
        for y in G[x]:
            if height[y] == -1:
                a = dfs(y, t+1, G, height, bridges)
                if t < a:
                    bridges.append((x,y))
                ret = min(ret, a)
            elif height[y] != t-1:
                ret = min(ret, height[y])
        return ret
    
    height = [-1] * len(G)
    bridges = []
    dfs(0, 0, G, height, bridges)
    return bridges


def delete_sequence(G):
    """
    Deletes a sequence of nodes in a graph using depth-first search (DFS).

    Parameters:
    - G (list): The adjacency list representation of the graph.

    Returns:
    - sequence (list): The sequence of nodes in the graph after deletion.

    """
    def dfs(x, G, visited, sequence):
        visited[x] = True
        for y in G[x]:
            if not visited[y]:
                dfs(y, G, visited, sequence)
        sequence.append(x)
    
    visited = [False] * len(G)
    sequence = []
    dfs(0, G, visited, sequence)
    return sequence

def nodi_di_articolazione(G: list[list[int]]) -> list[int]:
    """
    Finds and returns the articulation points in a given graph.

    Args:
        G (list[list[int]]): The adjacency list representation of the graph.

    Returns:
        list[int]: A list of articulation points in the graph.
    """
    def dfs(u, father, G, V, nodi, D, F, time):
        V[u] = True
        D[u] = time[0]
        time[0] += 1
        b = True
        for v in G[u]:
            if not V[v]:
                dfs(v, u, G, V, nodi, D, F, time)
            elif (v != father and D[v] < D[u]):
                b = False
        if b: nodi[father] = 1
        F[u] = time[0]
        time[0] += 1
    
    nodi = [0]*len(G)
    V = [0]*len(G)
    D = [0]*len(G)
    F = [0]*len(G)
    time = [0]
    
    dfs(0, 0, G, V, nodi, D, F, time)
    nodi_art = []
    for i in range(len(G)):
        if nodi[i] == 1:
            nodi_art.append(i)

    return nodi_art

def bfs_n2(x, G):
    """
    Perform breadth-first search starting from node x in the graph G.

    Args:
        x (int): The starting node.
        G (list): The adjacency list representation of the graph.

    Returns:
        list: A list of 0s and 1s indicating whether each node is visited or not.
    """
    visitati = [0]*len(G)
    visitati[x] = 1
    coda = [x]
    while coda:
        u = coda.pop(0)
        for y in G[u]:
            if visitati[y] == 0:
                visitati[y] = 1
                coda.append(y)
    return visitati

def bfs(x, G):
    """
    Perform breadth-first search starting from node x in the graph G.

    Parameters:
    - x: The starting node for the breadth-first search.
    - G: The graph represented as an adjacency list.

    Returns:
    - visitati: A list indicating which nodes have been visited during the breadth-first search.
                The value at index i is 1 if node i has been visited, and 0 otherwise.
    """
    visitati = [0]*len(G)
    visitati[x] = 1
    coda = [x]
    i = 0
    while len(coda) > i:
        u = coda[i]
        i += 1
        for y in G[u]:
            if visitati[y] == 0:
                visitati[y] = 1
                coda.append(y)
    return visitati

def bfs_parent(x, G):
    """
    Perform a breadth-first search starting from node x in the graph G and return the parent array.

    Args:
        x (int): The starting node.
        G (list): The adjacency list representation of the graph.

    Returns:
        list: The parent array where P[i] represents the parent of node i in the breadth-first search tree.

    """
    P = [-1]*len(G)
    P[x] = x
    coda = [x]
    i = 0
    while len(coda) > i:
        u = coda[i]
        i += 1
        for y in G[u]:
            if P[y] == -1:
                P[y] = u
                coda.append(y)
    return P

def bfs_distance(x, G):
    """
    Calculates the shortest distance from a given node 'x' to all other nodes in the graph 'G' using Breadth-First Search (BFS).

    Parameters:
    - x: The starting node.
    - G: The graph represented as an adjacency list.

    Returns:
    - D: A list of distances from the starting node to all other nodes. The distance is -1 if a node is unreachable from the starting node.
    """
    D = [-1]*len(G)
    D[x] = 0
    coda = [x]
    i = 0
    while len(coda) > i:
        u = coda[i]
        i += 1
        for y in G[u]:
            if D[y] == -1:
                D[y] = D[u]+1
                coda.append(y)
    return D


def dijkstra(s, G):
    """
    Applies Dijkstra's algorithm to find the shortest path from a source node to all other nodes in a graph.

    Parameters:
        s (int): The index of the source node.
        G (list): The adjacency list representation of the graph. Each element in the list is a tuple (y, costo),
                  where y is the index of a neighboring node and costo is the cost of the edge between the nodes.

    Returns:
        tuple: A tuple (D, P) where D is a list of shortest distances from the source node to each node in the graph,
               and P is a list of parent nodes that form the shortest path from the source node to each node.

    """
    inserito = [False]*len(G)
    from math import inf 
    lista = [(inf,-1)] * len(G)
    lista[s], inserito[s]  = (0,s), True
    for y, costo in G[s]:
        lista[y] = (costo, s)
    while True:
        minimo = inf
        for i in range(len(lista)):
            if not inserito[i] and lista[i][0] < minimo:
                minimo, x = lista[i][0], i
        if minimo == inf:
            break
        inserito[x] = True
        for y, costo in G[x]:
            if not inserito[y] and minimo + costo < lista[y][0]:
                lista[y] = (minimo+costo, x)
    D = [costo for costo, _ in lista]
    P = [padre for _, padre in lista]
    return D, P

def bfs_same_distance(u, v, G):
    """
    Returns a list of nodes in the graph `G` that have the same distance from nodes `u` and `v`.

    Parameters:
    - u: The starting node.
    - v: The target node.
    - G: The graph represented as an adjacency matrix.

    Returns:
    - S: A list of nodes that have the same distance from nodes `u` and `v`.
    """
    Du = bfs_distance(u, G)
    Dv = bfs_distance(v, G)

    S = []

    for i in range(len(G)):
        if Du[i] == Dv[i]:
            S.append(i)

    return S

def find_diameter_dfs(G):
    """
    Finds the diameter of a tree using depth-first search (DFS).

    Parameters:
    - G (list): The adjacency list representation of the tree.

    Returns:
    - int: The diameter of the tree.

    Algorithm:
    1. Initialize the maximum depth as 0.
    2. Initialize the visited array V with all elements set to 0.
    3. Call the helper function max_depth_dfs with the root node, G, V, maximum depth, current depth, and output array.
    4. Update the maximum depth and output array based on the result of the helper function.
    5. Reset the visited array V.
    6. Reset the maximum depth.
    7. Call the helper function max_depth_dfs with the node found in step 4, G, V, maximum depth, current depth, and output array.
    8. Return the maximum depth from the output array.

    Note:
    - This function assumes that the input graph is a tree.
    - The input graph G should be represented as an adjacency list.
    - The output is the diameter of the tree, which is the longest path between any two nodes in the tree.
    """
    def max_depth_dfs(u, G, V, max_depth, depth, output):
        V[u] = 1
        for x in G[u]:
            if V[x] == 0:
                max_depth_dfs(x, G, V, max_depth, depth+1, output)
        if depth > max_depth[0]:
            output[0] = u
            output[1] = depth
            max_depth[0] = depth
        return output
    
    max_depth = [0]
    V = [0] * len(G)
    output = [0,0]
    u = max_depth_dfs(0, G, V, max_depth, 0, output)[0]
    V = [0] * len(G)
    max_depth = [0]
    output = max_depth_dfs(u, G, V, max_depth, 0, output)
    return output[1]

def find_distance_of_two_subset(v_first, v_second, G):
    pass

def poisoned_nodes_dfs(u, G, P):
    """
    Finds the nodes in a graph that cannot be visited from a given starting node,
    considering that some nodes are poisoned.

    Parameters:
    u (int): The starting node.
    G (list): The adjacency list representation of the graph.
    P (list): The list indicating whether each node is poisoned (1) or not (0).

    Returns:
    list: The list of nodes that cannot be visited from the starting node.
    """

    def dfs(u, G, P, V):
        V[u] = True
        for v in G[u]:
            if not V[v] and P[v] != 1:
                dfs(v, G, P, V)

    V = [False]*len(G)
    dfs(u, G, P, V)

    not_visitable_nodes = []

    for i in range(len(G)):
        if V[i] == False and P[i] != 1:
            not_visitable_nodes.append(i)
    
    return not_visitable_nodes

def super_min_dijkstra(s, G):
    """
    Finds the shortest path distances and predecessors from a given source node to all other nodes in a graph.

    Args:
        s (int): The source node.
        G (list): The adjacency list representation of the graph.

    Returns:
        tuple: A tuple containing two lists:
            - D (list): The shortest path distances from the source node to all other nodes.
            - P (list): The predecessors of each node in the shortest path.

    Example:
        G = [[(1, 2), (2, 4)], [(2, 1), (3, 7)], [(3, 3)], [(4, 5)], []]
        D, P = super_min_dijkstra(0, G)
        print(D)  # Output: [0, 2, 4, 7, inf]
        print(P)  # Output: [None, 0, 0, 1, None]
    """
    inserito = [False]*len(G)
    from math import inf 
    lista = [(inf,-1)] * len(G)
    edges = [inf] * len(G)
    edges[s] = 0
    lista[s], inserito[s]  = (0,s), True
    for y, costo in G[s]:
        lista[y] = (costo, s)
        edges[y] = 1
    while True:
        minimo = inf
        min_edges = inf
        for i in range(len(lista)):
            if not inserito[i] and lista[i][0] < minimo:
                if edges[i] < min_edges:
                    minimo, x = lista[i][0], i
                    min_edges = edges[lista[y][1]] + 1
        if minimo == inf:
            break
        inserito[x] = True
        edges[x] = min_edges
        for y, costo in G[x]:
            if not inserito[y] and minimo + costo < lista[y][0]:
                lista[y] = (minimo+costo, x)
    D = [costo for costo, _ in lista]
    P = [padre for _, padre in lista]
    return D, P
