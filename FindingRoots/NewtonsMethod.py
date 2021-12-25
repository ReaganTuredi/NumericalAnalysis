import numpy as np 
import matplotlib.pyplot as plt 
from sympy import *
import sympy as sym
import math
from numpy import arange

def newton_method(func, deriv, init_guess, ep=0.0000000001):
    dx = ep*2
    x = init_guess
    counter=0
    while (dx > ep):
        x1 = x - func(x)/deriv(x)
        dx = abs(x - x1)
        x = x1
        counter=counter +1
        #print(counter)
        if counter==100:
            #print('max iterations hit')
            break
    if counter<50:
        return (round(x,10))
f= lambda x: x-(4*np.sin(2*x)) - 3
derivative= lambda x: -8*math.cos(2*x)+1
root_list=[]
for i in range(-10,10):
    if(newton_method(f,derivative,i)!= None):
        root_list.append(newton_method(f,derivative,i))
set(root_list)

