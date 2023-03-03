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
t = np.zeros(1000)
vx = np.zeros(1000)
vy = np.zeros(1000)
ax = np.zeros(1000)
ay = np.zeros(1000)
x = np.zeros(1000)
y = np.zeros(1000)
theta = np.zeros(1000)

for j in range(0,91):
 theta[j] = j
 vx[0] = v0*m.cos(m.radians(theta[j]))
 vy[0] = v0*m.sin(m.radians(theta[j]))
 ax[0] = -(C*rho*A*np.sqrt(vx[0]**2+vy[0]**2)*vx[0])/(2*mass)
 ay[0] = -(g+(C*rho*A*np.sqrt(vx[0]**2+vy[0]**2)*vy[0]))/(2*mass)
 x[0] = 0
 y[0] = 0
 t[0] = 0
 
 # calculate vx,vy
 for i in range(1000):
    if y[i]>=(-0.01):
         t[i+1]=t[i]+dt
         x[i+1]=x[i]+vx[i]*dt
         y[i+1]=y[i]+vy[i]*dt
         vx[i+1]=vx[i]+ax[i]*dt
         vy[i+1]=vy[i]+ay[i]*dt
         ax[i+1]=-0.00259*((vx[i+1]**2+vy[i+1]**2)**(1/2))*vx[i+1]
         ay[i+1]=-9.8-0.00259*((vx[i+1]**2+vy[i+1]**2)**(1/2))*vy[i+1]
    else :
        break
 print(theta[j],round(np.amax(x),2),round(np.amax(t),2),round(np.amax(y),2))
