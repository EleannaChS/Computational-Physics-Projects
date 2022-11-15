# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 19:57:17 2022

@author: EChS
"""

import numpy as np
from numpy.polynomial import Polynomial
import matplotlib.pyplot as plt

# Function to find the product term 
def proterm(i, value, x): 
    pro = 1; 
    for j in range(i): 
        pro = pro * (value - x[j]); 
    return pro; 
  
# Function for calculating 
# divided difference table 
def dividedDiffTable(x, y, n):
  
    for i in range(1, n): 
        for j in range(n - i): 
            y[j][i] = ((y[j][i - 1] - y[j + 1][i - 1]) /(x[j] - x[i + j]));
    return y;
  
# Function for applying Newton's 
# divided difference formula 
def applyFormula(value, x, y, n): 
  
    sum = y[0][0]; 
  
    for i in range(1, n):
        sum = sum + (proterm(i, value, x) * y[0][i]); 
      
    return sum; 
  
# Function for displaying divided 
# difference table 
def printDiffTable(y, n): 
  
    for i in range(n): 
        for j in range(n - i): 
            print(round(y[i][j], 4), "\t", 
                               end = " "); 
  
        print(""); 
  
# Driver Code
  
# number of inputs given 
n = 6; 
y = [[0 for i in range(10)] 
        for j in range(10)]; 
x = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7]
  
# y[][] is used for divided difference 
# table where y[][0] is used for input 
y[0][0] = 0.185; 
y[1][0] = 0.106; 
y[2][0] = 0.093; 
y[3][0] = 0.24; 
y[4][0] = 0.579; 
y[5][0] = 0.561; 

# calculating divided difference table 
y=dividedDiffTable(x, y, n); 
  
# displaying divided difference table 
printDiffTable(y, n); 
  
# value to be interpolated 
value =5; 
  
# printing the value 
#print("\nValue at", value, "is",
        #round(applyFormula(value, x, y, n), 2))

x_pol = np.linspace(0,0.8, 100)
y_pol =  [0.185, 0.106, 0.093, 0.24, 0.579, 0.561] 
p = lambda k: 0.185 - 0.79*(k-x[0]) + 3.3*(k-x[0])*(k-x[1]) + 15.6667*(k-x[0])*(k-x[1])*(k-x[2]) -25.8333*(k-x[0])*(k-x[1])*(k-x[2])*(k-x[3]) - 432.5*(k-x[0])*(k-x[1])*(k-x[2])*(k-x[3])*(k-x[4])                 

#p = Polynomial([24.277473, -36.57035, 208.66278, -312.5593, 839.121, -432.4815])
p_f = Polynomial.fit(x, y_pol, 5)
print(p_f)

fig = plt.figure
plt.plot(x, y_pol, 'ro')
plt.plot(x_pol,p(x_pol))
plt.title("Newton\'s Polynomial")
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('set1_ex4.png')
plt.show()

















