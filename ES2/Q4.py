import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

xrange = (0,10)


#function of interest
def func(x):
    return np.cos(x)**2

#'normalise' for the range we're looking at
normalization_factor, error = quad(func, *xrange)

def pdf(x):
    return func(x)/normalization_factor


# get the max-value in y
from scipy.optimize import brute
f = lambda x: -pdf(x)
x = brute(f, [xrange])
print(x)
ymax = -f( x[0] )
print(ymax)

#algo
def gen_accept_reject(size=1):
    res = []
    while len(res)<size:
        a = np.random.uniform(*xrange)
        b = np.random.uniform(0,ymax)
        y = pdf(a)
        if y > ymax:
            print('Some issue: as y larger than ymax')
        if b <= y:
            res.append(a)
    return res


#plot results
v=gen_accept_reject(10000)
x_ax=np.linspace(*xrange,100)
plt.hist(v, range=xrange, bins=100, density=True)
plt.plot(x_ax,pdf(x_ax))
plt.show()