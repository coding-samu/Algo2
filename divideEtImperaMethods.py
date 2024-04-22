from random import randint

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