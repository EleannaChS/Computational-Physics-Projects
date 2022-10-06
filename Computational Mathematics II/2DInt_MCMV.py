#2D integration using MCMV method

import numpy as np

rng = np.random.default_rng()

def circle(x,y):
    if(x**2+y**2 <= 1):
        return 1.;
    else:
        return 0.;
    
V = 4.
N = 10**6

I = 0

for i in range(N):
    x0 = 2*rng.random()-1   
    y0 = 2*rng.random()-1   
    I = I + circle(x0, y0)
    
I = V/N*I

print("I=",I) 
    
