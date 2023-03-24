import numpy as np

# announce variables
nb = 2
nt = 4

# set array
T = np.zeros(nt)
t1 = np.zeros(nt)
t2 = np.zeros(nt)

# set picture
for i in range(nt):
    t1[i] = 10**(3+i)
    t2[i] = 10**(3-i)
    if t1[i] ==t2[i]:
        t2[i] = 0
    T[i] = t1[i]+t2[i]
    T[i] = round(T[i],0)

    print(T[i])
