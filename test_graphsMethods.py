from graphsMethods import *

def test_DFSList():
    print("Running test cases for DFSList...")
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
def test_super_min_dijkstra():
    print("Running test cases for super_min_dijkstra...")
    # Test case 1: Simple graph with 5 nodes
    G = [[(1,2),(4,5)],[(0,2),(2,3)],[(1,3),(3,3)],[(2,3),(4,3)],[(3,3),(0,5)]]
    assert super_min_dijkstra(0, G) == ([0, 2, 5, 8, 5], [0, 0, 1, 4, 0])

    print("All test cases passed!")

test_super_min_dijkstra()

### Test cases for super min dijkstra ###
def test_super_min_dijkstra_by_modified_weight():
    print("Running test cases for super_min_dijkstra_by_modified_weight...")
    # Test case 1: Simple graph with 5 nodes
    G = [[(1,2),(4,5)],[(0,2),(2,3)],[(1,3),(3,3)],[(2,3),(4,3)],[(3,3),(0,5)]]
    assert super_min_dijkstra_by_modified_weight(0, G) == ([0, 2, 5, 8, 5], [0, 0, 1, 4, 0])

    print("All test cases passed!")

test_super_min_dijkstra_by_modified_weight()

### Test case for posioned nodes dfs ###
def test_poisoned_nodes_dfs():
    print("Running test cases for poisoned_nodes_dfs...")
    # Test case 1: Simple graph with 3 nodes
    G = [[1],[2],[]]
    P = [0,1,0]
    assert poisoned_nodes_dfs(0, G, P) == [2]

    # Test case 2: Disconnected graph with 5 nodes
    G = [[1],[0],[3],[2],[]]
    P = [0,1,0,1,0]
    assert poisoned_nodes_dfs(0, G, P) == [2,4]

    # Test case 3: Graph with a cycle
    G = [[1,2],[0,2],[0,1]]
    P = [0,1,0]
    assert poisoned_nodes_dfs(0, G, P) == []

    print("All test cases passed!")

test_poisoned_nodes_dfs()

### Test case for find diameter dfs ###
def test_find_diameter_dfs():
    print("Running test cases for find_diameter_dfs...")
    # Test case 1: Simple graph with 5 nodes
    G = [[1,4],[0,2,3],[1],[1],[0]]
    assert find_diameter_dfs(G) == 3

    print("All test cases passed!")

test_find_diameter_dfs()

### Test case for bfs same distance ###
def test_bfs_same_distance():
    print("Running test cases for bfs_same_distance...")
    # Test case 1: Simple graph with 7 nodes
    G = [[1,5],[2],[3],[4],[],[2,4],[2]]
    assert bfs_same_distance(6, 5, G) == [0, 1, 2, 3]

    print("All test cases passed!")

test_bfs_same_distance()

### Test case for nodi di articolazione ###
def test_nodi_di_articolazione():
    print("Running test cases for nodi_di_articolazione...")
    # Test case 1: Simple graph with 9 nodes
    G = [[3,4,5,8],[2,7],[1,6,7],[0,4,7],[0,3],[0,8],[2],[1,2,3],[0,5]]
    assert nodi_di_articolazione(G) == [0, 2, 3, 7]

    print("All test cases passed!")

test_nodi_di_articolazione()

### Test case for delete sequence ###
def test_delete_sequence():
    print("Running test cases for delete_sequence...")
    # Test case 1: Simple graph with 9 nodes
    G = [[3,4,5,8],[2,7],[1,6,7],[0,4,7],[0,3],[0,8],[2],[1,2,3],[0,5]]
    assert delete_sequence(G) == [4, 6, 2, 1, 7, 3, 8, 5, 0]

    print("All test cases passed!")

test_delete_sequence()

### Test case for find bridges ###
def test_find_bridges():
    print("Running test cases for find_bridges...")
    # Test case 1: Simple graph with 9 nodes
    G = [[3,4,5,8],[2,7],[1,6,7],[0,4,7],[0,3],[0,8],[2],[1,2,3],[0,5]]
    assert find_bridges(G) == [(2, 6), (3, 7)]

    print("All test cases passed!")

test_find_bridges()

