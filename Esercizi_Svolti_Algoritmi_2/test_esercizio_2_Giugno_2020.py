# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 14:58:42 2023

@author: Viinz
"""

def scesa(M):
    for colonna in range(len(M)):
        scesaRicorsiva(M, 0, colonna, [M[0][colonna]])
        

def scesaRicorsiva(M, riga, colonna, sol):
    if riga == len(M)-1:
        print(sol)
    else:
        for a in range(-1,2):
            if (a+colonna) in range(len(M)):
                #Siamo nei limiti della matrice
                sol.append(M[riga+1][a+colonna])
                scesaRicorsiva(M, riga+1, colonna+a, sol)
                sol.pop()

M = [[1,2,3,4],
     [5,6,7,8],
     [9,10,11,12],
     [13,14,15,16]
     ]

scesa(M)