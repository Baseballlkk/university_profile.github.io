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
Gd = -9.8

# load file
H, P, T, U = np.loadtxt(r"C:\Users\joe51\OneDrive\桌面\profile_ntu\大一下\大氣熱力學\CA3\46810-2018072100.edt.txt", delimiter = ',', usecols = (1, 2, 3, 4), skiprows = 3, unpack = True)

T = T+273.15

# calculate for qv
es = a*np.exp(-b/T)
e = es*U
qv = (ep*e)/(P-(1-ep)*e)

# calculate for potential temp
theta = T*(p0/P)**(Rd/Cp)

# calculate for theta_v
theta_v = T*(1+0.608*qv)*(p0/P)**(Rd/Cp)

'''
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

plt.savefig('Virtual_Potential_Temperature_andtheta_to_Altitude.png', dpi = 300)
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

# lapse rate of surrounding
def lapse(arr1, arr2):
    arr = np.zeros(len(arr1)-1)
    for i in range(len(arr1)-1):
        diff_1 = 0
        diff_2 = 0
        diff_1 = arr1[i+1]-arr1[i]
        diff_2 = arr2[i+1]-arr2[i]
        if (diff_2 != 0):
            arr[i] = diff_1/diff_2
        else :
            arr[i] = np.nan
    return arr

def ma(array, num):
    arrayout = np.zeros(len(array)-2*num)
    for i in range(num, len(array)-num):
        t = 0
        for j in range(i-num, i+num+1):
            if array[j]!=np.nan:
                t += array[j]
            arrayout[i-num] = t/(2*num+1)

    return arrayout

lapse_rate = lapse(T, H)
ma_lapse_rate = ma(lapse_rate, 300)
ma_altitude = ma(H, 300)

fig = plt.figure(figsize = (8,6))
plt.plot(-9.8-ma_lapse_rate, ma_altitude[:(len(ma_altitude)-1)], lw = 0.5)
plt.axvline(x = -9.8, ymin = 0, ymax = 1, lw = 0.5, color = 'orange')
plt.xlim([-9.82, -9.78])
plt.ylim([0, np.max(H)+1000])
plt.xticks(np.linspace(-9.82, -9.78, 5))
plt.yticks(np.linspace(0, np.max(H)+1000, 11))
plt.xlabel('Difference between lapse rate [K/Km]', fontsize = 15)
plt.ylabel('Altitude [m]', fontsize = 15)
plt.title('Difference between lapse rate vs. Altitude', fontsize = 15)
plt.show()
'''

# 3
epsilon = 0.622
Rd = 287
g = 9.80

Tv = (1+((1/epsilon)-1))*T
Tv_add = Tv+10

dz = np.empty(18)
dz_add = np.empty(18)
Pf = np.empty(18)

def find_nearest(array, value):
    idxarray = np.empty(len(array))
    for i in range(len(array)):
        idxarray[i] = abs(array[i]-value)
    idx = np.argmin(idxarray)
    return idx

# method 1: fing the nearest point
for i in range(18):
    Pf[i] = 1000-50*i
    dz[i] = -(Rd/(2*g))*np.log((Pf[i]-10)/Pf[i])*(Tv[find_nearest(P, (Pf[i]-10))]+Tv[find_nearest(P, Pf[i])])
    dz_add[i] = -(Rd/(2*g))*np.log((Pf[i]-10)/Pf[i])*(Tv[find_nearest(P, (Pf[i]-10))]+Tv[find_nearest(P, Pf[i])]+20)

