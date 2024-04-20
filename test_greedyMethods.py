from greedyMethods import *

def test_place_dumpsters():
    print("Running test cases for place_dumpsters...")
    # Test case 1: Simple list of houses
    L = [2,5,7,11,14,16,18]
    k = 3
    assert place_dumpsters(L, k) == [5, 14, 18]
    
    print("All test cases passed!")

test_place_dumpsters()

def test_select_a():
    print("Running test cases for select_a...")
    # Test case 1: Simple list of intervals
    lista = [(1,5),(14,21),(15,20),(2,9),(3,8),(6,13),(6,11),(18,22),(10,13),(12,17),(16,19)]
    assert select_a(lista) == [(1,5),(6,11),(12,17),(18,22)]
    
    print("All test cases passed!")

test_select_a()

def test_assegnazioneAule():
    print("Running test cases for assegnazioneAule...")
    # Test case 1: Simple list of intervals
    lista = [(1,4),(1,6),(7,8),(5,10)]
    assert assegnazioneAule(lista) == [[(1,4),(5,10)],[(1,6),(7,8)]]
    
    print("All test cases passed!")

test_assegnazioneAule()

def test_file():
    print("Running test cases for file...")
    # Test case 1: Simple list of intervals
    lista = [5,6,3,5,4,7,3]
    assert file(lista,11) == [2,6,4]
    
    print("All test cases passed!")

test_file()

def test_scelta():
    print("Running test cases for scelta...")
    # Test case 1: Simple list of intervals
    A = [10,2,4,6,1,7,3,4]
    B = [6,6,1,0,3,8,5,7]
    assert scelta(A,B) == 48
    
    print("All test cases passed!")

test_scelta()

def test_sottoinsieme_indipendente():
    print("Running test cases for sottoinsieme_indipendente...")
    # Test case 1: Simple graph with 10 nodes
    G = [[4],[2],[1,4,8],[5],[0,2,9],[3,6,7,8],[5],[5],[2,5],[4]]
    assert sottoinsieme_indipendente(G) == [0, 1, 3, 6, 7, 8, 9]
    
    print("All test cases passed!")

test_sottoinsieme_indipendente()

def test_swap():
    print("Running test cases for swap...")
    # Test case 1: Simple lists of elements
    A = [2,4,5,6,7]
    B = [3,4,2,1,3]
    k = 3
    assert swap(A,B,k) == 22
    
    print("All test cases passed!")

test_swap()