def es(A,k):
    nodo = 0
    countSolutions = 0
    def esR(A,k,n,sol,i=0,sum=0):
        nonlocal nodo
        nonlocal countSolutions
        nodo += 1
        if sum == k:
            print(sol)
            countSolutions += 1
            return
        if i == n:
            return
        if sum + A[i] <= k:
            sol.append(A[i])
            esR(A,k,n,sol,i+1,sum+A[i])
            sol.pop()
        esR(A,k,n,sol,i+1,sum)
    
    esR(A,k,len(A),[],0,0)
    print(countSolutions)
    print(nodo)

def esModificato(A,k):
    nodo = 0
    countSolutions = 0
    def esR(A,k,n,sol,i=0,sum=0):
        nonlocal nodo
        nonlocal countSolutions
        nodo += 1
        if sum == k:
            print(sol)
            countSolutions += 1
            return True
        if i == n:
            return False 
        if sum + A[i] <= k:
            sol.append(A[i])
            if esR(A,k,n,sol,i+1,sum+A[i]): return True
            sol.pop()
        if esR(A,k,n,sol,i+1,sum): return True
        return False
    
    esR(A,k,len(A),[],0,0)
    print(countSolutions)
    print(nodo)

#A = [61,20,1,33,20,2,4,1,1,33]
#k = 70
#es(A,k)
#esModificato(A,k)

def percorsiMatrice(M):
    n = len(M)

    def esplora(M,i,j,sol):
        # Se sono arrivato all'ultima riga, stampo sol
        if i == n-1:
            print(sol)
            return
        # Altrimenti:
        else:
            # Vado giù
            sol.append(M[i+1][j])
            esplora(M,i+1,j,sol)
            sol.pop()
            # Vado giù a sinistra
            if j > 0:
                sol.append(M[i+1][j-1])
                esplora(M,i+1,j-1,sol)
                sol.pop()
            # Vado giù a destra
            if j < n-1:
                sol.append(M[i+1][j+1])
                esplora(M,i+1,j+1,sol)
                sol.pop()

    for j in range(n):
        sol = []
        sol.append(M[0][j])
        esplora(M,0,j,sol)
        sol.pop()

def numeroTelefonico(n):
    T = [[0 for _ in range(10)] for _ in range(n+1)]

    for i in range(n+1):
        for j in range(10):
            if i == 0:
                T[i][j] = 0
            elif i == 1:
                T[i][j] = 1
            elif j == 0:
                T[i][j] = T[i-1][8]
            elif j == 1:
                T[i][j] = T[i-1][2] + T[i-1][4]
            elif j == 2:
                T[i][j] = T[i-1][1] + T[i-1][3] + T[i-1][5]
            elif j == 3:
                T[i][j] = T[i-1][2] + T[i-1][6]
            elif j == 4:
                T[i][j] = T[i-1][1] + T[i-1][5] + T[i-1][7]
            elif j == 5:
                T[i][j] = T[i-1][2] + T[i-1][4] + T[i-1][6] + T[i-1][8]
            elif j == 6:
                T[i][j] = T[i-1][3] + T[i-1][5] + T[i-1][9]
            elif j == 7:
                T[i][j] = T[i-1][4] + T[i-1][8]
            elif j == 8:
                T[i][j] = T[i-1][5] + T[i-1][7] + T[i-1][9] + T[i-1][0]
            elif j == 9:
                T[i][j] = T[i-1][6] + T[i-1][8]

    return sum(T[n])


def kZeriConsecutivi(n,k):
    def esR(n,k,i,sol,z,zericons):
        if n == i:
            print(sol)
            return
        if z == 0: zericons = True
        if zericons or n-i>k:
            sol.append(1)
            esR(n,k,i+1,sol,k,zericons)
            sol.pop()
        sol.append(0)
        esR(n,k,i+1,sol,z-1,zericons)
        sol.pop()
    sol = []
    esR(n,k,0,sol,k,False)


def stringheConDispari(n):
    def esR(n,nd,i,sol):
        if i == 2*n:
            print(sol)
            return
        elif i < n:
            for e in [1,2,3]:
                sol.append(e)
                if e % 2 == 1:
                    esR(n,nd+1,i+1,sol)
                else:
                    esR(n,nd,i+1,sol)
                sol.pop()
        elif i < 2*n:
            for e in [1,2,3]:
                if e % 2 == 0 and 2*n - i > nd:
                    sol.append(e)
                    esR(n,nd,i+1,sol)
                    sol.pop()
                elif e % 2 == 1 and nd > 0:
                        sol.append(e)
                        esR(n,nd-1,i+1,sol)
                        sol.pop()
    sol = []
    esR(n,0,0,sol)

if __name__ == '__main__':
    print(stringheConDispari(2))