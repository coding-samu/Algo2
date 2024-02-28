

def count_triplets_with_sum_k(arr, k):
    """
    Conta le triple di elementi nella lista 'arr' che hanno come somma 'k'.
    Restituisce il numero totale di triple.
    """
    arr.sort()  # Ordina la lista in modo crescente
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
