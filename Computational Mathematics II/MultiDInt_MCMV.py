#Multi-D integration using MCMV method

import numpy as np

rng = np.random.default_rng()

def sphere(a):
    r = 0
    for i in range(len(a)):
        r = r + a[i]**2
    if(r <= 1):
        return 1.;
    else:
        return 0.;

d = 10
    
V = 2**d
N = 10**6

I = 0

for i in range(N):
    a0 = 2*rng.random((d))-1     
    I = I + sphere(a0)
    
I = V/N*I

print("I=",I) 
    
