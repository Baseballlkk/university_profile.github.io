# import library
import numpy as np
import matplotlib.pyplot as plt
import math as m

# set initial conditions
mass = 1
v0 = 50
C = 0.4
rho = 1.293
A = 0.01
g = 9.8
dt = 0.01

#set vx,vy array
t = np.arange(0.,6.45+dt,dt)
vx = np.zeros(t.shape)
vy = np.zeros(t.shape)
ax = np.zeros(t.shape)
ay = np.zeros(t.shape)
x = np.zeros(t.shape)
y = np.zeros(t.shape)
theta = np.linspace(0,90,91)
MAX = np.zeros(91)
x[0] = 0
y[0] = 0

for i in range(91):
    vx[0] = v0*np.cos(theta[i])
    vy[0] = v0*np.sin(theta[i])
    ax[0] = -(C*rho*A*np.sqrt(vx[0]**2+vy[0]**2)*vx[0])/(2*mass)
    ay[0] = -(g+(C*rho*A*np.sqrt(vx[0]**2+vy[0]**2)*vy[0]))/(2*mass)
 
    # calculate vx,vy

    for j in range():
        while y[j]>=0:
         x[j+1] = x[j]+vx[j]*dt
         y[j+1] = y[j]+vy[j]*dt
         vx[j+1] = vx[j]+ax[j]*dt
         vy[j+1] = vy[j]+ay[j]*dt
         ax[j+1] = -0.00259*((vx[j+1]**2+vy[j+1]**2)**(1/2))*vx[j+1]
         ay[j+1] = -9.8-0.00259*((vx[j+1]**2+vy[j+1]**2)**(1/2))*vy[j+1]

    A = np.amax(x)
    MAX[i] = A
 
print(np.amax(MAX))
print(np.argmax(MAX))
print(theta[np.argmax(MAX)])
