#Ypologistika Mathimatika 
#Set 2
#Exercise 1
#Choraiti Sideri ELeanna
#AEM 4406

import numpy as np
import matplotlib.pyplot as plt
import math as m
from array import *

f = lambda x: x*m.exp(2*x)
#f = lambda x: 3*pow(x,3) - x  - pow(x,2)

a = 0
b = 3

x_pl = np.linspace(a,b,100)
f_pl = x_pl*np.exp(2*x_pl)
#f_pl = 3*pow(x_pl,3) - x_pl - pow(x_pl,2)

fig = plt.figure()
plt.plot(x_pl,f_pl, label = "f(x)")
plt.title("f(x) = xexp(2x)")
plt.grid()
plt.xlabel("x")
plt.ylabel("f(x)")

n_tr = 8
n= 2*n_tr

h = abs((b-a))/n


y_list = array('d',[])

x_list = np.arange(a, b+h, h)
for i in range(len(x_list)):
    y_list.append(f(x_list[i]))

#print(x_list)
#print(y_list)

integral = 0

for j in range(0, n-1,2):
    integral = integral + h/3*(y_list[j] + 4*y_list[j+1] + y_list[j+2])
    
print("Simpson's rule\n")
print("Number of triads: ", n_tr , "\n")
print("The integral's value is", integral, "\n")    
    
    
    
   