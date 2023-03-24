import numpy as np

# set constaant
A = 0.845
B = 0.035
C = 0.000
D = -0.030
E = 0.820
F = 1.600

# set numpy array
n = np.zeros(10)
X = np.zeros(10)
Y = np.zeros(10)

# receive value from input
x = input('input X0:')
x = float(x)
X[0] = x

y = input('input Y0:')
y = float(y)
Y[0] = y

n[0] = 0

# claculate
for i in range(9):
    n[i+1] = i+1
    X[i+1] = A*X[i]+B*Y[i]+C
    Y[i+1] = D*X[i]+E*Y[i]+F

# savetext
data = np.array(list(zip(n,X,Y)))
np.savetxt('mida.txt',data,comments='#',header = ' n X    Y    ',fmt='  %1.1d %5.3f %5.3f')