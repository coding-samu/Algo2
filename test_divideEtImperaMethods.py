from divideEtImperaMethods import *

def test_pow():
    print("Running test cases for pow...")

    # Test case 1: Simple values
    a = 2
    n = 3
    assert pow(a,n) == 8
    
    # Test case 2: Simple values
    a = 3
    n = 4
    assert pow(a,n) == 81
    
    print("All test cases passed!")

test_pow()

def test_maximum_sum_of_sublist():
    print("Running test cases for maximum_sum_of_sublist...")

    # Test case 1: Simple list of elements
    A = [3,-5,6,-5,8,-3,-4,5]
    assert maximum_sum_of_sublist(A,0,len(A)-1) == (9,5,7,7)

    # Test case 2: Simple list of elements
    A = [2,0,-2,1,-3,1,0,4,-2,3,-1,2,-2,-2,-5,1]
    assert maximum_sum_of_sublist(A,0,len(A)-1) == (7,-3,5,1)
    
    print("All test cases passed!")

test_maximum_sum_of_sublist()