def generate_complete_graph(n: int) -> list[list[int]]:
    G: list[list[int]] = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                G[i].append(j)
    return G