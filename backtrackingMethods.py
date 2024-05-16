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

def cerca_percorso(n):
    def ricorsiva(n,combinazioni,scacchiera,sol,x=0,y=0,i=0):
        if i == n*n-1:
            print(sol, len(sol))
            return True
        for px,py in combinazioni:
            px += x
            py += y
            if px >= 0 and px < n and py >= 0 and py < n and scacchiera[py][px] == 0:
                scacchiera[py][px]=1
                sol.append((px,py))
                if ricorsiva(n,combinazioni,scacchiera,sol,px,py,i+1):
                    return True
                sol.pop()
                scacchiera[py][px]=0
        return False
    
    scacchiera = [[0 for _ in range(n)] for _ in range(n)]
    scacchiera[0][0] = 1
    sol = [(0,0)]
    combinazioni = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]
    return ricorsiva(n,combinazioni,scacchiera,sol)

if __name__ == '__main__':
    print(cerca_percorso(5))