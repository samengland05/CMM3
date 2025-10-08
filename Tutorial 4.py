#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  7 16:26:39 2025

@author: charliepeyton
"""
import numpy as np
def newton(f,Df,x0,E,maxit): 
    xn=x0 
    for n in range(0,maxit): 
        fxn=f(xn) 
        if abs(fxn)<E: 
            print('Found solution after',n,'iterations') 
            return xn  
        Dfxn=Df(xn) 
        if Dfxn==0:  
            print('Zero derivative.No solution found')  
            return None 
        
        xn=xn-(fxn/Dfxn) 
   
    print('Exceeded maximum iterations. No solution found') 
    return None

f=lambda x:x**2+4*x-12
df=lambda x:2*x+4
x0=1
E=0.001
max_iter=100

solution=newton(f,df,x0,E,max_iter)
print(solution)
