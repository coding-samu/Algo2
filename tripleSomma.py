

def count_triplets_with_sum_k(arr, k):
    """
    Counts the number of triplets in a given list that sum up to a given value.

    Args:
        arr (list): The input list of integers.
        k (int): The target sum.

    Returns:
        tuple: A tuple containing the count of triplets and a list of tuples representing the triplets.

    Example:
        >>> count_triplets_with_sum_k([1, 2, 3, 4, 5], 6)
        (1, [(1, 2, 3)])
    """
    arr.sort()  # Sort the list in ascending order
    n = len(arr)
    count = 0
    tupleList = []

    for i in range(n - 2):
        left, right = i + 1, n - 1

        while left < right:
            curr_sum = arr[i] + arr[left] + arr[right]

            if curr_sum == k:
                count += 1
                tupleList += [(arr[i], arr[left], arr[right])]
                left += 1
                right -= 1
            elif curr_sum < k:
                left += 1
            else:
                right -= 1

    return count, tupleList


# Esempio di utilizzo
lista_di_interi = [1, 4, 2, 3, 5, 6]
valore_k = 10
risultato, tupleList = count_triplets_with_sum_k(lista_di_interi, valore_k)
print(f"Il numero di triple con somma {valore_k} è: {risultato}")
print(f"Le triple sono: {tupleList}")