'''
plt.scatter(dz, Pf, s = 10)
plt.scatter(dz_add, Pf, s = 10)
plt.xlim([np.min(dz), np.max(dz_add)])
plt.ylim([np.max(P), np.min(Pf)-10])
plt.xticks(np.linspace(140, 695, 6))
plt.yticks(Pf)
plt.xlabel('Physical Depth [m]', fontsize = 15)
plt.ylabel('Pressure [hPa]', fontsize = 15)
plt.title('Physical Depth of 10 hPa per 50 hPa by Nearest Point', fontsize = 15)
plt.legend([r'$T_v$', r'$T_v+10$'], loc = 'lower right')

plt.savefig('Physical_Depth_by_1.png', dpi = 300)
plt.show()

plt.plot(dz_add-dz, Pf, lw = 0.5)
plt.scatter(dz_add-dz, Pf, s = 10)
plt.xlim([np.min(dz_add-dz), np.max(dz_add-dz)])
plt.ylim([np.max(P), np.min(Pf)-10])
plt.xticks(np.linspace(2.5, 20.5, 5))
plt.yticks(Pf)
plt.xlabel('Differnce of Physical Depth [m]', fontsize = 15)
plt.ylabel('Pressure [hPa]', fontsize = 15)
plt.title('Physical Depth Difference of 10 hPa per 50 hPa by Nearest Point', fontsize = 15)

plt.savefig('Physical_Depth_Difference_by_1.png', dpi = 300)
plt.show()
'''
# method 2: Interpolar method
dz2 = np.empty(18)
dz_add2 = np.empty(18)
Pf2 = np.empty(18)

def interpolate(array1, array2, value):
    ip = (array2[find_nearest(array1, value)+1]-array2[find_nearest(array1, value)])/(array1[find_nearest(array1, value)+1]-find_nearest(array1, value)+1)*(value-find_nearest(array1, value)+1)+array2[find_nearest(array1, value)]
    return ip

for i in range(18):
    Pf2[i] = 1000-50*i
    dz2[i] = -(Rd/(2*g))*np.log((Pf2[i]-10)/Pf2[i])*(interpolate(P, Tv, (Pf2[i]-10))+interpolate(P, Tv, Pf2[i]))
    dz_add2[i] = -(Rd/(2*g))*np.log((Pf2[i]-10)/Pf2[i])*(interpolate(P, Tv, (Pf2[i]-10))+interpolate(P, Tv, Pf2[i])+20)
'''
plt.scatter(dz2, Pf2, s = 10)
plt.scatter(dz_add2, Pf2, s = 10)
plt.xlim([np.min(dz2), np.max(dz_add2)])
plt.ylim([np.max(P), np.min(Pf2)-10])
plt.xticks(np.linspace(140, 695, 6))
plt.yticks(Pf2)
plt.xlabel('Physical Depth [m]', fontsize = 15)
plt.ylabel('Pressure [hPa]', fontsize = 15)
plt.title('Physical Depth of 10 hPa per 50 hPa by Interpolation', fontsize = 15)
plt.legend([r'$T_v$', r'$T_v+10$'], loc = 'lower right')

plt.savefig('Physical_Depth_by_2.png', dpi = 300)
plt.show()

plt.plot(dz_add2-dz2, Pf, lw = 0.5)
plt.scatter(dz_add2-dz2, Pf, s = 10)
plt.xlim([np.min(dz_add2-dz2), np.max(dz_add2-dz2)])
plt.ylim([np.max(P), np.min(Pf2)-10])
plt.xticks(np.linspace(2.5, 20.5, 5))
plt.yticks(Pf)
plt.xlabel('Differnce of Physical Depth [m]', fontsize = 15)
plt.ylabel('Pressure [hPa]', fontsize = 15)
plt.title('Physical Depth Difference of 10 hPa per 50 hPa by Interpolation', fontsize = 15)

plt.savefig('Physical_Depth_Difference_by_2.png', dpi = 300)
plt.show()
'''


# Difference between the two method
err_dz = (dz2-dz)/dz2*100
err_dz_add = (dz_add2-dz_add)/dz_add2*100
print(err_dz)
print(err_dz_add)


plt.scatter(err_dz, Pf, s = 10)
plt.plot(err_dz, Pf, lw = 0.5)
plt.scatter(err_dz_add, Pf, s = 10)
plt.plot(err_dz_add, Pf, lw = 0.5)
plt.xlim([np.min(err_dz), 0.01])
plt.ylim([np.max(P), np.min(Pf2)-10])
plt.xticks(np.linspace(-0.05, 0., 6))
plt.yticks(Pf)
plt.xlabel('Relative Error [%]', fontsize = 15)
plt.ylabel('Pressure', fontsize = 15)
plt.title('Relative Error between the Two Method', fontsize = 15)
plt.legend([r'err_$Tv$', '',r'err_$T_v+10$', ''], loc = 'best')
plt.savefig('savefig.png')
plt.show()