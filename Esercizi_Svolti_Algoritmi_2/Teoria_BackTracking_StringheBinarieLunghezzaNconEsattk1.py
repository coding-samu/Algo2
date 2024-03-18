# -*- coding: utf-8 -*-
"""
@author: Viinz

Voglio un Algoritmo che usa la tecnica del BackTracking per calcolare tutte le stringhe
binarie di lunghezza n con al ESATTAMENTE  k 1.


TIPO DI ESERCIZIO: BackTracking
"""
def bk3(n,k,tot=0, i=0, Sol=[]):
    if i==n:
        print(''.join(Sol))
    else:
        if tot + n - (i+1) >=k:
            Sol.append('0')
            bk3(n, k, tot, i+1, Sol)
            Sol.pop()
        if tot < k:
            Sol.append('1')
            bk3(n,k,tot+1,i+1,Sol)
            Sol.pop()
            
        
bk3(6,3)