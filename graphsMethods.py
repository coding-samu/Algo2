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

#print(subtree([2,3,2,4,2,3,4,0],4))

def ordinamento_topologico(G: list[list[int]]) -> list[list[int]]:
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
    Du = bfs_distance(u, G)
    Dv = bfs_distance(v, G)

    S = []

    for i in range(len(G)):
        if Du[i] == Dv[i]:
            S.append(i)

    return S

def find_diameter_dfs(G): # on trees
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

### Test case for posioned nodes dfs ###
#G = [[1],[2],[]]
#P = [0,1,0]
#print(poisoned_nodes_dfs(0, G, P))

### Test case for find diameter dfs ###
#G = [[1,4],[0,2,3],[1],[1],[0]]
#print(find_diameter_dfs(G))

### Test case for bfs same distance ###
#G = [[1,5],[2],[3],[4],[],[2,4],[2]]
#print(bfs_same_distance(6, 5, G))

### Test case for nodi di articolazione ###
#G = [[3,4,5,8],[2,7],[1,6,7],[0,4,7],[0,3],[0,8],[2],[1,2,3],[0,5]]
#print(nodi_di_articolazione(G))

### Test case for delete sequence ###
#G = [[3,4,5,8],[2,7],[1,6,7],[0,4,7],[0,3],[0,8],[2],[1,2,3],[0,5]]
#print(delete_sequence(G))

### Test case for find bridges ###
#G = [[3,4,5,8],[2,7],[1,6,7],[0,4,7],[0,3],[0,8],[2],[1,2,3],[0,5]]
#print(find_bridges(G))

### Test case for find path all ###
#G = [[1,3,4],[0,2],[1,3,4],[0,2,4],[0,3,2]]
#print(find_path_all(0, G))

### Test case for count edges ###
#G = [[1,2],[3],[3],[4,5],[5],[6],[1]]
#print(count_edges(G))  # Output: (1, 1, 1)

### Test case for ordinamento topologico dfs ###
#print(ordinamento_topologico_dfs([[1,4,5],[2],[3],[4],[],[2],[2]]))

### Test case for generate complete graph ###
#G = generate_complete_graph(4)
#print(G)

### Test case for orienta grafo completo ###
#G = orienta_grafo_completo(G)
#print(G)

### Test case for orient all ###
#G = [[1],[3],[1,4],[4],[2,3],[4]]
#print(orient_all(0, G, [0]*6))

### Test case for conta pozzi da nodo ###
#G = [[2,9],[0,2,5,7],[],[4,6],[10],[],[9],[8],[],[10],[3]]
#print(conta_pozzi_da_nodo(1, G, [0]*11))

### Test case for sort Topologico ### 
#G = [[1,5,6],[2,6],[],[2,4,6],[5,6],[],[2,5]]
#print(sortTopologico(G))