# CA0 for themodynamic 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as ma
import copy as cp

# set constant
P0=1000
Rd=287
Cp=1004



# open file
file = input('Inout the file name:') 
P, H, T = np.loadtxt(file,skiprows=4, usecols=(0,1,2), unpack=True)

TK = T + 273.15

iv = []

# calculate for potential
theta=TK*(P0/P)**(Rd/Cp)

pmax=np.max(P)

for i in range(1,np.shape(TK)[0]):
    if (TK[i]>TK[i-1]):
        iv.append(TK[i])



print(TK)
print(iv)


# plot graph of pressure
plt.plot(TK, P, 'b')
plt.plot(theta, P, 'r')
plt.legend(['Temperature','$\Theta$'])
plt.ylim([pmax,0])
plt.yticks(np.linspace(1000,0,11))
plt.title('Temperature(B) and Potential(R) as Pressure Decrease', size=20)
plt.xlabel('Temperature & Potential Energy (K)', size=15)
plt.ylabel('Pressure in hPa', size=15)
plt.axhline(y=888.0, xmin = 0, xmax=1)
plt.axhline(y=864.0, xmin = 0, xmax=1)
plt.fill_between(TK, y1=888, y2 = 864, color = 'c')
plt.fill_between(theta, y1=888, y2 = 864, color = 'c')
plt.axhline(y=731.0, xmin = 0, xmax=1)
plt.axhline(y=704.0, xmin = 0, xmax=1)
plt.fill_between(TK, y1=731.0, y2 = 704.0, color = 'y')
plt.fill_between(theta, y1=731.0, y2 = 704.0, color = 'y')
plt.axhline(y=100.0, xmin = 0, xmax=1)
plt.axhline(y=72.6, xmin = 0, xmax=1)
plt.fill_between(TK, y1=100.0, y2 = 72.6, color = 'g')
plt.fill_between(theta, y1=100.0, y2 = 72.6, color = 'g')
plt.grid()
plt.savefig('Temperature_&_Potential_Temperature_Pressure.png')
plt.show()


# plot graph of altitude
plt.plot(TK, H, 'b')
plt.plot(theta, H, 'r')
plt.legend(['Temperature','$\Theta$'])
plt.ylim({0,20000})
plt.title('Temperature(B) and Potential(R) as Altitude Increase', size = 20)
plt.xlabel('Temperature & Potential Energy (K)', size=15)
plt.ylabel('Altitude in meter', size=15)
plt.grid()
plt.axhline(y = 1162, xmin = 0, xmax = 1)
plt.axhline(y = 1397, xmin = 0, xmax = 1)
plt.fill_between(TK, y1 = 1162, y2 = 1397, color = 'c')
plt.fill_between(theta, y1 = 1162, y2 = 1397, color = 'c')
plt.axhline(y=2808.0, xmin = 0, xmax=1)
plt.axhline(y=3122.0, xmin = 0, xmax=1)
plt.fill_between(TK, y1=2808.0, y2 = 3122.0, color = 'y')
plt.fill_between(theta, y1=2808.0, y2 = 3122.0, color = 'y')
plt.axhline(y=16680.0, xmin = 0, xmax=1)
plt.axhline(y=18522.0, xmin = 0, xmax=1)
plt.fill_between(TK, y1=16680.0, y2 = 18522.0, color = 'g')
plt.fill_between(theta, y1=16680.0, y2 = 18522.0, color = 'g')
plt.savefig('Temperature_&_Potential_Temperature_Altitude.png')
plt.show()
