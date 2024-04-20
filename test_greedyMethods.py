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