
#acceptance - rejection method
"""
requested f(x)=2/(pi(1-x^2)^0.5), 0<x<1
we choose g(x)=1/(2(1-x)^0.5)
k: f(x)/g(x) supremum
f(x)/g(x)= 4/(pi*(1+x)^0.5) <= 4/pi, hence k = 4/pi
""" 

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng()

def f(x):
    return 2/(np.pi*pow((1-x**2),0.5))

def g(x):
    return 1/(2*pow(1-x,0.5))

def G_inv(x):
    return 1.-x**2

#test x~g(x)
x1 = rng.uniform(0,1,100000)

y = G_inv(x1)

x_plot = np.linspace(0.,1)

plt.figure(figsize = (8,8))
plt.hist(y, bins=50, density=True, label="invesre function data")
plt.plot(x_plot,g(x_plot), label="g(x)")
plt.legend(loc="upper right")

#Acceptance-Rejection method
k = 4/np.pi
acc = 0

its = 100
yf=[]

u1 = rng.uniform()

for i in range(its):
    u1 = rng.uniform()
    y = G_inv(u1)
    u2 = rng.uniform()
    
    if(u2 <= f(y)/(k*g(y))):
        flag = 1 #acceptacne
        yf.append(y)
    else:
        flag = 0  

    acc = acc + flag
    
print("Acceptance rate:", acc/its)

plt.figure(figsize = (8,8))
plt.hist(yf, density=True, label="data genetated from Acceptance-Rejection method")
plt.plot(x_plot,f(x_plot), label="f(x)")
plt.legend(loc="upper right")









