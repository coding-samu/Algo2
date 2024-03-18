# -*- coding: utf-8 -*-
"""
@author: Viinz

Voglio un Algoritmo che usa la tecnica del BackTracking per calcolare tutte le stringhe
binarie di lunghezza n.

Stampando così 2^n Elementi. Con un Costo Algoritmico Theta(n*2^n)

TIPO DI ESERCIZIO: BackTracking
"""
def bk(n, i=0, Sol=[]):
    if i==n:
        print(''.join(Sol))
    else:
        Sol.append('0')
        bk(n, i+1, Sol)
        Sol.pop()
        Sol.append('1')
        bk(n, i+1, Sol)
        Sol.pop()
        
bk(3)
