# import lab
import numpy as np
import matplotlib.pyplot as plt

# load file
H, P, T, U = np.loadtxt('46810-2018072100.edt.txt',dtype = 'float' , delimiter = ',', skiprows=3, usecols=(1,2,3,4), unpack = True)

# calculate for Kelvin degree
TK = T+273.15

# define the max and min of each variable
hmax = np.max(H)
pmax = np.max(P)
tmax = np.max(TK)
umax = np.max(U)

hmin = np.min(H)
pmin = np.min(P)
tmin = np.min(TK)
umin = np.min(U)

# plot the graph of temperature to altitude
plt.plot(TK, H, linewidth=0.5)
plt.axhline(y = hmax, xmin = 0, xmax = 1, color = 'red')
plt.xlim([tmin-1, tmax+1])
plt.ylim([hmin-10, hmax+1000])
plt.xlabel('Temperature [K]', fontsize = 15)
plt.ylabel('Altitude [m]', fontsize = 15)
plt.xticks(np.linspace(tmin-1, tmax+1, 11))
plt.yticks(np.linspace(0,hmax+10, 21))
plt.title('Temperature Change as the Altitude increasing', fontsize = 15)
plt.legend(['TK'])

plt.savefig('Temperature Change as the Altitude increasing.png')
plt.show()


# plot the graph of temperature to pressure
plt.plot(TK, P, linewidth=0.5)
plt.axhline(y = pmin, xmin = 0, xmax = 1, color = 'red')
plt.xlim([tmin-1, tmax+1])
plt.ylim([pmax,0])
plt.xlabel('Temperature [K]', fontsize = 15)
plt.ylabel('Pressure [hPa]', fontsize = 15)
plt.xticks(np.linspace(tmin-1, tmax+1, 11))
plt.yticks(np.linspace(pmax,0, 21))
plt.title('Temperature Change as the Pressure decreasing', fontsize = 15)
plt.legend(['TK'])

plt.savefig('Temperature Change as the Pressure decreasing.png')
plt.show()


# plot the graph of relative humodity to altitude
plt.plot(U, H, linewidth=0.5)
plt.axhline(y = hmax, xmin = 0, xmax = 1, color = 'red')
plt.xlim([umin-1, umax+1])
plt.ylim([hmin-10, hmax+1000])
plt.xlabel('Relative Humidity [%]', fontsize = 15)
plt.ylabel('Altitude [m]', fontsize = 15)
plt.xticks(np.linspace(0, 100, 11))
plt.yticks(np.linspace(0,hmax+10, 21))
plt.title('Relative Humidity Change as the Altitude increasing', fontsize = 15)
plt.legend(['Relative Humidity'])

plt.savefig('Relative Humidity Change as the Altitude increasing.png')
plt.show()


# plot the graph of relative humidity to pressure
plt.plot(U, P, linewidth=0.5)
plt.axhline(y = pmin, xmin = 0, xmax = 1, color = 'red')
plt.xlim([0, 100])
plt.ylim([pmax, 0])
plt.xlabel('Relative Humidity [%]', fontsize = 15)
plt.ylabel('Pressure [hPa]', fontsize = 15)
plt.xticks(np.linspace(0, 100, 11))
plt.yticks(np.linspace(pmax,0, 21))
plt.title('Relative Humidity Change as the Pressure decreasing', fontsize = 15)
plt.legend(['Relative Humidity'])

plt.savefig('Relative Humidity Change Change as the Pressure decreasing.png')
plt.show()
