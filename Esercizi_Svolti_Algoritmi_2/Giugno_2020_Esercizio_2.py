# -*- coding: utf-8 -*-
"""
@author: Viinz


TIPO DI ESERCIZIO: BackTracking
"""

def scesa(M):
    for j in range(len(M)):
        scesaRicorsiva(M, 0, j, [M[0][j]])
    
    
def scesaRicorsiva(M, i, j, sol):
    if i == len(M)-1:   #Ci troviamo nell'ultima riga
        print(sol)
    else:
        for l in range(-1,2):
            if (j+l) in range(len(M)):
                a= j+l
                #print("j: "+str(j)+" l:"+str(l)+" j+l"+str(a))
                sol.append(M[i+1][j+l])
                scesaRicorsiva(M, i+1, j+l, sol)
                sol.pop() 
    
M = [[1,2,3],
     [4,5,6],
     [7,8,9]]

scesa(M)