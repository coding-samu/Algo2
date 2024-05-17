import sys
import time
import numpy as np
import matplotlib.pylab as plt

sys.setrecursionlimit(20000)

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
    soluzione = []
    def euristica(mossa, scacchiera):
        x, y = mossa
        combinazioni = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]
        mosse_valide = [(x+px, y+py) for px, py in combinazioni if 0 <= x+px < n and 0 <= y+py < n and scacchiera[y+py][x+px] == 0]
        return len(mosse_valide)

    def ricorsiva(n,combinazioni,scacchiera,sol,x=0,y=0,i=0):
        if i == n*n-1:
            #print(sol, len(sol))
            return True
        combinazioni.sort(key=lambda mossa: euristica((x+mossa[0], y+mossa[1]), scacchiera))  # Ordina le mosse
        for px,py in combinazioni:
            px += x
            py += y
            if px >= 0 and px < n and py >= 0 and py < n and scacchiera[py][px] == 0:
                scacchiera[py][px]=1
                sol.append((px,py,i+1))
                if ricorsiva(n,combinazioni,scacchiera,sol,px,py,i+1):
                    return True
                sol.pop()
                scacchiera[py][px]=0
        return False
    
    scacchiera = [[0 for _ in range(n)] for _ in range(n)]
    scacchiera[0][0] = 1
    sol = [(0,0,0)]
    combinazioni = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]
    t = ricorsiva(n,combinazioni,scacchiera,sol)
    return sol,t

if __name__ == '__main__':

    for i in range (7,8):
        if i == 28 or i == 59 or i == 65 or i == 82 or i == 90 or i == 93 or i == 102 or i == 117 or i == 121 or i == 123 or i == 125: continue
        print("Test metodo per i = " + str(i))
        start = time.time()
        soluzione,t = cerca_percorso(i)
        end = time.time()
        print(end-start)
        print("Trovato per i = " + str(i) + " " + str(t))

        if t:
            M = [[0 for _ in range(i)] for _ in range(i)]
            for e in soluzione:
                M[e[1]][e[0]] = e[2]

            M_np = np.array(M)

            background = np.ones(M_np.shape)

            plt.figure()
            plt.matshow(background, fignum=0, cmap='binary')  # Mostra la matrice di sfondo

            # Calcola la dimensione del testo in base alla dimensione della matrice
            fontsize = max(20 - M_np.shape[0], 5)

            for x in range(M_np.shape[0]):
                for y in range(M_np.shape[1]):
                    plt.text(y, x, str(M_np[x, y]), ha='center', va='center', color='black', fontsize=fontsize)

            plt.xlim(-0.5,i-0.5)
            plt.ylim(-0.5,i-0.5)
            plt.gca().xaxis.tick_top()
            plt.gca().invert_yaxis()
            plt.title('Scacchiera ' + str(i) + 'x' + str(i))
            plt.savefig('esImages/' + str(i) + '.png')

            plt.close()