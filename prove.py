def count_edges(G):
    n = len(G)
    visited = [False] * n
    finish = [False] * n
    parent = [None] * n
    forward = backward = cross = 0
    
    def dfs(v):
        nonlocal forward, backward, cross
        visited[v] = True
        for u in G[v]:
            if not visited[u]:
                parent[u] = v
                dfs(u)
            elif parent[v] != u:
                if parent[u] is None or parent[u] != v:
                    if not finish[u]:
                        backward += 1
                        print(f"backward: {v}-{u}")
                    else:
                        e = u
                        while parent[e] != v and parent[e] != 0:
                            e = parent[e]
                        if parent[e] == 0:
                            cross += 1
                            print(f"cross: {v}-{u}")
                        else:
                            forward += 1
                            print(f"forward: {v}-{u}")                
        finish[v] = True
    dfs(0)
    return forward, backward, cross

G = [[1,2],[3],[3],[4,5],[5],[6],[1]]
print(count_edges(G))  # Output: (1, 1, 1)