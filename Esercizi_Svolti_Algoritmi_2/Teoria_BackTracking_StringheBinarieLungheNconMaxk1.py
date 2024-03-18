# -*- coding: utf-8 -*-
"""
@author: Viinz

Voglio un Algoritmo che usa la tecnica del BackTracking per calcolare tutte le stringhe
binarie di lunghezza n con al Max k 1.


TIPO DI ESERCIZIO: BackTracking
"""

def bk2(n,k,j=0,i=0,Sol=[]):
    if i==n:
        print(''.join(Sol))
    else:
        Sol.append('0')
        bk2(n, k, j, i+1, Sol)
        Sol.pop()
        if j<k:   #Siamo nel Caso in cui abbiamo ancora la possibilità di aggiungere degli 1 nella Stringa
            Sol.append('1')
            bk2(n, k,j+1, i+1, Sol)
            Sol.pop()
        
bk2(4, 2)
            

