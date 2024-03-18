# -*- coding: utf-8 -*-
"""
@author: Viinz

Esercizio 2 Traccia di Ottobre

Tipo di Esercizio: BackTracking
"""

def es2(n, tot_zero=0, i=0, sol=[]):
    if i==2*n:
        print("".join(sol))
    else:
        if tot_zero<n:
            sol.append('0')
            es2(n, tot_zero+1, i+1, sol)
            sol.pop()
            
            sol.append('1')
            es2(n, tot_zero, i+1, sol)
            sol.pop()
            
        else:
            sol.append('1')
            es2(n, tot_zero, i+1, sol)
            sol.pop()
        
es2(2)        
