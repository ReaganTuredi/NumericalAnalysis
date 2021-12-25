import numpy as np 
import matplotlib.pyplot as plt 
from sympy import *
import sympy as sym
import math
from numpy import arange

def secant_method(f,a,b,N):
    for i in range(1,N):
        temp1 = a - f(a)*(b-a)/(f(b) - f(a))
        temp2 = f(temp1)
       
        if f(a)*temp2 < 0:
            a = a
            b = temp1
        elif f(b)*temp2 < 0:
            a = temp1
            b = b
        elif temp2 == 0:
            return temp1
        else: 
            return 0
    temp_return=(a -(f(a)*(b - a))/(f(b) - f(a)))
    return temp_return
#------------------------------------------------------
#Error calculation 

# error calculation for secant method
def secant_method_error(f,a,b,N):
    lists=[]
    for i in range(1,N):
        temp1 = a - f(a)*(b-a)/(f(b) - f(a))
        temp2 = f(temp1)
       
        if f(a)*temp2 < 0:
            a = a
            b = temp1
            lists.append(b)
        elif f(b)*temp2 < 0:
            a = temp1
            b = b

        elif temp2 == 0:
            return temp1
        else: 
            return 0
    temp_return=(a -(f(a)*(b - a))/(f(b) - f(a)))
    return lists

sme=secant_method_error(f,2,3,8)

p_0_sm=[]
p_1_sm=[]
p_2_sm=[]
for i in range(0,5):
    p_0_sm.append((error(sme[i+1],sme[i],3.1618,0)))
    p_1_sm.append((error(sme[i+1],sme[i],3.1618,1)))
    p_2_sm.append((error(sme[i+1],sme[i],3.1618,2)))
