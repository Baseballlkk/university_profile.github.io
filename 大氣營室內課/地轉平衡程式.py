# import library
import math as m
import numpy as np
import matplotlib.pyplot as plt

# set constant
rho = 1                                               
omega = 2*(m.pi)/86400                               # period of self rotating
phi = m.radians(90)                                  # assume the latitude is 90 degree*
dt = 10

# establish arrays
t = np.zeros(10000)                                   # array of time
x = np.zeros(10000)                                   # array of x-coordinate
y = np.zeros(10000)                                   # array of y-coordinate
vx = np.zeros(10000)                                  # array of x velocity
vy = np.zeros(10000)                                  # array of y velocity
ax = np.zeros(10000)                                  # array of x acceleration
ay = np.zeros(10000)                                  # array of y acceleration
theta = np.zeros(10000)                               # array of degree of wind
P = np.zeros(10000)

# set initial value 
x[0] = 0
y[0] = 0
vx[0] = 0
vy[0] = 0                                          # im m/s
ax[0] = (-1/rho)*(-1/1000)+2*omega*vy[0]*np.sin(phi)
ay[0] = (-1/rho)*(-1/1000)
t[0] = 0
theta[0] = np.radians(90)

# calculate the data
for i in range(9999):
    t[i+1] = t[i]+dt
    x[i+1] = x[i]+vx[i]*dt
    y[i+1] = y[i]+vy[i]*dt
    vx[i+1] = vx[i]+ax[i]*dt
    vy[i+1] = vy[i]+ay[i]*dt
    dp = -1/1000
    Gy = (-1/rho)*(dp)
    ax[i+1] = 2*omega*vy[i+1]*np.sin(phi)
    ay[i+1] = Gy-2*omega*vx[i+1]*np.sin(phi) 

xmin = np.min(x)
ymin = np.min(y)

xmax = np.max(x)
ymax = np.max(y)

# plot y-x diagram
plt.scatter(x,y,c=t)
plt.xticks(np.linspace(0,xmax+10,11))
plt.yticks(np.linspace(0,ymax+10,11))
plt.xlim([xmin-10,xmax+10])
plt.ylim([ymin-10,ymax+10])
plt.title('trajectory or air parcel in geostatic equilibrium', fontsize=30)
plt.xlabel('x')
plt.ylabel('y')
plt.show()