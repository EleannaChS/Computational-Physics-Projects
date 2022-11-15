#Ypologistika Mathimatika 
#Set 2
#Exercise 1
#Choraiti Sideri ELeanna
#AEM 4406

import numpy as np
import matplotlib.pyplot as plt
import math as m
from array import *

f = lambda t,y: y*pow(t,2) - 1.1*y


def Eulers(t0, fx, tmax, h):
    n = (int)((tmax - t0)/h)
    
    y = 1
    t = 0
    
    t_array = array('d', [])
    y_array = array('d', [])
    
    for i in range(0, n+1):
        
        t_array.append(t)
        y_array.append(y)
        
        k = f(t,y)
        
        y = y + k*h
        t = t + h
    return t_array, y_array    
    
def RK4(t0, fx, tmax, h):
   
    n = (int)((tmax - t0)/h)
    
    y = 1
    t = 0
    
    t_array = array('d', [])
    y_array = array('d', [])
    
    for i in range(0, n+1):
        
        t_array.append(t)
        y_array.append(y)
        
        k1 = f(t,y)                
        k2 = f(t + 0.5*h, y + 0.5*h*k1)        
        k3 = f(t + 0.5*h, y + 0.5*h*k2)  
        k4 = f(t + h, y + h*k3)
            
        y = y + h*(1/6*k1 + 1/3*k2 + 1/3*k3 + 1/6*k4)
        t = t + h
      
    return t_array, y_array
 
(t1,y1) = Eulers(0, f, 2, 0.5)
(t2,y2) = Eulers(0, f, 2, 0.25)
(t3,y3) = RK4(0, f, 2, 0.5)
(t4,y4) = RK4(0, f, 2, 0.25)

fig = plt.figure
plt.plot(t1,y1, label = "Eulers, h=0.5")
plt.plot(t2,y2, label = "Eulers, h=0.25")
plt.plot(t3,y3, label = "RK4, h=0.5")
plt.plot(t4,y4, label = "RK4, h=0.25")
plt.legend(loc="best")
plt.title("Solving of the ODE dy/dt = yt^2 -1.1y")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.grid()






