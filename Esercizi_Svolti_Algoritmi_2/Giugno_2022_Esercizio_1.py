# -*- coding: utf-8 -*-
"""
@author: Viinz

Soluzione Esercizio 1 Giugno 2022

Tipo soluzione: Programmazione dinamica
"""


"""
 if j==0 and S[j]<S[1]:
                  T[i][j] = 0
              if j>0 and S[j]==i and S[i][j-1]==0 and S[i-1][j]==0:
                  T[i][j]= 0
              if S[j]==i:                  
                T[i][j]= max(T[i][j-1], T[i-1][j])+1
              if j>0 and S[j]!=i:
                T[i][j]=T[i][j-1]
"""
def es1(S):
    T=[[0]*len(S) for _ in range(0,3)]
    for j in range(len(S)):
        if j==0 and S[j]!=0:
            T[0][j]=0
        if j>0 and S[j]==0:
            T[0][j]=T[0][j-1]+1
        if j>0 and S[j]!=0:
            T[0][j]= T[0][j-1]
    
    for i in range(1,3):
          for j in range(len(S)):
              if j==0 and S[j]!=i:
                  T[i][j]=0
              if j>0 and S[j]==i:
                  if T[i-1][j]==0 and T[i][j-1]==0:
                      T[i][j]=0
                  else:
                      T[i][j] = max(T[i][j-1], T[i-1][j])+1
              if j>0 and S[j]!=i:
                  T[i][j]=T[i][j-1]
    print(T)

    

a=[0,1,2,5,6,1,4,1,2,2,2,1,5,2]
b=[5,0,6,7,2,2,1,0,1]
es1(a)




























