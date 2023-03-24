# import lib
import numpy as np
import matplotlib.pyplot as plt

# load data
H, P, T, U = np.loadtxt(r"C:\Users\joe51\OneDrive\桌面\profile_ntu\大一下\大氣熱力學\CA3\46810-2018072100.edt.txt", delimiter = ',', usecols = (1, 2, 3, 4), skiprows = 3, unpack = True)

T = T+273.15

# set constant
g = 9.8
Cp = 1004
P0 = 1000
Rd = 287

# topic 1
## draw potential temperature & static energy
Sd = Cp*T+g*H
Pt = T*(P0/P)**(Rd/Cp)

figure = plt.figure(figsize = (8,6))
plt.plot(Sd, H, lw = 0.5, color = 'blue')
plt.plot(Cp*Pt, H, lw = 0.5, color = 'orange')
plt.axhline(y = 15397, xmin = 0, xmax = 1)
plt.axhline(y = np.max(H), xmin = 0, xmax = 1, lw = 0.1)
plt.xticks(np.linspace(np.min(Sd), np.max(Cp*Pt), 5))
plt.yticks(np.linspace(0, np.max(H)+1000, 11))
plt.xlim([np.min(Sd), np.max(Cp*Pt)])
plt.ylim([0, np.max(H)+1000])
plt.xlabel('Static Energy & Cp*Potential Temperature [J/kg]', fontsize = 15)
plt.ylabel('Altitude', fontsize = 15)
plt.title('Static Energy Proifle - Altitude', fontsize = 15)
plt.legend([r'$S_d$', r'$C_p*\theta$'])

plt.savefig('Static_Energy.png', dpi = 600)
plt.show()

fig = plt.figure(figsize = (8,6))
plt.plot(Sd-Cp*Pt, H, lw = 0.5)
plt.axhline(y = 15397, xmin = 0, xmax = 1)
plt.axhline(y = np.max(H), xmin = 0, xmax = 1, lw = 0.1)
plt.xticks(np.linspace(-443040, 280, 5))
plt.yticks(np.linspace(0, np.max(H)+1000, 11))
plt.xlim([-443040, 280])
plt.ylim([0, np.max(H)+1000])
plt.xlabel('Difference of Static Energy & Cp*Potential Temperature [J/kg]', fontsize = 15)
plt.ylabel('Altitude', fontsize = 15)
plt.title('Difference of Static Energy & Cp*Potential Temperature Proifle - Altitude', fontsize = 15)

plt.savefig('Dif_Static_Energy.png', dpi = 600)
plt.show()

# topic 2
## calculate dry parcel
lapse_rate = 9.8/1000

## creat array
Td = np.empty(len(T))
Ptd = np.empty(len(T))
Sdd = np.empty(len(T))

## set initial value
Td[0] = T[0]

## calculate for Td
for i in range(len(Td)-1):
    Td[i+1] = Td[i]-lapse_rate*(H[i+1]-H[i])
## calculate for Ptd
Ptd = Td*(P0/P)**(Rd/Cp)

## calculate for Sdd
Sdd = Cp*Td+g*H

## plot T & Td
fig = plt.figure(figsize = (8,6))
plt.plot(T, H, lw = 0.5)
plt.plot(Td, H, lw = 0.5, color = 'green')
plt.axhline(y = 15397, xmin =0, xmax = 1, lw = 0.5, color = 'blue')
plt.fill_between(Td, y1 = 0, y2 = 644, color = 'pink')
plt.xticks(np.linspace(140 ,305, 4))
plt.yticks(np.linspace(0, np.max(H), 11))
plt.xlim([140, 305])
plt.ylim([0, 16000])
plt.xlabel('Temperatuer [K]', fontsize = 15)
plt.ylabel('Altitude [m]', fontsize = 15)
plt.title('Temperature for real & dry air profile', fontsize = 15)
plt.legend(['T', r'$T_d$'])

plt.savefig('Temp_of_dry.png', dpi = 600)
plt.show()


## potential temperature
fig = plt.figure(figsize = (8,6))
plt.plot(Pt, H, lw = 0.5)
plt.plot(Ptd, H, lw = 0.5, color = 'green')
plt.axhline(y = 15397, xmin =0, xmax = 1, lw = 0.5, color = 'blue')
plt.xticks(np.linspace(240,400, 5))
plt.yticks(np.linspace(0, np.max(H), 11))
plt.xlim([240,400])
plt.ylim([0, 16000])
plt.xlabel('Potential Temperatuer [K]', fontsize = 15)
plt.ylabel('Altitude [m]', fontsize = 15)
plt.title('Potential Temperature for real & dry air profile', fontsize = 15)
plt.legend([r'$\theta$', r'$\theta_d$'])

plt.savefig('PTemp_of_dry.png', dpi = 600)
plt.show()

# emphisize low
fig = plt.figure(figsize = (8,6))
plt.plot(Pt, H, lw = 0.5)
plt.plot(Ptd, H, lw = 0.5, color = 'green')
plt.axhline(y = 636, xmin = 0, xmax = 1, lw = 0.5, color = 'orange')
plt.xticks(np.linspace(300, 310, 6))
plt.yticks(np.linspace(0, 1000, 11))
plt.xlim([300,310])
plt.ylim([0, 1000])
plt.xlabel('Potential Temperatuer [K]', fontsize = 15)
plt.ylabel('Altitude [m]', fontsize = 15)
plt.title('Potential Temperature for real & dry air profile', fontsize = 15)
plt.legend([r'$\theta$', r'$\theta_d$'])

plt.savefig('PTemp_of_dry_low.png', dpi = 600)
plt.show()
print(Ptd[0])
## dry static
fig = plt.figure(figsize = (8,6))

plt.plot(Sdd, H, lw = 0.5, color = 'green')
# plt.xticks(np.linspace(300, 310, 6))
# plt.yticks(np.linspace(0, 1000, 11))
# plt.xlim([300,310])
# plt.ylim([0, 1000])
plt.xlabel('Static Energy [J/kg]', fontsize = 15)
plt.ylabel('Altitude [m]', fontsize = 15)
plt.title('Satic Energy for real & dry air profile', fontsize = 15)
plt.legend([r'$S_d$', r'$S_{dd}$'])

plt.savefig('Sdd.png', dpi = 600)
plt.show()

# plt.plot(Sd, H, lw = 0.5)
# topic 3