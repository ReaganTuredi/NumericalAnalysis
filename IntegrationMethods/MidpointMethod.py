import math
import numpy as np
import matplotlib.pyplot as plt

h_list_error_midpoint=[]
integration_list_midpoint=[]
for n in n_list:
    a = -1
    b = 1
    h = (b - a) / (n)
    x = np.linspace(a, b, n)
    f = 1/(2+(x**2))
    integration_list_midpoint.append(h * sum(((f[:n-1] + f[1:])/2)))
    h_list_error_midpoint.append((h * sum(((f[:n-1] + f[1:])/2)))-\
                                 (math.sqrt(2)*math.atan(math.sqrt(2)/2)))
integration_list_midpoint