### Test case for find path all ###
def test_find_path_all():
    print("Running test cases for find_path_all...")
    # Test case 1: Simple graph with 5 nodes
    G = [[1,3,4],[0,2],[1,3,4],[0,2,4],[0,3,2]]
    assert find_path_all(0, G) == [0, 1, 2, 3, 4, 3, 2, 4, 2, 1, 0, 3, 0, 4, 0]

    print("All test cases passed!")

test_find_path_all()

### Test case for count edges ###
def test_count_edges():
    print("Running test cases for count_edges...")
    # Test case 1: Simple graph with 7 nodes
    G = [[1,2],[3],[3],[4,5],[5],[6],[1]]
    assert count_edges(G) == (1, 1, 1)

    print("All test cases passed!")

test_count_edges()

### Test case for ordinamento topologico dfs ###
def test_ordinamento_topologico_dfs():
    print("Running test cases for ordinamento_topologico_dfs...")
    # Test case 1: Simple graph with 7 nodes
    G = [[1,4,5],[2],[3],[4],[],[2],[2]]
    assert ordinamento_topologico_dfs(G) == [6, 0, 5, 1, 2, 3, 4]

    print("All test cases passed!")

### Test case for generate complete graph ###
def test_generate_complete_graph():
    print("Running test cases for generate_complete_graph...")
    # Test case 1: Simple graph with 4 nodes
    G = generate_complete_graph(4)
    assert G == [[1, 2, 3], [0, 2, 3], [0, 1, 3], [0, 1, 2]]

    print("All test cases passed!")

test_generate_complete_graph()

### Test case for orienta grafo completo ###
def test_orienta_grafo_completo():
    print("Running test cases for orienta_grafo_completo...")
    # Test case 1: Simple graph with 4 nodes
    G = orienta_grafo_completo([[1, 2, 3], [0, 2, 3], [0, 1, 3], [0, 1, 2]])
    assert G == [[1, 2, 3], [2, 3], [3], []]

    print("All test cases passed!")

test_orienta_grafo_completo()

### Test case for orient all ###
def test_orient_all():
    print("Running test cases for orient_all...")
    # Test case 1: Simple graph with 6 nodes
    G = [[1],[3],[1,4],[4],[2,3],[4]]
    assert orient_all(0, G, [0]*6) == [[1], [3], [1, 4], [], [3], [4]]

    print("All test cases passed!")

test_orient_all()

### Test case for conta pozzi da nodo ###
def test_conta_pozzi_da_nodo():
    print("Running test cases for conta_pozzi_da_nodo...")
    # Test case 1: Simple graph with 11 nodes
    G = [[2,9],[0,2,5,7],[],[4,6],[10],[],[9],[8],[],[10],[3]]
    assert conta_pozzi_da_nodo(1, G, [0]*11) == 3

    print("All test cases passed!")

test_conta_pozzi_da_nodo()

### Test case for sort Topologico ### 
def test_sortTopologico():
    print("Running test cases for sortTopologico...")
    # Test case 1: Simple graph with 7 nodes
    G = [[1,5,6],[2,6],[],[2,4,6],[5,6],[],[2,5]]
    assert sortTopologico(G) == [3, 4, 0, 1, 6, 5, 2]

    print("All test cases passed!")

test_sortTopologico()

### Test case for find distance of two subset ###
def test_find_distance_of_two_subset():
    print("Running test cases for find_distance_of_two_subset...")
    # Test case 1: Simple graph with 5 nodes
    G = [[1,2,4],[0,3],[0,3,4],[1,2,4],[0,2,3]]
    assert find_distance_of_two_subset([0],[4], G) == 1

    # Test case 2: Simple graph with 5 nodes
    G = [[1,2,4],[0,3],[0,3,4],[1,2,4],[0,2,3]]
    assert find_distance_of_two_subset([0],[0], G) == 0

    # Test case 3: Simple graph with 5 nodes
    G = [[1,2,4],[0,3],[0,3,4],[1,2,4],[0,2,3]]
    assert find_distance_of_two_subset([1],[4], G) == 2

    print("All test cases passed!")

test_find_distance_of_two_subset()

print(grafo_quadrato([[1],[2],[3],[4],[5],[0]])) # [[1, 2], [2, 3], [3, 4], [4, 5], [5, 0], [0, 1]]

print(grafo_quadrato(grafo_quadrato([[1],[2],[3],[4],[5],[0]])))