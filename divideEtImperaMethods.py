from random import randint
from math import ceil

def selezione2(A,k):
    '''Restituisce l'elemento di rango k dove 1 <= k <= len(A)'''
    if len(A) == 1:
        return A[0]
    perno = A[0]
    A1, A2 = [], []
    for x in A:
        if x < perno:
            A1.append(x)
        elif x > perno:
            A2.append(x)
    if len(A1) >= k:
        return selezione2(A1,k)
    elif len(A1) == k-1:
        return perno
    else:
        return selezione2(A2,k-len(A1)-1)
    
def selezione2R(A,k):
    '''Restituisce l'elemento di rango k dove 1 <= k <= len(A)'''
    if len(A) == 1:
        return A[0]
    perno = A[randint(0,len(A)-1)]
    A1, A2 = [], []
    for x in A:
        if x < perno:
            A1.append(x)
        elif x > perno:
            A2.append(x)
    if len(A1) >= k:
        return selezione2R(A1,k)
    elif len(A1) == k-1:
        return perno
    else:
        return selezione2R(A2,k-len(A1)-1)
    
def selezione(A,k):
    ''' Restituisce l'elemento di rango k dove 1 <= k <= len(A) 
        scegliendo ogni volta il perno con la regola del mediano dei mediani
    '''
    if len(A) <= 120:
        A.sort()
        return A[k-1]
    B = [sorted(A[5*i : 5*i+5])[2] for i in range(len(A)//5)]
    perno = selezione(B,ceil(len(A)/10))
    A1, A2 = [], []
    for x in A:
        if x < perno:
            A1.append(x)
        elif x > perno:
            A2.append(x)
    if len(A1) >= k:
        return selezione(A1,k)
    elif len(A1) == k-1:
        return perno
    else:
        return selezione(A2,k-len(A1)-1)
    
def pow(a,n):
    if n == 0:
        return 1
    x = pow(a,n//2)
    if n % 2:
        return x*x*a
    return x*x