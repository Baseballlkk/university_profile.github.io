# import library
import numpy as np
import matplotlib.pyplot as plt
import math as m

# set initial conditions
mass = 1
v0 = 50
theta = m.radians(45)
C = 0.4
rho = 1.293
A = 0.01
g = 9.8
dt = 0.01

#set vx,vy array
t = np.arange(0.,6.46+dt,dt)
vx = np.zeros(t.shape)
vy = np.zeros(t.shape)
ax = np.zeros(t.shape)
ay = np.zeros(t.shape)
x = np.zeros(t.shape)
y = np.zeros(t.shape)


vx[0] = v0*np.cos(theta)
vy[0] = v0*np.sin(theta)
ax[0] = -(C*rho*A*np.sqrt(vx[0]**2+vy[0]**2)*vx[0])/(2*mass)
ay[0] = -(g+(C*rho*A*np.sqrt(vx[0]**2+vy[0]**2)*vy[0]))/(2*mass)
x[0] = 0
y[0] = 0

# calculate vx,vy
for i in range(646):
    x[i+1] = x[i]+vx[i]*dt
    y[i+1] = y[i]+vy[i]*dt
    vx[i+1] = vx[i]+ax[i]*dt
    vy[i+1] = vy[i]+ay[i]*dt
    ax[i+1] = -0.00259*((vx[i+1]**2+vy[i+1]**2)**(1/2))*vx[i+1]
    ay[i+1] = -9.8-0.00259*((vx[i+1]**2+vy[i+1]**2)**(1/2))*vy[i+1]
print(np.amax(x))
print(np.amax(t))

# plot picture


plt.plot(x,y,'b:')
plt.xlabel('x')
plt.ylabel('y')
plt.title('y-x')
plt.xticks(np.linspace(0,153.53,10))
plt.yticks(np.linspace(0,49.18,10))
plt.show()