# -*- coding: utf-8 -*-
"""
@author: Viinz

Data una Stringa S sull'alfabeto {0,1,2} Voglio costruire ilnumero di sottostringe 012.
Ad Esempio:
            S = 1210121001; risultato = 1
                   ---     
            S = 0100120;    risultato = 4
                --   -
                -   --
                  - --
                   ---
                   

TIPO DI ESERCIZIO:  Programmazione Dinamica

"""

def es2(S):
    T = [[0] * len(S) for i in range(0,3)]
    for j in range(len(S)):
        if j == 0 and S[j]!='0': T[0][j] = 0
        if j == 0 and S[j]=='0': T[0][j] = 1
        if j > 0 and S[j]!= '0': T[0][j] = T[0][j-1]
        if j > 0 and S[j]== '0': T[0][j] = T[0][j-1]+1
        
    for i in range(1,3):
        for j in range(len(S)):
            if j == '0':
                T[i][j] = 0
            elif j>0 and S[j]!=str(i):
                T[i][j] = T[i][j-1]
            elif j>0 and S[j]==str(i):
                T[i][j] = T[i][j-1] + T[i-1][j]
    
    print(T[-1][-1])

es2('0100120')    
