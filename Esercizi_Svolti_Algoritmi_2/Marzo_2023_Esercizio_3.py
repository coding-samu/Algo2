# -*- coding: utf-8 -*-
"""
@author: Viinz

Indici e Variabili usate:
    i=0 : l'indice che indica la posizione nella Stringa di numeri
    tot=0 : indica la somma dei nodi Passatti, fino a quello dove ci troviamo ora
    sol=[] : è la lista che useremo per concatenare gli elementi della funzione.

TIPO DI ESERCIZIO: BackTracking

"""


def es3(n,k,T, i=0, tot=0, Sol=[]):
    
    if i == n:  #Siamo nel caso in cui ci troviamo sul nodo Foglia
        print(Sol)
        return
    for j in range(k+1):  #Per ogni nodo dove ci troviamo siamo pronti a inserirci nei k rami
        if tot + j + (n - i - 1)*k >= T:
            Sol.append(j)
            es3(n,k,T, i+1, tot+j, Sol)
            Sol.pop()
            
es3(3,5,12)

            
        
        
    
    

