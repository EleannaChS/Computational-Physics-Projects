#Computational Electromagnetism
#Set 1
#Exe 1.1
#Eleanna Choraiti Sideri
#AEM 4406

import numpy as np
import matplotlib.pyplot as plt

#The function vp_c calculates the ratio of the numerical phase velocity
#divided by the analytical phase velocity i.e. c
#a is the the a in the relation cDt = aDx
#u is the ratio u = Dx/lambda
def vp_c(a, u):
    return u*2.0*np.pi/np.arccos((1.0/a)**2.0*(np.cos(2.0*np.pi*a*u)-1.0)+1.0)

def ph_err(vp, n):
    return ((1.0/vp)-1)*360*n

u_pl = np.linspace(0.001, 1, 10000)
n = 10 

a1 = 0.5
vp_c1 = vp_c(a1, u_pl) 
err1 = np.abs(vp_c1 - 1.0)
ph_err1 = ph_err(vp_c1 , n)

a2 = 0.25
vp_c2 = vp_c(a2, u_pl)
err2 = np.abs(vp_c2 - 1.0)
ph_err2 = ph_err(vp_c2 , n)

a3 = 0.125
vp_c3 = vp_c(a3, u_pl)
err3 = np.abs(vp_c3 - 1.0)
ph_err3 = ph_err(vp_c3 , n)

plt1 = plt.figure

plt.plot(u_pl,vp_c1, "-", color = "blue", label = "a=0.5")
plt.plot(u_pl,vp_c2, "-", color = "red", label = "a=0.25")
plt.plot(u_pl,vp_c3, "-", color = "green", label = "a=0.125")

plt.xscale("log")
plt.grid()
plt.legend()
plt.title("vp/c = f(Dx/lambda), cDt=aDx")
plt.xlabel("Dx/lambda")
plt.ylabel("vp/c")
#plt.ylim([0, 1.1])
plt.savefig('vp_c.png')
plt.show()

u_test = 0.1

print("a=0.5, Dx/lambda=0.1,\nvp/c = ",vp_c(a1, u_test), "\n")
print("phase error over 10lambda_0: ",  ph_err(vp_c(a1, u_test), n), "\n")
print("a=0.25, Dx/lambda=0.1,\nvp/c = ",vp_c(a2, u_test), "\n")
print("phase error over 10lambda_0: ",  ph_err(vp_c(a2, u_test), n), "\n")
print("a=0.125, Dx/lambda=0.1,\nvp/c = ",vp_c(a3, u_test), "\n")
print("phase error over 10lambda_0: ",  ph_err(vp_c(a3, u_test), n), "\n")

#Plot near Dx/lambda = 0.1 
plt2 = plt.figure

plt.plot(u_pl,vp_c1, "-", color = "blue", label = "a=0.5")
plt.plot(u_pl,vp_c2, "-", color = "red", label = "a=0.25")
plt.plot(u_pl,vp_c3, "-", color = "green", label = "a=0.125")
plt.xscale("log")
plt.xlim([0.08, 0.12])
plt.ylim([0.98, 0.99])
#default_x_ticks = range(1)
#plt.xticks(default_x_ticks, 0.1)
plt.grid()
plt.legend()
plt.title("vp/c = f(Dx/lambda), cDt=aDx")
plt.xlabel("Dx/lambda")
plt.ylabel("vp/c")

plt.show()

#error plot
plt3 = plt.figure

plt.plot(u_pl,err1, "-", color = "blue", label = "a=0.5")
plt.plot(u_pl,err2, "-", color = "red", label = "a=0.25")
plt.plot(u_pl,err3, "-", color = "green", label = "a=0.125")

plt.xscale("log")
plt.yscale("log")
plt.grid()
plt.legend()
plt.title("|vp - c|/c error")
plt.xlabel("Dx/lambda")
plt.ylabel("error")
plt.xlim([0.001, 1])
plt.savefig('error.png')

plt.show()

#phase error plot
plt3 = plt.figure

plt.plot(u_pl,ph_err1, "-", color = "blue", label = "a=0.5")
plt.plot(u_pl,ph_err2, "-", color = "red", label = "a=0.25")
plt.plot(u_pl,ph_err3, "-", color = "green", label = "a=0.125")

plt.xscale("log")
plt.yscale("log")
plt.grid()
plt.legend()
plt.title("Phase error")
plt.xlabel("Dx/lambda")
plt.ylabel("error")
plt.xlim([0.001, 1])
plt.savefig('phase_error.png')
plt.show()

#plot of values of vp/c = f(a)
x = [0.125, 0.25, 0.5]
y = [vp_c(a3, u_test), vp_c(a2, u_test), vp_c(a1, u_test)]

a, b = np.polyfit(x, y, 1)
y_fit = [a*x[0]+b, a*x[1]+b, a*x[2]+b ]

plt4 = plt.figure
plt.plot(x, y,".")
plt.plot(x, y_fit)
plt.grid()
plt.title("vp/c = f(a)")
plt.xlabel("a")
plt.ylabel("vp/c")
plt.savefig('vp_c_a.png')

print("Linear fitting line:\nvp/c = ",a,"a + ",b)
