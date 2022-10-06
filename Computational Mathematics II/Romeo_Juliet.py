#Romeo and Juliet want to meet
#Each one delays from 0 to 1hr
#When each arrives, waits 15min and then leaves
#What is the probability they meet

import numpy as np
import matplotlib.pyplot as plt 

rng = np.random.default_rng()

#Test of the random number generator
#test = rng.random((100,1))
#test_x = np.linspace(0, 1, 100)
#plt.figure
#plt.scatter(test_x,test)

probs = []
its = []

for nmax in range(1,1000):
    flag = 0
    for i in range(nmax):
        
        r = rng.random()
        j = rng.random()
        
        d = abs(r-j)
        
        if d < 0.25:
            flag = flag + 1
        else:
            flag = flag + 0    
            
    #print("The probability of the meeting is: ", flag/nmax)        
    probs.append(flag/nmax)
    its.append(nmax)
    
plt.figure()
plt.plot(its,probs)
plt.ylabel("probability")
plt.xlabel("N")
plt.ylim(0,1)
    