import numpy as np 
import matplotlib.pyplot as plt 
import sympy as sym
from sympy import *
import math
from numpy import arange


f= lambda x: x-(4*np.sin(2*x)) - 3 #this is nothing more than a function f(x)... you can use whichever function you want.

def fixed_point(g,a,iterations):
    x_0 = a
    temp_list=[]
    for val in range(iterations):
        next_x = g(x_0)
        x_0 = next_x
        temp_list.append(next_x)
    return_val=temp_list[iterations-1]
    return round(return_val,10)
  
g = lambda x: -np.sin(2*x) + 5*x/4 - 3/4.
temp_list_1=[]
for i in range(-1,5):
    temp_list_1.append(fixed_point(g,i,20))
temp_list_1


## This method is not good! The purpose of this module is to show in inefficiency of this method. 


#------------------------------------------------
#Error calculation

def fixed_point_error(g,a,iterations):
    x_0 = a
    temp_list=[]
    for val in range(iterations):
        next_x = g(x_0)
        x_0 = next_x
        temp_list.append(next_x)
    return temp_list

fp_error_list=[]   
fp_error_list.append(fixed_point_error(g,4,6))
fp_error_list=fp_error_list[0]

p_0_fp=[]
p_1_fp=[]
p_2_fp=[]
for i in range(0,5):
    p_0_fp.append((error(fp_error_list[i+1],fp_error_list[i],3.1618,0)))
    p_1_fp.append((error(fp_error_list[i+1],fp_error_list[i],3.1618,1)))
    p_2_fp.append((error(fp_error_list[i+1],fp_error_list[i],3.1618,2)))
