import math
import numpy as np
import matplotlib.pyplot as plt

def adap1(TOL):
    def f(x):
        return 1/(2+(x**2))
    a=-1
    B=1
    temp_func=0.5*f(a)+0.5*f(B)
    h=0.1
    I=h*temp_func
    Ie = 0 
    temp_list=[]
    final_difference=[]
    counter=0
    for N in range(1,400,2):
        h=(b-a)/N
        temp_func=0.5*f(a)+0.5*f(b)
        for k in range(1,N):
            temp_func+=f(a+k*h)
            I=h*temp_func
        temp_list.append(I-Ie)
        counter+=1
        if(I-Ie<TOL):
            break
        Ie = I
    print('number of function evaluations is',counter)
    return counter,temp_list,I

adtrap_10_8_evals=adap1(1*10**-8)[0]
adtrap_10_7_evals=adap1(1*10**-7)[0]
adtrap_10_6_evals=adap1(1*10**-6)[0]
adtrap_10_5_evals=adap1(1*10**-5)[0]
adtrap_10_4_evals=adap1(1*10**-4)[0]
adtrap_10_3_evals=adap1(1*10**-3)[0] #the value [0] outputs function evals, not the value of the integral. Use [2] for that.
