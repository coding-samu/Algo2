# -*- coding: utf-8 -*-
"""
@author: Viinz

Numero di telefono di lunghezza n, con cifre adiacenti del tastietino numerico

1 2 3 
4 5 6 
7 8 9 
* 0 #

TIPO DI ESERCIZIO: Programmazione Dinamica

"""
      
def es1(n):
    T = [[0]*10 for _ in range(n+1)]
    for i in range(n+1):
        for j in range(10):
            if i==0:
                T[i][j]=0
            elif i==1:
                T[i][j]=1

            elif j==0: T[i][j] = T[i-1][8]
            elif j==1: T[i][j] = T[i-1][2] + T[i-1][4]
            elif j==2: T[i][j] = T[i-1][1] + T[i-1][4] + T[i-1][3]
            elif j==3: T[i][j] = T[i-1][2] + T[i-1][6]
            elif j==4: T[i][j] = T[i-1][1] + T[i-1][5] + T[i-1][7]
            elif j==5: T[i][j] = T[i-1][2] + T[i-1][4] + T[i-1][6] + T[i-1][8]
            elif j==6: T[i][j] = T[i-1][3] + T[i-1][5] + T[i-1][9]
            elif j==7: T[i][j] = T[i-1][4] + T[i-1][8]
            elif j==8: T[i][j] = T[i-1][5] + T[i-1][7] + T[i-1][9] + T[i-1][0]
            elif j==9: T[i][j] = T[i-1][6] + T[i-1][8]
    print(sum(T[n]))

es1(3)

