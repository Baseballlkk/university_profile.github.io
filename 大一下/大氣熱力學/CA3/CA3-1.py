# import library
import numpy as np
from matplotlib import pyplot as plt

# set constant
a = 2.53*1e8
b = 5.42*1e3
ep = 0.622
p0 = 1000
Rd = 287
Cp = 1004

# load file
H, P, T, U = np.loadtxt('46810-2018072100.edt.txt', delimiter = ',', usecols = (1, 2, 3, 4), skiprows = 3, unpack = True)

T = T+273.15

# calculate for qv
es = a*np.exp(-b/T)
e = es*U
qv = (ep*e)/(P-(1-ep)*e)

# calculate for potential temp
theta = T*(p0/P)**(Rd/Cp)

# calculate for theta_v
theta_v = T*(1+0.608*qv)*(p0/P)**(Rd/Cp)

# plot the graph of theta_v
fig = plt.figure(figsize = (8,6))

plt.plot(theta_v, H, lw = 0.5)
plt.xlim([326,1016])
plt.ylim([0, np.max(H)+1000])
plt.xticks(np.linspace(326, 1016, 6))
plt.yticks(np.linspace(0, np.max(H)+1000, 11))
plt.title(r'$\theta_v$ - Altitude profile', fontsize = 15)
plt.xlabel('Virtual Potential Temperature [K]', fontsize = 15)
plt.ylabel('Altitude [m]', fontsize = 15)
plt.legend([r'$\theta_v$'])

plt.savefig('Virtual_Potential_Temperature_to_Altitude.png', dpi = 300)
plt.show()

# plot potential temp
fig = plt.figure(figsize = (8,6))
plt.plot(theta_v, H, lw = 0.5, color = 'blue')
plt.plot(theta, H, lw = 0.5, color = 'orange')
plt.xlim([np.min(theta),np.max(theta_v)])
plt.ylim([0, np.max(H)+1000])
plt.xticks(np.linspace(300,1016, 5))
plt.yticks(np.linspace(0, np.max(H)+1000, 11))
plt.title(r'$\theta_v$ & $\theta$- Altitude profile', fontsize = 15)
plt.xlabel('Virtual Potential Temperature [K]', fontsize = 15)
plt.ylabel('Altitude [m]', fontsize = 15)
plt.legend([r'$\theta_v$', r'$\theta$'])

plt.savefig('Virtual_Potential_Temperature_to_Altitude.png', dpi = 300)
plt.show()

# plot the difference
fig = plt.figure(figsize = (8,6))
dif = theta_v-theta
plt.plot(dif, H, lw = 0.5)
plt.xlim([0, 51])
plt.ylim([0, np.max(H)+1000])
plt.xticks(np.linspace(0, 52, 5))
plt.yticks(np.linspace(0, np.max(H)+1000, 11))
plt.title(r'Difference between $\theta_v-\theta$ - Altitude Profile', fontsize = 15)
plt.xlabel('Difference [K]', fontsize = 15)
plt.ylabel('Altitude [m]', fontsize = 15)
plt.legend(['Difference'])
plt.savefig('Difference.png', dpi = 300)
plt.show()