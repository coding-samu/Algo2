import sys
import time
import numpy as np
import matplotlib.pylab as plt
sys.setrecursionlimit(20000)

def cerca_percorso(n):
    iterazioni = 0
    def euristica(mossa, scacchiera):
        x, y = mossa
        combinazioni = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]
        mosse_valide = [(x+px, y+py) for px, py in combinazioni if 0 <= x+px < n and 0 <= y+py < n and scacchiera[y+py][x+px] == 0]
        score = len(mosse_valide)
        # Aggiungi un bonus per le mosse che portano verso il centro della scacchiera
        distanza_centro = abs(n/2 - x) + abs(n/2 - y)
        score -= distanza_centro / n  # Normalizza la distanza per il numero di celle
        return score

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
    return sol,t,iterazioni

def verifica_matrice(matrice):
    n = len(matrice)
    numeri_visti = set()
    for riga in matrice:
        for numero in riga:
            if numero in numeri_visti or numero < 0 or numero >= n*n:
                return False
            numeri_visti.add(numero)
    return True

def salva_matrice_come_immagine(M):
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

if __name__ == '__main__':

    for i in range (2,101):
        print("Test metodo per i = " + str(i))
        start = time.time()
        soluzione,t,iterazioni = cerca_percorso(i)
        end = time.time()
        print(end-start)
        print("Trovato per i = " + str(i) + " " + str(t))
        M = [[-1 for _ in range(i)] for _ in range(i)]
        for e in soluzione:
            M[e[1]][e[0]] = e[2]
        vm = verifica_matrice(M)
        print("Matrice verificata: " + str(vm))
        print()
        
        if t and i < 10:
            salva_matrice_come_immagine(M)