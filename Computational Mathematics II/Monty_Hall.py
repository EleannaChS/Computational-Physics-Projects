#Monty Hall Problem

import numpy as np
import matplotlib.pyplot as plt 

rng = np.random.default_rng()

#Test of the random number generator
#test = rng.random((100,1))
#test_x = np.linspace(0, 1, 100)
#plt.figure
#plt.scatter(test_x,test)

def door_decision_1_2():
    n = rng.random()
    if n < 1./3.:
        i_de_i = 0
    elif n < 2./3.:
        i_de_i = 1
    else:
        i_de_i = 2
    return i_de_i

def door_desicion_3():
    i_de_i = 0
    return i_de_i

def strategy_1(i_de):
    i_de_f = i_de
    return i_de_f

def strategy_2(i_de, i_gift):
    for i in range(3):
        if i != i_de and i != i_open:
            i_de_f = i
    return i_de_f

def strategy_3(i_de, i_gift):
    if i_open == 2:
        i_de_f = 1
    else:
        i_de_f = i_de
    return i_de_f    

prob_t = []
n_t = []

for Nmax in range(10,10000,10):        
    flag = 0   
    for j in range(Nmax):     
    #The gift is being placed behing a door
        p = [0, 0, 0]
        n = rng.random()
        #print(n)
        if n < 1./3.:
            p[0] = 1
            p[1] = 0
            p[2] = 0
            i_gift = 0
        elif n < 2./3.:
            p[0] = 0
            p[1] = 1
            p[2] = 0
            i_gift = 1
        else:
            p[0] = 0
            p[1] = 0
            p[2] = 1
            i_gift = 2         
            
        #The player chooses a door
        #i_de = door_decision_1_2()
        i_de = door_desicion_3()
        
        #Monty opens an empty door
        n = rng.random()
        if i_de == 0:
            if n < 0.5:
                i_open = 1
                if i_open == i_gift:
                    i_open = 2
            else:
                i_open = 2
                if i_open == i_gift:
                    i_open = 1
        if i_de == 1:
            if n < 0.5:
                i_open = 0
                if i_open == i_gift:
                    i_open = 2
            else:
                i_open = 2
                if i_open == i_gift:
                    i_open = 0
        if i_de == 2:
            if n < 0.5:
                i_open = 0
                if i_open == i_gift:
                    i_open = 1
            else:
                i_open = 1
                if i_open == i_gift:
                    i_open = 0
                                            
        #The player applies his strategy
        #i_de_final =  strategy_1(i_de) 
        #i_de_final =  strategy_2(i_de, i_gift)
        i_de_final =  strategy_3(i_de, i_gift)
        
        #We check if the player won
        
        if i_de_final == i_gift:
            flag = flag + 1
        
    prob_t.append(flag/Nmax)   
    n_t.append(Nmax)            


plt.figure()
plt.plot(n_t,prob_t)
plt.ylabel("probability")
plt.xlabel("N")
plt.ylim(0,1)






