from heapq import heappush, heappop

def place_dumpsters(L, k):
    """
    Place dumpsters along a street based on the given house locations and a maximum distance between dumpsters.

    Args:
        L (list): A list of integers representing the locations of houses along the street.
        k (int): The maximum distance between dumpsters.

    Returns:
        list: A list of integers representing the locations of the placed dumpsters.
    """
    dumpsters = []
    dump_count = 0
    street = L[-1]

    for house in L:
        if dump_count == 0:
            if house + k > street:
                p = street
            else:
                p = house + k
            dumpsters.append(p)
            dump_count += 1
        else:
            if house > dumpsters[-1] + k:
                if house + k > street:
                    p = street
                else:
                    p = house + k
                dumpsters.append(p)
                dump_count += 1
    return dumpsters


def select_a(lista):
    """
    Selects a subset of intervals from the given list based on the greedy method.

    Args:
        lista (list): A list of intervals represented as tuples (inizio, fine).

    Returns:
        list: A subset of intervals from the given list that satisfies the greedy condition.
    """
    lista.sort(key=lambda x: x[1])
    libero = 0
    sol = []
    for inizio, fine in lista:
        if libero < inizio:
            sol.append((inizio, fine))
            libero = fine
    return sol


def assegnazioneAule(lista):
    """
    Assigns classrooms to a list of time intervals.

    Args:
        lista (list): A list of tuples representing time intervals. Each tuple contains two elements: the start time and the end time.

    Returns:
        list: A list of lists representing the assigned time intervals for each classroom. Each inner list contains tuples representing time intervals assigned to a specific classroom.

    """
    sol = [[]]
    H = [(0,0)]
    lista.sort()
    for inizio,fine in lista:
        libera, aula = H[0]
        if libera < inizio:
            sol[aula].append((inizio,fine))
            heappop(H)
            heappush(H,(fine,aula))
        else:
            sol.append([(inizio,fine)])
            heappush(H,(fine,len(sol)-1))
    return sol


def file(D, k):
    """
    Selects files from a list based on their sizes, until the total size of selected files is less than or equal to a given limit.

    Args:
        D (list): A list of file sizes.
        k (int): The maximum total size of selected files.

    Returns:
        list: A list of indices of the selected files.

    """
    n = len(D)
    lista = [(D[i], i) for i in range(n)]
    lista.sort()
    spazio, sol = 0, []
    for d, i in lista:
        if spazio + d <= k:
            sol.append(i)
            spazio += d
        else:
            return sol
        

def scelta(A, B):
    """
    Calculates the sum of elements from two lists based on a greedy method.

    The function takes two lists, A and B, of equal length as input. It calculates the difference
    between each element of A and B, sorts the differences in descending order, and then selects
    the first half of the sorted list from A and the second half from B. Finally, it returns the
    sum of the selected elements.

    Args:
        A (list): The first list of elements.
        B (list): The second list of elements.

    Returns:
        int: The sum of the selected elements.

    """
    n = len(A)
    lista = [(A[i]-B[i],i) for i in range(n)]
    lista.sort(reverse=True)
    sol = 0
    for i in range(n//2):
        sol += A[lista[i][1]]
    for i in range(n//2,n):
        sol += B[lista[i][1]]
    return sol