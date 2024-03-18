# -*- coding: utf-8 -*-
"""
@author: Viinz

Esercizo 1 Luglio 2022

Tipo di soluzione: Programmazione dinamica
"""

def es1(S):
    T=[[0]*len(S) for _ in range(0,2)]
    for j in range(len(S)):
        if j==0 and S[j]!=0:
            T[0][j]=0
        if j==0 and S[j]==0:
            T[0][j]=1
        if j>0 and S[j]!=0:
            T[0][j]=T[0][j-1]
        if j>0 and S[j]==0:
            T[0][j]=T[0][j-1]+1
    
    for j in range(len(S)):
        if j==0:
            T[1][j]=0
        if S[j]==1:
            T[1][j]=T[1][j-1] + T[0][j]
        if S[j]!=1:
            T[1][j]=T[1][j-1]
    print(T)
    print(T[-1][-1])



S=[0,1,0,0,0,1,0,1]
es1(S)




