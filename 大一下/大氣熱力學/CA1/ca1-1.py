# import lab
import numpy as np
import matplotlib.pyplot as plt

# load file
H, P, T, U = np.loadtxt('46810-2018072100.edt.txt',dtype = 'float' , delimiter = ',', skiprows=3, usecols=(1,2,3,4), unpack = True)

# calculate for Kelvin degree
TK = T+273.15

# find tropopause 
for i in range(len(H)):
    if H[i] == 15512:
        print(P[i])

# define the max and min of each variable
hmax = np.max(H)
pmax = np.max(P)
tmax = np.max(TK)
umax = np.max(U)

hmin = np.min(H)
pmin = np.min(P)
tmin = np.min(TK)
umin = np.min(U)

# compare between temp and rh as altitude
f, ax=plt.subplots(1, 2, sharey='row') 
ax[0].plot(TK,H, linewidth=0.5)
ax[0].axhline(y = hmax, xmin = 0, xmax = 1, color = 'red')
ax[0].axhline(y = 15512, xmin = 0, xmax = 1, color = 'green')
ax[0].set_xlim([tmin-1, tmax+1])
ax[0].set_ylim([hmin-10, hmax+1000])
ax[0].set_xlabel('Temperature [K]', fontsize = 15)
ax[0].set_ylabel('Altitude [m]', fontsize = 15)
ax[0].set_xticks(np.linspace(tmin-1, tmax+1, 11))
ax[0].set_yticks(np.linspace(0,hmax+10, 21))
ax[0].set_title('Temperature Change as the Altitude increasing', fontsize = 15)
plt.legend(['TK'])

ax[1].plot(U, H, linewidth=0.5)
ax[1].axhline(y = hmax, xmin = 0, xmax = 1, color = 'red')
ax[1].axhline(y = 15511, xmin = 0, xmax = 1, color = 'green')
ax[1].set_xlim([umin-1, umax+1])
ax[1].set_ylim([hmin-10, hmax+1000])
ax[1].set_xlabel('Relative Humidity [%]', fontsize = 15)
ax[1].set_ylabel('Altitude [m]', fontsize = 15)
ax[1].set_xticks(np.linspace(0, 100, 11))
ax[1].set_yticks(np.linspace(0,hmax+10, 21))
ax[1].set_title('Relative Humidity Change as the Altitude increasing', fontsize = 15)
plt.legend(['Relative Humidity'])

plt.savefig('Temperature  Relative Humidity Change as the Altitude increasing.png')
plt.show()

# compare between temp and rh as pressure
f, ax=plt.subplots(1, 2, sharey='row') 
ax[0].plot(TK, P, linewidth=0.5)
ax[0].axhline(y = pmin, xmin = 0, xmax = 1, color = 'red')
ax[0].axhline(y = 122.2, xmin = 0, xmax = 1, color = 'green')
ax[0].set_xlim([tmin-1, tmax+1])
ax[0].set_ylim([pmax,0])
ax[0].set_xlabel('Temperature [K]', fontsize = 15)
ax[0].set_ylabel('Pressure [hPa]', fontsize = 15)
ax[0].set_xticks(np.linspace(tmin-1, tmax+1, 11))
ax[0].set_yticks(np.linspace(pmax,0, 21))
ax[0].set_title('Temperature Change as the Pressure decreasing', fontsize = 15)
ax[0].legend(['TK'])

ax[1].plot(U, P, linewidth=0.5)
ax[1].axhline(y = pmin, xmin = 0, xmax = 1, color = 'red')
ax[1].axhline(y = 122.2, xmin = 0, xmax = 1, color = 'green')
ax[1].set_xlim([0, 100])
ax[1].set_ylim([pmax, 0])
ax[1].set_xlabel('Relative Humidity [%]', fontsize = 15)
ax[1].set_ylabel('Pressure [hPa]', fontsize = 15)
ax[1].set_xticks(np.linspace(0, 100, 11))
ax[1].set_yticks(np.linspace(pmax,0, 21))
ax[1].set_title('Relative Humidity Change as the Pressure decreasing', fontsize = 15)
plt.legend(['Relative Humidity'])

plt.savefig('Temperature  Relative Humidity Change as the Pressure decreasing.png')
plt.show()

# compare between altitude and pressure at temp
f, ax=plt.subplots(1, 2, sharex='row') 
ax[0].plot(TK,H, linewidth=0.5)
ax[0].axhline(y = hmax, xmin = 0, xmax = 1, color = 'red')
ax[0].axhline(y = 15512, xmin = 0, xmax = 1, color = 'green')
ax[0].set_xlim([tmin-1, tmax+1])
ax[0].set_ylim([hmin-10, hmax+1000])
ax[0].set_xlabel('Temperature [K]', fontsize = 15)
ax[0].set_ylabel('Altitude [m]', fontsize = 15)
ax[0].set_xticks(np.linspace(tmin-1, tmax+1, 11))
ax[0].set_yticks(np.linspace(0,hmax+10, 21))
ax[0].set_title('Temperature Change as the Altitude increasing', fontsize = 15)
plt.legend(['TK'])

ax[1].plot(TK, P, linewidth=0.5)
ax[1].axhline(y = pmin, xmin = 0, xmax = 1, color = 'red')
ax[1].axhline(y = 122.2, xmin = 0, xmax = 1, color = 'green')
ax[1].set_xlim([tmin-1, tmax+1])
ax[1].set_ylim([pmax,0])
ax[1].set_xlabel('Temperature [K]', fontsize = 15)
ax[1].set_ylabel('Pressure [hPa]', fontsize = 15)
ax[1].set_xticks(np.linspace(tmin-1, tmax+1, 11))
ax[1].set_yticks(np.linspace(pmax,0, 21))
ax[1].set_title('Temperature Change as the Pressure decreasing', fontsize = 15)
ax[1].legend(['TK'])

plt.savefig('Compare of altitude & pressure by the temperature')
plt.show()

# compare between altitude and pressure at rh
f, ax=plt.subplots(1, 2, sharex='row')
ax[0].plot(U, H, linewidth=0.5)
ax[0].axhline(y = hmax, xmin = 0, xmax = 1, color = 'red')
ax[0].axhline(y = 15511, xmin = 0, xmax = 1, color = 'green')
ax[0].set_xlim([umin-1, umax+1])
ax[0].set_ylim([hmin-10, hmax+1000])
ax[0].set_xlabel('Relative Humidity [%]', fontsize = 15)
ax[0].set_ylabel('Altitude [m]', fontsize = 15)
ax[0].set_xticks(np.linspace(0, 100, 11))
ax[0].set_yticks(np.linspace(0,hmax+10, 21))
ax[0].set_title('Relative Humidity Change as the Altitude increasing', fontsize = 15)
plt.legend(['Relative Humidity'])

ax[1].plot(U, P, linewidth=0.5)
ax[1].axhline(y = pmin, xmin = 0, xmax = 1, color = 'red')
ax[1].axhline(y = 122.2, xmin = 0, xmax = 1, color = 'green')
ax[1].set_xlim([0, 100])
ax[1].set_ylim([pmax, 0])
ax[1].set_xlabel('Relative Humidity [%]', fontsize = 15)
ax[1].set_ylabel('Pressure [hPa]', fontsize = 15)
ax[1].set_xticks(np.linspace(0, 100, 11))
ax[1].set_yticks(np.linspace(pmax,0, 21))
ax[1].set_title('Relative Humidity Change as the Pressure decreasing', fontsize = 15)
plt.legend(['Relative Humidity'])

plt.show()