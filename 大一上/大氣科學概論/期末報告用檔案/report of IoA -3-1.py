# import lib
import numpy as np
import math as m
import matplotlib.pyplot as plt

# setting constant
h = 11000                                            # the height of tropopause
T = 15.04-0.00649*h
p = 101.29*(((T+273.15)/288.08)**5.256)
rho = p/(0.2869*(T+273.15))                          # in kg/m3
print(rho)
p = p*1000                                           # unit in Pa
omega = 2*(m.pi)/86400                               # period of self rotating
phi = m.radians(60)                                  # assume the latitude is 45 degree
pc = -1                                               # assume the rate of pressure change is 1 Pa/m
dt = 1

# setting array of changing variables
x = []                                   # array of x-coordinate
y = []                                   # array of y-coordinate
vx = []                                  # array of x velocity
vy = []                                  # array of y velocity
ax = []                                  # array of x acceleration
ay = []                                  # array of y acceleration
t = []                                   # array of time
theta = []                               # array of degree of wind
P = []                                   # array of pressure

# setting initial condition of variables
x.append(0)
y.append(0)
vx.append(0)
vy.append(1)                                           # im m/s
ax.append((-1/rho)*(-1)+2*omega*((vx[0]**2+vy[0]**2)**(1/2))*m.sin(phi))
ay.append((-1/rho)*(-1))
t.append(0)
theta.append(m.radians(90))
P.append(p)

# counting the data
for i in range(999):
    if ay[i]>0:
        x.append(x[i]+vx[i]*dt)
        y.append(y[i]+vy[i]*dt)
        vx.append(vx[i]+ax[i]*dt)
        vy.append(vy[i]+ay[i]*dt)
        theta.append(m.atan(vy[i+1]/vx[i+1]))
#        P[i+1] = P[i]+pc*vy[i]*dt
        dp = pc*vy[i]*dt
        Gy = (-1/rho)*(dp/(y[i+1]-y[i]))
        ax.append(2*omega*((vx[i+1]**2+vy[i+1]**2)**(1/2))*np.sin(phi)*np.sin(theta[i]))
        ay.append(Gy-2*omega*((vx[i+1]**2+vy[i+1]**2)**(1/2))*np.sin(phi)*np.cos(theta[i]))
        print(i,round(np.degrees(theta[i]),2),round(x[i],2),round(y[i],2),round(ax[i],2),round(ay[i],2))
    else:
        break

# plot y-x diagram
plt.plot(x,y,'b:')
plt.xticks(np.linspace(0,1000,11))
plt.yticks(np.linspace(0,2000,11))
plt.xlim([0,1000])
plt.ylim([0,2000])
plt.title('y-x')
plt.xlabel('x')
plt.ylabel('y')
plt.show()