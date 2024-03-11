from graphsMethods import DFSList

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