# import library
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

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

Tv = (1+(1/ep-1)*qv)*T

def find_nearest(array, value):
    idxarray = np.empty(len(array))
    for i in range(len(array)):
        idxarray[i] = abs(array[i]-value)
    idx = np.argmin(idxarray)
    return idx
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



# plot dry air
fig = plt.figure(figsize = (8,6))
plt.plot(theta_v-theta, H, lw = 0.5)
plt.xlim([np.min(theta_v-theta),np.max(theta_v-theta)])
plt.ylim([0, np.max(H)+1000])
plt.xticks(np.linspace(np.min(theta_v-theta),np.max(theta_v-theta), 5))
plt.yticks(np.linspace(0, np.max(H)+1000, 11))
plt.title(r'$\theta_v - \theta$- Altitude profile', fontsize = 15)
plt.xlabel(r'Difference between $\theta_v - \theta$ [K]', fontsize = 15)
plt.ylabel('Altitude [m]', fontsize = 15)

plt.savefig('Difference_between_Virtual_Potential_Temperature_and_theta_to_Altitude.png', dpi = 300)
plt.show()


'''
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
            arr[i] = -diff_1/diff_2
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
time =int(input('Input times: '))

lapse_rate = lapse(T, H)
ma_lapse_rate = ma(lapse_rate, time)
ma_altitude = ma(H, time)



fig = plt.figure(figsize = (8,6))
plt.axvline(x = 9.8, ymin = 0, ymax = 1, lw = 0.5, color = 'green')
plt.plot(9.8-ma_lapse_rate*1000, ma_altitude[:(len(ma_altitude)-1)], lw = 0.5)
plt.xlim([np.min(9.8-ma_lapse_rate*1000), np.max(9.8-ma_lapse_rate*1000)])
plt.ylim([0, np.max(H)+1000])
plt.xticks(np.linspace(0, 20, 5))
plt.yticks(np.linspace(0, np.max(H)+1000, 11))
plt.xlabel('Difference between lapse rate [K/Km]', fontsize = 15)
plt.ylabel('Altitude [m]', fontsize = 15)
plt.title('Difference between lapse rate with smooth average 100 times vs. Altitude', fontsize = 15)
plt.savefig('Difference between lapse rate with smooth average 100 times vs. Altitude.png', dpi = 300)
plt.show()

fig = plt.figure(figsize = (8,6))

for i in range(len(ma_lapse_rate)):
    if (ma_lapse_rate[i]*1000) <= 2:
        plt.axhline(y = H[i], xmin = 0, xmax = 1, color = 'red', lw = 0.5)
        print(H[i])
        break
plt.plot(ma_lapse_rate*1000, ma_altitude[:(len(ma_altitude)-1)], lw = 0.5)
plt.axvline(x = 0, ymin = 0, ymax = 1, lw = 0.5, color = 'green')
plt.xlim([np.min(ma_lapse_rate*1000), np.max(ma_lapse_rate*1000)])
plt.ylim([0, np.max(H)+1000])
plt.xticks(np.linspace(-9.5, 9.5, 5))
plt.yticks(np.linspace(0, np.max(H)+1000, 11))
plt.xlabel('lapse rate [K/Km]', fontsize = 15)
plt.ylabel('Altitude [m]', fontsize = 15)
plt.title('lapse rate with smooth average 100 times vs. Altitude', fontsize = 15)
plt.savefig(' lapse rate with smooth average 100 times vs. Altitude.png', dpi = 300)
plt.show()
'''
# 3
epsilon = 0.622
Rd = 287
g = 9.80

Tv = (1+0.608*qv)*T
Tv_add = Tv+10

dz = np.empty(18)
dz_add = np.empty(18)
Pf = np.empty(18)



# method 1: fing the nearest point

