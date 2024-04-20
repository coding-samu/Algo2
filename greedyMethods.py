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

def sottoinsieme_indipendente(G):
    """
    Finds the maximum independent set in a given graph using Depth-First Search (DFS).

    Parameters:
    G (list): The adjacency list representation of the graph.

    Returns:
    list: The list of vertices in the maximum independent set.

    """
    def dfs_visit(u,G):
        visited[u] = 0
        for v in G[u]:
            if visited[v] == -1:
                dfs_visit(v,G)
                if visited[v] == 2: visited[u] = 1
        if visited[u] == 0: visited[u] = 2
    visited = [-1]*len(G)
    dfs_visit(0,G)
    return [u for u in range(len(G)) if visited[u] == 2]


def swap(A,B,k):
    """
    Swaps elements between two lists to maximize the sum of the elements in one of the lists.

    The function takes two lists, A and B, and an integer k as input. It then calculates the
    difference between each element of A and B, sorts the differences in descending order, and
    swaps the first k elements of A with the first k elements of B. Finally, it returns the sum
    of the elements in A.

    Args:
        A (list): The first list of elements.
        B (list): The second list of elements.
        k (int): The number of elements to swap between the two lists.

    Returns:
        int: The sum of the elements in list A after swapping.

    """
    n = len(A)
    lista = [(A[i]-B[i],i) for i in range(n)]
    lista.sort()
    for i in range(k):
        A[lista[i][1]], B[lista[i][1]] = B[lista[i][1]], A[lista[i][1]]
    return sum(A)


def fai_benzina(l,A,a,b):
    """
    Finds the minimum number of gas stations to reach the destination.

    The function takes a list of gas stations along a route and a maximum distance that can be
    traveled with a full tank as input. It then iterates over the gas stations and places a
    gas station at the farthest reachable point from the current gas station. Finally, it returns
    the list of gas stations placed along the route.

    Args:
        l (int): kilometers that can be traveled with a full tank.
        A (list): A list of integers representing the locations of gas stations along the route.
        a (int): The starting point of the route.
        b (int): The destination point of the route.

    Returns:
        list: A list of integers representing the locations of the placed gas stations.

    """
    def ric(c,d):
        if c >= d:
            return
        par = c
        arr = d
        # Trovo la più distante tra le stazioni che posso raggiungere da c
        j = 0
        for i in range(len(A)):
            if A[i] <= c + l:
                par = A[i]
                j = i
            else:
                break
        fermate[j] = 1

        # Trovo la più distante tra le stazioni da cui posso raggiungere d
        j = 0
        for i in range(len(A)-1,-1,-1):
            if A[i] >= d - l:
                arr = A[i]
                j = i
            else:
                break
        fermate[j] = 1

        ric(par,arr)

    fermate = [0]*len(A)
    ric(a,b)
    return sorted([A[i] for i in range(len(A)) if fermate[i] == 1])
