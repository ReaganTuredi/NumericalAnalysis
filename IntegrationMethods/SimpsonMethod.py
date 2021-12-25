import math
import numpy as np
import matplotlib.pyplot as plt

h_list_error_simpson=[]
integration_list_simpson=[]
for n in n_list:
    a = -1
    b = 1
    h = (b - a) / (n)
    x = np.linspace(a, b, n+1)
    f = 1/(2+(x**2))
    integration_list_simpson.append((h/3) *  np.sum(f[0:-1:2]+4*f[1::2]+f[2::2]))
    h_list_error_simpson.append(((h/3) *  np.sum(f[0:-1:2]+4*f[1::2]+f[2::2]))\
                                  - (math.sqrt(2)*math.atan(math.sqrt(2)/2)) )
integration_list_simpson
