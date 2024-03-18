# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 13:41:56 2023

@author: Viinz
"""

def es2(X, i=0, sol=[]):
    if i == len(X):
        print("".join(sol))
    else:
        for k in {'0','1','2'}:
            if X[i]!=k and i>0 and sol[i-1]!=k:
                sol.append(k)
                es2(X, i+1, sol)
                sol.pop()
            if X[i]!=k and i==0:
                sol.append(k)
                es2(X, i+1, sol)
                sol.pop()
                

es2('2001')
        
    