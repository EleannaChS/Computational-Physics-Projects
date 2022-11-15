# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 16:39:32 2022

@author: EChS
"""

import numpy as np
from numpy.polynomial import Polynomial
import matplotlib.pyplot as plt
import math

x = [-1, 0, 1]
#x = [0, 1, 4]

f = lambda x: 1 + math.sin(math.pi*x)
#f = lambda x: 2*pow(x,0.5) 

y = [f(x[0]), f(x[1]), f(x[2])]
print(y,"\n")
    
p = Polynomial.fit(x, y, 2)
print(p,"\n")

#x_pol = np.linspace(-2,2, 100) 
x_pol = np.linspace(-2,6, 100)

fig = plt.figure
plt.plot(x, y, 'ro')
plt.plot(x_pol,p(x_pol))
plt.title('Lagrange Polynomial')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('set1_ex3.png')
plt.show()