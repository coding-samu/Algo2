def fib(n):
    if n <= 1:
        return n
    a = b = 1
    for i in range(2,n):
        a,b = b,a+b
    return b

def riempiDisco(A,C):
    n = len(A)
    T = [[0]*(C+1) for i in range(n+1)]
    for i in range(1,n+1):
        for c in range(C+1):
            if c < A[i-1]:
                T[i][c] = T[i-1][c]
            else:
                T[i][c] = max(T[i-1][c],T[i-1][c-A[i-1]]+A[i-1])
    
    valore = T[n][C]
    sol = set()
    i = n
    while i > 0:
        if T[i][valore] != T[i-1][valore]:
            sol.add(i-1)
            valore -= A[i-1]
        i -= 1
    return T[n][C],sol


def sequence_without_3_consecutive_zeros(n):
    T = [0]*(n+1)
    if n <= 1:
        return n+1
    T[0] = 1
    T[1] = 2
    T[2] = 4
    for i in range (3,n+1):
        T[i] = T[i-1] + T[i-2] + T[i-3]
    return T[n]


def count_combos_for_room_from_one_to_three_beds_for_n_people(n):
    T = [0 for _ in range(n+1)]
    T[0] = 0
    T[1] = 1
    T[2] = 2
    for i in range(3,n+1):
        T[i] = T[i-1] + (i-1)*T[i-2] + int(((i-1)*T[i-2])//2)
    return T[n]


def max_sum_distance_two(A):
    n = len(A)
    T = [0 for _ in range(n+1)]
    T[0] = A[0]
    T[1] = max(A[0],A[1])
    for i in range(2,n):
        T[i] = max(T[i-1],T[i-3]+A[i])
    return T[n-1]


def tiling_one_type(n):
    T = [0]*(n+1)
    T[1], T[2] = 1, 2
    for i in range(3,n+1):
        T[i] = T[i-1] + T[i-2]
    return T[n]

def tiling_two_types(n):
    T = [0]*(n+1)
    T[0], T[1], T[2], T[3] = 1, 1, 2, 7
    for i in range(4,n+1):
        T[i] = T[i-1] + T[i-2] + 4*T[i-3] + 2*T[i-4]
    return T[n]


def  cardsGameTree(L):
    def rec(L,parz,player,n):
        if n == 1: 
            parz[player] += L[0]
            return parz
        parzS = [parz[0],parz[1]]
        parzD = [parz[0],parz[1]]
        parzS[player] += L[0]
        parzD[player] += L[-1]
        S = rec(L[1:],parzS,1-player,n-1)
        D = rec(L[:-1],parzD,1-player,n-1)
        return S,D


    n = len(L)-1
    S = rec(L[1:],[L[0],0],1,n)
    D = rec(L[:-1],[L[-1],0],1,n)
    return S,D

def riempiDisco2(A,c):
    n = len(A)
    T = [[0]*(c+1) for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(c+1):
            if j < A[i-1]:
                T[i][j] = T[i-1][j]
            else:
                T[i][j] = max(T[i-1][j],T[i-1][j-A[i-1]]+A[i-1])
            stampaMatrice(T)
            print()
    return T[n][c]

def componiStringa(I,s):
    T = [0 for _ in range(len(s))]
    if s[0] in I:
        T[0] = 1
    for i in range(1,len(s)):
        if s[i] in I:
            T[i] += T[i-1]
        if s[i-1:i+1] in I:
            if i == 1:
                T[i] += 1
            else:
                T[i] += T[i-2]
    return T

def stampaMatrice(M):
    for i in range(len(M)):
        print(M[i])