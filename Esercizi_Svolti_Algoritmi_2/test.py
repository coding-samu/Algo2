# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 14:05:57 2023

@author: Viinz
"""
def es2(n,k,i=0,zs=0,done=False,sol=[]):
    if i==n:
        print("".join(sol))
    else:
        if done or (n-i-1)>=k:
            sol.append('1')
            es2(n,k,i+1,0,done,sol)
            sol.pop()
        sol.append('0')
        if zs+1>=k: 
            done=True
        es2(n,k,i+1,zs+1,done,sol)
        sol.pop()

es2(4,2)
    
