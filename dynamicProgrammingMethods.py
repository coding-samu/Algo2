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


def piastrellamento_di_tipo_A(n):
    T = [0]*(n+1)
    T[1], T[2] = 1, 2
    for i in range(3,n+1):
        T[i] = T[i-1] + T[i-2]
    return T[n]

def piastrellamento_di_tipo_B(n):
    T = [0]*(n+1)
    if n < 4: return 0
    T[4] = 2
    for i in range(5,n+1):
        T[i] = T[i-1]*2
    return T[n]

def piastrellamento_di_due_tipi(n):
    T = [0]*(n+1)
    if n == 0: return 0
    if n == 1: return 1
    if n == 2: return 2
    T[1], T[2] = 1, 2
    for i in range(3,n+1):
        T[i] = 2*T[i-1]

    if n >= 4:
        return piastrellamento_di_tipo_A(n) + piastrellamento_di_tipo_B(n) + 2*T[n-1] + 4*(T[n-4])
    else:
        return piastrellamento_di_tipo_A(n) + piastrellamento_di_tipo_B(n) + 2*T[n-1]