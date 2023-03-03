# import library
import numpy as np
import matplotlib.pyplot as plt
import math as mt

# setting parameters
m = 200
m_a = 10
k = 197192
k_a = 9859.6
c = 502.4
c_a = 62.8
F_0 = 5000
omega = 31
dt = 0.01

# setting array
t = np.zeros(501)  # simulate with time interval 0.01 seconds
x = np.zeros(t.shape)
v = np.zeros(t.shape)
a = np.zeros(t.shape)

tw = np.zeros(t.shape)
xw = np.zeros(t.shape)
vw = np.zeros(t.shape)
aw = np.zeros(t.shape)

# initialize value of arrays
t[0] = 0
x[0] = 0
v[0] = 0
a[0] = 0
t[1] = 0.01
x[1] = 0
v[1] = 0
a[1] = 0

tw[0] = 0
xw[0] = 0
vw[0] = 0
aw[0] = 0
tw[1] = 0.01
xw[1] = 0
vw[1] = 0
aw[1] = 0

# calculate for equation(with m_a)
for i in range(2,501):
    t[i+1] = t[i]+dt
    m*a[i+1]+(c_a+c)*v[i+1]+(m_a/(m+m_a)*k_a+k)*x[i+1]=F_0*mt.sin(omega*t[i])


# calculate for equation( without m_a)
for i in range(501):
    tw[i+1] = t[i]+dt