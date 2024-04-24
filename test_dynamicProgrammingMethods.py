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

def test_riempiDisco():
    print("Running test cases for riempiDisco...")

    # Test case 1: Simple values
    A = [80,15,40,95,30,50,40,30]
    C = 85
    assert riempiDisco(A,C) == (85,{1,2,4})
    
    print("All test cases passed!")

test_riempiDisco()

def test_sequence_without_3_consecutive_zeros():
    print("Running test cases for sequence_without_3_consecutive_zeros...")

    # Test case 1: Simple values
    n = 3
    assert sequence_without_3_consecutive_zeros(n) == 7
    
    # Test case 2: Simple values
    n = 4
    assert sequence_without_3_consecutive_zeros(n) == 13
    
    print("All test cases passed!")

test_sequence_without_3_consecutive_zeros()

def test_count_combos_for_room_from_one_to_three_beds_for_n_people():
    print("Running test cases for count_combos_for_room_from_one_to_three_beds_for_n_people...")

    # Test case 1: Simple values
    n = 3
    assert count_combos_for_room_from_one_to_three_beds_for_n_people(n) == 5
    
    # Test case 2: Simple values
    n = 4
    assert count_combos_for_room_from_one_to_three_beds_for_n_people(n) == 14
    
    print("All test cases passed!")

test_count_combos_for_room_from_one_to_three_beds_for_n_people()

def test_max_sum_distance_two():
    print("Running test cases for max_sum_distance_two...")

    # Test case 1: Simple list of elements
    A = [1,10,3,2,4,1,7]
    assert max_sum_distance_two(A) == 17
    
    # Test case 2: Simple list of elements
    A = [5,4,10,6,8]
    assert max_sum_distance_two(A) == 13
    
    print("All test cases passed!")

test_max_sum_distance_two()