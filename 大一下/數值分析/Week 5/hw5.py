# import lib
import numpy as np
import matplotlib.pyplot as plt
import Gauss

# set constant value
M = 5e-7
dt = 60
dz = 0.05

# load .txt file
z, T_init = np.loadtxt('T_ini.txt', delimiter = ',', unpack=True, skiprows = 1)
time, T_s = np.loadtxt('T_s.txt', delimiter = ',', unpack = True, skiprows = 1)

# cal n
n = len(z)

# build array
A = np.zeros((n, n))

## for element of array
e1 = -M
e2 = 1+2*M
e3 = 1+M

for i in range(n):
    for j in range(n):
        if i==j:
            A[i,j] = e2
            if (j-1)<0:
                pass
            else :
                A[i, j-1] = e1
            if (j+1) == n:
                A[i, j] = e3
            else :
                A[i, j+1] = e1


X = np.zeros(n)
X5 = np.zeros(len(time))
X10 = np.zeros(len(time))
X20 = np.zeros(len(time))
X50 = np.zeros(len(time))
X100 = np.zeros(len(time))

X5[0] = T_init[0]
X10[0] = T_init[1]
X20[0] = T_init[3]
X50[0] = T_init[9]
X100[0] = T_init[19]


# loop for calculating
for i in range(len(time)-1):
    T_init = Gauss.Gauss_elim(n, A, T_init, X)
    T_init[0] += M*T_s[i+1]
    X5[i+1] = T_init[0]
    X10[i+1] = T_init[1]
    X20[i+1] = T_init[3]
    X50[i+1] = T_init[9]
    X100[i+1] = T_init[19]


fig = plt.figure(figsize = (8,6))
plt.plot(np.linspace(0, 24, 1440), T_s)
plt.plot(np.linspace(0, 24, 1440), X5)
plt.plot(np.linspace(0, 24, 1440), X10)
plt.plot(np.linspace(0, 24, 1440), X20)
plt.plot(np.linspace(0, 24, 1440), X50)
plt.plot(np.linspace(0, 24, 1440), X100)

plt.show()