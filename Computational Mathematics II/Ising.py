#the 1D Ising model

import numpy as np
from matplotlib import pyplot as plt

rng = np.random.default_rng()

Ttab = [1,10,20]

N = 10000
for k in range(4):
    T = Ttab[k];
    beta = 1./T
    
    spins = np.random.choice([1,-1],N)
    max_steps = 500
    
    M = np.zeros(max_steps)
    counter = 0
    
    for step in range(max_steps):
        x = np.random.randint(1,N-1)
        
        init_spin = spins[x]
        fin_spin = -spins[x]
           
        init_energy = -(init_spin*spins[x-1] + init_spin*spins[x+1])
        fin_energy = -(fin_spin*spins[x-1] + fin_spin*spins[x+1])
        dE = fin_energy - init_energy
        
        p = np.exp(-beta*dE)
        r = rng.uniform() 
        
        if r < p:
            spins[x] = fin_spin
            counter = counter + 1
        M[step] = np.sum(spins)
    
    plt.figure()
    time_steps=np.arange(1,max_steps+1,1)
    plt.plot(time_steps,M, label='T={}'.format(T))
    plt.xlabel("Iterations")
    plt.ylabel("Magnetization")
    plt.legend()
    #plt.ylim([-1,1])
    
    # plt.figure()
    # time_steps=np.arange(1,max_steps+1,1)
    # plt.plot(time_steps,M, label='T={}'.format(T))
    # plt.xlabel("Iterations")
    # plt.ylabel("Magnetization")
    # plt.legend()
