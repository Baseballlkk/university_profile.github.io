# set lib
import numpy as np
import matplotlib.pyplot as plt

# set constant
nmax = 10000

# set array
P = np.random.rand(nmax-1)
X = np.zeros(nmax)
Y = np.zeros(nmax)

# set initial condition
X[0] = 0
Y[0] = 0

# calculate
for i in range(nmax-1):
    if 0.00<=P[i]<0.01:
        A = 0.000
        B = 0.000
        C = 0.000
        D = 0.000
        E = 0.000
        F = -0.012
    elif 0.01<=P[i]<0.86:
        A = 0.845
        B = 0.035
        C = 0.000
        D = -0.030
        E = 0.820
        F = 1.600
    elif 0.86<=P[i]<0.93:
        A = 0.200
        B = -0.260
        C = 0.000
        D = 0.255
        E = 0.245
        F = 0.290
    elif 0.93<=P[i]<=1.00:
        A = -0.150
        B = 0.240
        C = 0.000
        D = 0.250
        E = 0.200
        F = 0.680

    X[i+1] = A*X[i]+B*Y[i]+C
    Y[i+1] = D*X[i]+E*Y[i]+F

# plot
plt.plot(X,Y,'go')
plt.savefig('midb.png')
plt.show()
