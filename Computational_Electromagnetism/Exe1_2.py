#Computational Electromagnetism
#Set 1
#Exe 1.2
#Eleanna Choraiti Sideri
#AEM 4406

import numpy as np
import matplotlib.pyplot as plt

#initialisation of the computational space with zeros
rows, cols = (150, 150)
cs = [[0.0 for i in range(cols)] for j in range(rows)]
#for row in cs:
#    print(row)
    
#application of the initial conditions
for i in range(1,6):
    cs[0][i] = 1.0
    cs[1][i+1] = 1.0
for j in range(6,11):
    cs[0][j] = -1.0
    cs[1][j+1] = -1.0
    
c = 1.0
#u = Dt/Dx

u = 0.9
#u = 1.0
#u = 1.1

nmax = 101
imax = cols-1

#explicit time-marching solution
for n in range(1,nmax):
    for i in range(1,imax):
        cs[n+1][0] = 0.0
        cs[n+1][imax-1] = 0.0
        cs[n+1][i] = (c*u)**2*(cs[n][i+1]-2.0*cs[n][i]+cs[n][i-1]) + 2.0*cs[n][i] - cs[n-1][i]

#this was a test print
#print()
#for row in cs:
#    print(row)    

arr1 = cs[0]
arr2 = cs[21]
arr3 = cs[41]
arr4 = cs[61]
arr5 = cs[81]
arr6 = cs[101]
x = np.linspace(0,1,len(arr1))

plt.figure()
plt.plot(x, arr1, label = "t=0" )
plt.plot(x, arr2, label = "t=20")
plt.plot(x, arr3, label = "t=40")
plt.plot(x, arr4, label = "t=60")
plt.plot(x, arr5, label = "t=80")
plt.plot(x, arr6, label = "t=100")
plt.title("Discrete wave equation explicit time-marching solution \n(Dt/Dx = 0.9)")
#plt.title("Discrete wave equation explicit time-marching solution \n(Dt/Dx = 1.0)")
#plt.title("Discrete wave equation explicit time-marching solution \n(Dt/Dx = 1.1)")
plt.grid()
plt.legend(loc="best")
plt.xlabel("x")
plt.ylabel("f")
fig = plt.figure(figsize=(4, 6))
 
axs = fig.subplots(6, sharex=True)
fig.suptitle("Discrete wave equation \nexplicit time-marching solution \n(Dt/Dx = 0.9)")
#fig.suptitle("Discrete wave equation \nexplicit time-marching solution \n(Dt/Dx = 1.0)")
#fig.suptitle("Discrete wave equation \nexplicit time-marching solution \n(Dt/Dx = 1.1)")
axs[0].plot(x, arr1, label = "t=0" )
axs[0].legend(loc="best", prop={'size': 7})
axs[1].plot(x, arr2, label = "t=20")
axs[1].legend(loc="best", prop={'size': 7})
axs[2].plot(x, arr3, label = "t=40")
axs[2].legend(loc="best", prop={'size': 7})
axs[3].plot(x, arr4, label = "t=60")
axs[3].legend(loc="best", prop={'size': 7})
axs[4].plot(x, arr5, label = "t=80")
axs[4].legend(loc="best", prop={'size': 7})
axs[5].plot(x, arr6, label = "t=100")
axs[5].legend(loc="best", prop={'size': 7})
plt.xlabel("x")
plt.ylabel("f")

