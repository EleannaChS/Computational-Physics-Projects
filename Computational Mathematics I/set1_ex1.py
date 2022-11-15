# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 20:51:37 2022

@author: EChS
"""

#Ypologistika Mathimatika 
#Set 1
#Exercise 1

import numpy as np
import math
import matplotlib.pyplot as plt

fa = lambda x: math.exp(x) - 2*x*math.cos(x) - 3
fb = lambda x: pow(x,2) + math.sin(x) + math.exp(x) - 2
fa_p = lambda x: math.exp(x) + 2*x*math.sin(x) - 2*math.sin(x)
fb_p = lambda x: 2*x + math.cos(x) + math.exp(x)
    
x = np.linspace(-2,2, 100) 
fa_pl =  np.exp(x) - 2*x*np.cos(x)-3
fb_pl = pow(x,2) + np.sin(x) + np.exp(x) -2

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.plot(x,fa_pl, label = "(a)")
plt.plot(x,fb_pl, label = "(b)")
plt.legend(loc='best')
plt.savefig('set1_ex1.png')
plt.show()

def bisection(f, a, b, acc): 
    m = (a + b)/2
    it_num = 0
    if f(a)*f(b) > 0 :
        return print("Wrong a,b")
    else:
        while abs(f(m)) >= acc:
            if f(a)*f(m) < 0:
                b = m
            elif f(a)*f(m) > 0:
                a = m
            else:
                it_num += 1
                break
            m = (a + b)/2
            it_num += 1
            root = m
        print("Root= ", root, "\nIteration number= ", it_num)
        print("f(root) =", f(root))
    return root, it_num

print("\nBisection")
bisection(fa,0,2,pow(10,-10))
bisection(fb,0,1,pow(10,-10))

def newton_rapson(f, f_prime, x0, acc):
    max_it = 50
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


print("\nNewton-Rapson")
newton_rapson(fa, fa_p, 0, pow(10,-10))
newton_rapson(fb, fb_p, 0, pow(10,-10))


















           
    