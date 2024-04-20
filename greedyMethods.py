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