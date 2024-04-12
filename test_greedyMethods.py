from greedyMethods import *

def test_place_dumpsters():
    print("Running test cases for place_dumpsters...")
    # Test case 1: Simple list of houses
    L = [2,5,7,11,14,16,18]
    k = 3
    assert place_dumpsters(L, k) == [5, 14, 18]
    
    print("All test cases passed!")

test_place_dumpsters()