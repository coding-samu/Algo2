def fib(n):
    if n <= 1:
        return n
    a = b = 1
    for i in range(2,n):
        a,b = b,a+b
    return b

def esI(A,C):
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