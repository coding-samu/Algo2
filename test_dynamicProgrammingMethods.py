from dynamicProgrammingMethods import *

def test_fib():
    print("Running test cases for fib...")

    # Test case 1: Simple values
    n = 7
    assert fib(n) == 13
    
    # Test case 2: Simple values
    n = 17
    assert fib(n) ==  1597
    
    print("All test cases passed!")

test_fib()