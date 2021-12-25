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
