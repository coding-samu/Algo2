# -*- coding: utf-8 -*-
"""
@author: Viinz

Esercizio 2 Settembre

Tipo di soluzione: BackTracking
"""
def es2(n, i=0, d_p=0, d_s=0, sol=[]):
    if i==2*n:
        print("".join(sol))
    else:
        #Mettiamo un numero qualsiasi finchè sono nella prima metà della sequenza
        if i<n: #Siamo nella prima parte
            sol.append('1')
            es2(n,i+1,d_p+1,d_s,sol)
            sol.pop()
            
            sol.append('2')
            es2(n,i+1,d_p,d_s,sol)
            sol.pop()
            
            sol.append('3')
            es2(n,i+1,d_p+1,d_s,sol)
            sol.pop()
        else:                    
            if 2*n-1-i +d_s >= d_p:
                sol.append('2')
                es2(n,i+1,d_p,d_s,sol)
                sol.pop()
            if d_s+1<=d_p:
                sol.append('1')
                es2(n,i+1,d_p,d_s+1,sol)
                sol.pop()
                    
                sol.append('3')
                es2(n,i+1,d_p,d_s+1,sol)
                sol.pop()
                
                
es2(2)
            
        




