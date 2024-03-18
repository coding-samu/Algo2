# -*- coding: utf-8 -*-
"""
@author: Viinz

Soluzione esercizio Gennaio.

Tipo di soluzione: Programmazione dinamica
"""

def es1(S):
    n = len(S)
    T = [[0]*n for _ in range(len(S))]
    
    for i in range(n):
        for j in range(n):
            if S[j] > S[i]:             #Caso j > i
                T[i][j]=0
            if j==0 and S[i]%S[j]==0:   #Caso colonna 0 i viene diviso da j
                T[i][j] = 1
            if j==0 and S[j]<S[i]:      #Caso Colonna 0 i non viene diviso da j
                T[i][j]=0
            if S[i]%S[j]!= 0:   #Caso S[j] non divide S[i] ma colonna è >0
                T[i][j] = T[i][j-1]
            if S[i]%S[j]==0:
                T[i][j] = T[i][j-1] +1
    max_elem=0
    for a in range(n):
        if T[a][a] > max_elem:
            max_elem=T[a][a]
        
            
    print(max_elem)
    
    
f=[3,5,10,20]
s=[1,3,6,13,17,18]
    
es1(s)



