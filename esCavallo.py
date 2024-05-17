import sys
import time
from utilities import salva_matrice_come_immagine, salva_matrice_come_json

sys.setrecursionlimit(3000000)

def cerca_percorso(n):
    iterazioni = 0
    def euristica(mossa, scacchiera):
        x, y = mossa
        combinazioni = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]
        mosse_valide = [(x+px, y+py) for px, py in combinazioni if 0 <= x+px < n and 0 <= y+py < n and scacchiera[y+py][x+px] == 0]
        score = len(mosse_valide)
        distanza_centro = abs(n/2 - x) + abs(n/2 - y)
        score -= distanza_centro / n
        return score

    def ricorsiva(n,combinazioni,scacchiera,sol,x=0,y=0,i=0):
        if i == n*n-1:
            return True
        combinazioni.sort(key=lambda mossa: euristica((x+mossa[0], y+mossa[1]), scacchiera))
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
    return sol,t,iterazioni

def test_func(i):
    print("Test metodo per i = " + str(i))
    start = time.time()
    soluzione,t,iterazioni = cerca_percorso(i)
    end = time.time()
    print(end-start)
    print("Trovato per i = " + str(i) + " " + str(t))
    M = [[-1 for _ in range(i)] for _ in range(i)]
    for e in soluzione:
        M[e[1]][e[0]] = e[2]
    print()
    return t,M

if __name__ == '__main__':

    for i in range (2,301):
        t,M = test_func(i)
        if t:
            if i < 26:
                salva_matrice_come_immagine(M,i,'esCavalloImages/')
            salva_matrice_come_json(M,i,'esCavalloJson/')