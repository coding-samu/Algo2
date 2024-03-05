def generate_complete_graph(n: int) -> list[list[int]]:
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
    n = len(G)  # Numero di nodi
    archi_orientati = [[] for _ in range(len(G))]  # Lista per memorizzare gli archi orientati

    # Iteriamo su tutte le coppie di nodi distinti
    for u in range(n):
        for v in range(u + 1, n):
            # Orientiamo l'arco u → v se u è adiacente a v
            if v in G[u]:
                archi_orientati[u].append(v)
            # Altrimenti, orientiamo l'arco v → u
            else:
                archi_orientati[v].append(u)

    return archi_orientati


# Esempio
G = generate_complete_graph(5)
print(G)
G = orienta_grafo_completo(G)
print(G)