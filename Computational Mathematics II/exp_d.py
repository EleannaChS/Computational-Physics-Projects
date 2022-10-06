import numpy as np
from statsmodels.graphics.gofplots import qqplot
import matplotlib.pyplot as plt
from scipy.stats import expon

n = 100000

rng = np.random.default_rng()
x = rng.uniform(0,1,n)

l = 1

y = -np.log(1-x)/l

x_plot = np.linspace(0,7)

plt.figure(figsize = (8,8))
plt.hist(y, bins=50, density=True, label="invesre function data") #probabilith density
plt.plot(x_plot,np.exp(-x_plot), label="exp(-x)")
plt.legend(loc="upper right")


qqplot(y,expon,fit=True,line="45")
plt.show()