# import library
import numpy as np
import matplotlib.pyplot as plt
import math as m

# set constant
h = 11000 # the condition is setted at tropopause
T = 15.04-0.00649*h
p = 101.29*(((T+273.15)/288.08)**5.256)
rho = p/(0.2869*(T+273.15))
omega = (2*m.pi)/86400
P2 = 200
P1 = 300
dt = 1 # in s
R = 1000 # in meter
G = (-1/rho)*((P2-P1)*100/R)
phi = m.radians(60)

# set array
t = np.zeros(10000000)
x = np.zeros(10000000)
y = np.zeros(10000000)
vx = np.zeros(10000000)
vy = np.zeros(10000000)
ax = np.zeros(10000000)
ay = np.zeros(10000000)
theta = np.zeros(10000000)
P = np.zeros(10000000)

# set initial condition
t[0] = 0
x[0] = 0
y[0] = 0
vx[0] = 0
vy[0] = 75 # in m/s
theta[0] = m.radians(90)
ax[0] = 2*omega*(((vx[0]**2)+(vy[0]**2))**(1/2))*np.sin(phi)
ay[0] = G
P[0]=300

# calculate for track of air parcel
for i in range(1000000):
    if ay[i]>=0:
        P
        t[i+1] = t[i]+dt
        x[i+1] = x[i]+vx[i]*dt+(1/2)*ax[i]*(dt**2)
        y[i+1] = y[i]+vy[i]*dt+(1/2)*ay[i]*(dt**2)
        vx[i+1] = vx[i]+ax[i]*dt
        vy[i+1] = vy[i]+ay[i]*dt
        theta[i+1] = np.arctan(vy[i+1]/vx[i+1])
        ax[i+1] = 2*omega*(((vx[i+1]**2)+(vy[i+1]**2))**(1/2))*np.sin(phi)*np.sin(theta[i+1])
        ay[i+1] = G-2*omega*(((vx[i+1]**2)+(vy[i+1]**2))**(1/2))*np.sin(phi)*np.cos(theta[i+1])
        print(i,round(np.degrees(theta[i]),2),round(t[i],2),round(x[i],2),round(y[i],2),round(vx[i],2),round(vy[i],2),round(ax[i],2),round(ay[i],2))
    else :
        break

# plot the track
plt.plot(x,y,'b')
plt.xticks(np.linspace(0,2,21))
plt.yticks(np.linspace(0,200,21))
plt.xlim([0,2])
plt.ylim([0,200])
plt.xlabel('x')
plt.ylabel('y')
plt.title('x-y')
plt.show()