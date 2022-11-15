# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 20:00:13 2022

@author: EChS
"""

#Ypologistika Mathimatika 
#Set 1
#Exercise 1

import numpy as np
import math
import matplotlib.pyplot as plt

f = lambda x: 2*math.exp(x) - 3*x**2
g = lambda x: (2*math.exp(x) - x) / (3*x - 1)
f_prime = lambda x: 2*math.exp(x) - 6*x

x = np.linspace(-2,2, 100) 
f_pl = 2*np.exp(x) - 3*x**2

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.plot(x,f_pl, label = "f(x)")
plt.legend(loc='best')
plt.savefig('set1_ex2.png')
plt.show()

def s_f_p_i (fx, gx, x0, acc):
    it_num = 0
    max_it = 50
    root = x0
    while abs(f(root)) >= acc and it_num < max_it:
        x0 = root
        root = g(x0)
        it_num += 1
    print("Root= ", root, "\nIteration number= ", it_num)
    print("f(root) =", f(root))
    return  

def newton_rapson(f, f_prime, x0, acc):
    max_it = 60
    root = x0 
    it_num = 0
    while abs(f(root)) >= acc:
        xi = root
        if f_prime(xi) == 0:
            print("f'(x)=0, can't continue\n")
            print("Root= ", root, "\nIteration number= ", it_num)
            break
        root = xi - (f(xi)/f_prime(xi))
        it_num += 1
        if it_num == max_it:
            print("Maximum iterations")
            print("Root= ", root, "\nIteration number= ", it_num)
            break
    print("Root= ", root, "\nIteration number= ", it_num)
    print("f(root) =", f(root))
    return root, it_num
    

print("\nx=g(x) method")
s_f_p_i(f,g,-1,pow(10,-10))

print("\nNewton-Rapson method")
newton_rapson(f, f_prime, -1, pow(10,-10))
