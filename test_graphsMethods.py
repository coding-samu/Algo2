from graphsMethods import *

def test_DFSList():
    # Test case 1: Simple graph with 3 vertices
    G = [[1, 2], [0, 2], [0, 1]]
    assert DFSList(0, G) == [True, True, True]
    assert DFSList(1, G) == [True, True, True]
    assert DFSList(2, G) == [True, True, True]

    # Test case 2: Disconnected graph with 4 vertices
    G = [[1], [0], [3], [2]]
    assert DFSList(0, G) == [True, True, False, False]
    assert DFSList(1, G) == [True, True, False, False]
    assert DFSList(2, G) == [False, False, True, True]
    assert DFSList(3, G) == [False, False, True, True]

    # Test case 3: Graph with a cycle
    G = [[1, 2], [0, 2], [0, 1]]
    assert DFSList(0, G) == [True, True, True]
    assert DFSList(1, G) == [True, True, True]
    assert DFSList(2, G) == [True, True, True]

    print("All test cases passed!")

test_DFSList()

### Test cases for super min dijkstra ###
G = [[(1,2),(4,5)],[(0,2),(2,3)],[(1,3),(3,3)],[(2,3),(4,3)],[(3,3),(0,5)]]
print(super_min_dijkstra(0,G))



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