for i in range(18):
    Pf[i] = 1000-50*i
    dz_sub = Tv[find_nearest(P, Pf[i]):(find_nearest(P, (Pf[i]-10)))]
    dz[i] = (Rd/g)*np.log((P[find_nearest(P, Pf[i])])/(P[find_nearest(P, (Pf[i]-10))]))*np.nanmean(dz_sub)
    # dz[i] = (Rd/g)*np.log(Pf[i]/(Pf[i]-10))*np.mean(dz_sub)
    dz_add_sub = Tv_add[find_nearest(P, Pf[i]):(find_nearest(P, (Pf[i]-10))+1)]
    dz_add[i] = (Rd/(g))*np.log((P[find_nearest(P, Pf[i])])/(P[find_nearest(P, (Pf[i]-10))]))*(np.nanmean(dz_add_sub))
    # dz_add[i] = (Rd/(g))*np.log(Pf[i]/(Pf[i]-10))*(np.mean(dz_add_sub))

plt.scatter(dz, Pf, s = 10)
plt.scatter(dz_add, Pf, s = 10)
plt.xlim([np.min(dz), np.max(dz_add)])
plt.ylim([np.max(P), np.min(Pf)-10])
plt.xticks(np.linspace(100, 440, 5))
plt.yticks(Pf)
plt.xlabel('Physical Depth [m]', fontsize = 15)
plt.ylabel('Pressure [hPa]', fontsize = 15)
plt.title('Physical Depth by Nearest Point', fontsize = 15)
plt.legend([r'$T_v$', r'$T_v+10$'], loc = 'lower right')

plt.savefig('Physical_Depth_by_1.png', dpi = 300)
plt.show()

plt.plot(dz_add-dz, Pf, lw = 0.5)
plt.scatter(dz_add-dz, Pf, s = 10)
plt.xlim([np.min(dz_add-dz), np.max(dz_add-dz)])
plt.ylim([np.max(P), np.min(Pf)-10])
plt.xticks(np.linspace(2.8, 20.2, 4))
plt.yticks(Pf)
plt.xlabel('Difference of Physical Depth [m]', fontsize = 15)
plt.ylabel('Pressure [hPa]', fontsize = 15)
plt.title('Physical Depth Difference by Nearest Point', fontsize = 15)

plt.savefig('Physical_Depth_Difference_by_1.png', dpi = 300)
plt.show()

# method 2: Interpolar method
dz2 = np.empty(18)

def interpolate(array1, array2, value):
    if array1[find_nearest(array1, value)]<value:
        ip = (array2[find_nearest(array1, value)+1]-array2[find_nearest(array1, value)])/(array1[find_nearest(array1, value)+1]-array1[find_nearest(array1, value)])*(value-array1[find_nearest(array1, value)])+array2[find_nearest(array1, value)]
    
    elif array1[find_nearest(array1, value)] == value:
        ip = array2[find_nearest(array1, value)]
    else :
        ip = (array2[find_nearest(array1, value)]-array2[find_nearest(array1, value)-1])/(array1[find_nearest(array1, value)]-array1[find_nearest(array1, value)-1])*(value-array1[find_nearest(array1, value)-1])+array2[find_nearest(array1, value)-1]

    return ip

for i in range(18):
    dz2[i] = interpolate(P, H, (Pf[i]-10))-interpolate(P, H, (Pf[i]))
print(dz)
print(dz2)

plt.scatter(dz2, Pf, s = 10)
plt.xlim([np.min(dz2), np.max(dz2)])
plt.ylim([np.max(P), np.min(Pf)-10])
plt.xticks(np.linspace(80, 420, 5))
plt.yticks(Pf)
plt.xlabel(' Real Physical Depth [m]', fontsize = 15)
plt.ylabel('Pressure [hPa]', fontsize = 15)
plt.title('Real Physical Depth ', fontsize = 15)

plt.savefig('Physical_Depth.png', dpi = 300)
plt.show()

# error between the real and near point
err = (dz-dz2)/(dz2)*100

print(err)
plt.scatter(err, Pf, s = 10)
plt.xlim([np.min(err), np.max(err)])
plt.ylim([np.max(P), np.min(Pf)-10])
plt.xticks(np.linspace(-2, 14.2, 4))
plt.yticks(Pf)
plt.xlabel(' Difference of Physical Depth [%]', fontsize = 15)
plt.ylabel('Pressure [hPa]', fontsize = 15)
plt.title('Difference of Physical Depth between near point and real ', fontsize = 15)

plt.savefig('Difference_Physical_Depth.png', dpi = 300)
plt.show()
'''