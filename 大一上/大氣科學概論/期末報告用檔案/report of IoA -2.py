# import lib
import numpy as np
import math as m
import matplotlib.pyplot as plt

# setting constant
#h = 11000                                            # the height of tropopause
#T = 15.04-0.00649*h
#p = 101.29*(((T+273.15)/288.08)**5.256)
#rho = p/(0.2869*(T+273.15))                          # in kg/m3
rho = 1                                               
#p = p*1000                                           # unit in Pa
omega = 2*(m.pi)/86400                               # period of self rotating
phi = m.radians(60)                                  # assume the latitude is 45 degree*
pc = -1                                              # assume the rate of pressure change is 1 Pa/m*
dt = 10

# setting array of changing variables
x = np.zeros(10000)                                   # array of x-coordinate
y = np.zeros(10000)                                   # array of y-coordinate
vx = np.zeros(10000)                                  # array of x velocity
vy = np.zeros(10000)                                  # array of y velocity
ax = np.zeros(10000)                                  # array of x acceleration
ay = np.zeros(10000)                                  # array of y acceleration
t = np.zeros(10000)                                   # array of time
theta = np.zeros(10000)                               # array of degree of wind
P = np.zeros(10000)                                   # array of pressure    
# add nan
# setting initial condition of variables
x[0] = 0
y[0] = 0
vx[0] = 0
vy[0] = 0                                          # im m/s
ax[0] = (-1/rho)*(-1)+2*omega*vy[0]*np.sin(phi)
ay[0] = (-1/rho)*(-1)
t[0] = 0
theta[0] = np.radians(90)
#P[0] = p

# counting the data
for i in range(9999):
#    if ay[i]>=0:
        t[i+1] = t[i]+dt
        x[i+1] = x[i]+vx[i]*dt
        y[i+1] = y[i]+vy[i]*dt
        vx[i+1] = vx[i]+ax[i]*dt
        vy[i+1] = vy[i]+ay[i]*dt
        dp = -1/1000
        Gy = (-1/rho)*(dp)
        ax[i+1] = 2*omega*vy[i+1]*np.sin(phi)
        ay[i+1] = Gy-2*omega*vx[i+1]*np.sin(phi)
        print(i,round(x[i],2),round(y[i],2),round(ax[i],2),round(ay[i],2))
#    else:
#        break
# set if vy<0

# plot y-x diagram
#plt.plot(x,y,'b:')
#plt.plot(y,x,'b:')
plt.scatter(x,y,c=t)
plt.xticks(np.linspace(0,164500,11))
plt.yticks(np.linspace(0,200000,11))
plt.xlim([0,164500])
plt.ylim([0,69000])
plt.title('y-x')
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('reprot_of_introduction_of_atmospheric_science_at_lat_60.png')
plt.show()