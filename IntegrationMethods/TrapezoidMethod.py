n_list=[4,8,16,32,64,128]
h_list_error_trapezoid=[]
integration_list_trapezoid=[]
for n in n_list:
    a = -1
    b = 1
    h = (b-a)/n
    x = np.linspace(a, b, n+1)
    f = 1/(2+(x**2))
    integration_list_trapezoid.append((h)*(sum(f[1:n]) + 0.5*((f[0]) + f[n])))
    h_list_error_trapezoid.append(( (h)*(sum(f[1:n]) + 0.5*((f[0]) + f[n])))\
                                  - (math.sqrt(2)*math.atan(math.sqrt(2)/2)) )
integration_list_trapezoid
