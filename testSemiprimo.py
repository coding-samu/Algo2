from math import sqrt

# Test in tempo O(sqrt(n))per verificare se un numero è semiprimo
def semiprimo(n):
    # Calcola il limite superiore per il ciclo
    bound = int(sqrt(n))
    temp = 0
    for i in range(2, bound):
        if n % i == 0:
            temp = n // i