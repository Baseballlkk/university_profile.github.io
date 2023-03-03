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
t = []
vx = []
vy = []
ax = []
ay = []
x = []
y = []


vx.append(v0*m.cos(theta))
vy.append(v0*m.sin(theta))
ax.append(-(C*rho*A*np.sqrt(vx[0]**2+vy[0]**2)*vx[0])/(2*mass)) 
ay.append(-(g+(C*rho*A*np.sqrt(vx[0]**2+vy[0]**2)*vy[0]))/(2*mass))
x.append(0)
y.append(0)
t.append(0)

# calculate vx,vy
for i in range(1000):
    if y[i]>=0:
        t.append(t[i]+dt)
        x.append(x[i]+vx[i]*dt)
        y.append(y[i]+vy[i]*dt)
        vx.append(vx[i]+ax[i]*dt)
        vy.append(vy[i]+ay[i]*dt)
        ax.append(-0.00259*((vx[i+1]**2+vy[i+1]**2)**(1/2))*vx[i+1])
        ay.append(-9.8-0.00259*((vx[i+1]**2+vy[i+1]**2)**(1/2))*vy[i+1])
    else :
        break
    
print(round(np.amax(x),2))
print(round(np.amax(t),2))
print(round(np.amax(y),2))

# plot picture


plt.plot(x,y,'b:')
plt.xlabel('x')
plt.ylabel('y')
plt.title('y-x')
plt.xticks(np.linspace(0,174,11))
plt.yticks(np.linspace(0,52,11))
plt.show()