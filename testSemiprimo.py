from math import sqrt

# Test in tempo O(sqrt(n))per verificare se un numero è semiprimo
def semiprimo(n):
    """
    Determines whether a number is a semiprime.

    A semiprime is a number that is the product of two prime numbers.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is a semiprime, False otherwise.
    """
    # Calculate the upper limit for the loop
    bound = int(sqrt(n))
    count = 0
    for i in range(2, bound):
        if n % i == 0:
            count += 1
    return count == 1