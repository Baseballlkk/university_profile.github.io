# import lib
import numpy as np
import matplotlib.pyplot as plt
import Gauss
import Gauss_Seidel as gs
import Jacobi as ja
import datetime

# set constant value
dt = 60
dz = 0.05
M = 5e-7*dt*(dz**(-2))
TOL = 0.05
gr = int(1e4)

# load .txt file
z, T_init = np.loadtxt('T_ini.txt', delimiter = ',', unpack=True, skiprows = 1)
time, T_s = np.loadtxt('T_s.txt', delimiter = ',', unpack = True, skiprows = 1)

#################################################Topic 1#######################################################
'''
# input array size
m = int(input("Input the size of square array: "))
arrA = np.zeros((m, m))
arrX = np.zeros(m)
arrAX = np.zeros(m)
arrXN = np.zeros(m)
dif = np.zeros(m)

for i in range(m):
    for j in range(m):
        print("Input arrA[", i,",",  j, "]")
        arrA[i, j] = float(input())

for i in range(m):
    print("Input arrAX[", i,"]")
    arrAX[i] = float(input())

for i in range(m):
    print("Input arrX[", i,"]")
    arrX[i] = float(input())

## process of Gauss-Seidel method
startgs = datetime.datetime.now()
for i in range(gr):
    arrXN = gs.GS(m, arrA, arrAX, arrX)
    dif = np.abs((arrXN-arrX)/arrX)
    if np.sum(np.where(dif<=TOL, 0, 1)) == 0:
        break
    else :
        arrX = arrXN
endgs = datetime.datetime.now()
print(endgs-startgs)



## process of Jacobi method
l = int(input("Input the size of square array: "))
arrAgs = np.zeros((l, l))
arrXgs = np.zeros(l)
arrAXgs = np.zeros(l)
arrXNgs = np.zeros(l)
arrXngs = np.zeros(l)
difgs = np.zeros(l)

for i in range(l):
    for j in range(l):
        print("Input arrA[", i,",",  j, "]")
        arrAgs[i, j] = float(input())

for i in range(l):
    print("Input arrAX[", i,"]")
    arrAXgs[i] = float(input())

for i in range(l):
    print("Input arrX[", i,"]")
    arrXgs[i] = float(input())

## process of Jacobi method
startja = datetime.datetime.now()
for i in range(gr):
    arrXNgs = ja.Ja(arrAgs, arrAXgs, arrXgs)
    if np.sum(np.where(arrXNgs == 0, 1, 0)) == 0:
        difgs = np.abs((arrXNgs-arrXgs)/arrXgs)
    if np.sum(np.where(difgs<=TOL, 0, 1)) == 0:
        break
    else :
        arrXgs = arrXNgs
endja = datetime.datetime.now()
print(endja-startja)
################################################Topic 2####################################################
'''
# cal n
n = len(z)

# build array
A = np.zeros((n, n))

## for element of array
e1 = -M
e2 = 1+2*M
e3 = 1+M

for i in range(n):
    for j in range(n):
        if i==j:
            A[i,j] = e2
            if (j-1)<0:
                pass
            else :
                A[i, j-1] = e1
            if (j+1) == n:
                A[i, j] = e3
            else :
                A[i, j+1] = e1


Xge = np.zeros(n)
X5ge = np.zeros(len(time))
X10ge = np.zeros(len(time))
X20ge = np.zeros(len(time))
X50ge = np.zeros(len(time))
X100ge = np.zeros(len(time))
XNge = np.zeros(n)

X5ge[0] = T_init[0]
X10ge[0] = T_init[1]
X20ge[0] = T_init[3]
X50ge[0] = T_init[9]
X100ge[0] = T_init[19]

XNge = T_init
# loop for calculating
start1 = datetime.datetime.now()
for i in range(len(time)-1):
    XNge[0] += M*T_s[i+1]
    XNge= Gauss.gauss_elimination(A, XNge)
    X5ge[i+1] = XNge[0]
    X10ge[i+1] = XNge[1]
    X20ge[i+1] = XNge[3]
    X50ge[i+1] = XNge[9]
    X100ge[i+1] = XNge[19]

end1 = datetime.datetime.now()
print('GE = ', end1-start1)

fig = plt.figure(figsize = (8,6))
plt.plot(np.linspace(0, 24, 1440), T_s)
plt.plot(np.linspace(0, 24, 1440), X5ge)
plt.plot(np.linspace(0, 24, 1440), X10ge)
plt.plot(np.linspace(0, 24, 1440), X20ge)
plt.plot(np.linspace(0, 24, 1440), X50ge)
plt.plot(np.linspace(0, 24, 1440), X100ge)
plt.xlim([0, 24])
plt.ylim([20, 30])
plt.xticks(np.linspace(0, 24, 7))
plt.yticks(np.linspace(20, 30, 6))
plt.grid()
plt.xlabel('Time [hr]', fontsize = 15)
plt.ylabel('Temperature [K]', fontsize = 15)
plt.title('Soil Tmeperature of 5 cm, 10 cm, 20 cm, 50 cm, 100 cm', fontsize = 15)
plt.legend(['surface', '5 cm', '10 cm', '20 cm', '50 cm', '100 cm'])

plt.savefig('T_ge.png')
plt.show()
#################################################################################

X = np.zeros(n)
X5 = np.zeros(len(time))
X10 = np.zeros(len(time))
X20 = np.zeros(len(time))
X50 = np.zeros(len(time))
X100 = np.zeros(len(time))
XN = np.zeros(n)

X5[0] = T_init[0]
X10[0] = T_init[1]
X20[0] = T_init[3]
X50[0] = T_init[9]
X100[0] = T_init[19]

XN = T_init
# loop for calculating
start2 = datetime.datetime.now()
for i in range(len(time)-1):
    XN[0] += M*T_s[i+1]
    XN= gs.GS(n, A, XN, X)
    X5[i+1] = XN[0]
    X10[i+1] = XN[1]
    X20[i+1] = XN[3]
    X50[i+1] = XN[9]
    X100[i+1] = XN[19]
end2 = datetime.datetime.now()
print('GS = ', end2-start2)

fig = plt.figure(figsize = (8,6))
plt.plot(np.linspace(0, 24, 1440), T_s)
plt.plot(np.linspace(0, 24, 1440), X5)
plt.plot(np.linspace(0, 24, 1440), X10)
plt.plot(np.linspace(0, 24, 1440), X20)
plt.plot(np.linspace(0, 24, 1440), X50)
plt.plot(np.linspace(0, 24, 1440), X100)
plt.xlim([0, 24])
plt.ylim([20, 30])
plt.grid()
plt.xticks(np.linspace(0, 24, 7))
plt.yticks(np.linspace(20, 30, 6))
plt.xlabel('Time [hr]', fontsize = 15)
plt.ylabel('Temperature [K]', fontsize = 15)
plt.title('Soil Tmeperature of 5 cm, 10 cm, 20 cm, 50 cm, 100 cm', fontsize = 15)
plt.legend(['surface', '5 cm', '10 cm', '20 cm', '50 cm', '100 cm'])

plt.savefig('T_gs.png')
plt.show()
#####################################################################################################################

Xgs = np.zeros(n)
X5gs = np.zeros(len(time))
X10gs = np.zeros(len(time))
X20gs = np.zeros(len(time))
X50gs = np.zeros(len(time))
X100gs = np.zeros(len(time))
XNgs = np.zeros(n)
Xngs = np.zeros(n)

X5gs[0] = T_init[0]
X10gs[0] = T_init[1]
X20gs[0] = T_init[3]
X50gs[0] = T_init[9]
X100gs[0] = T_init[19]

XNgs = T_init
# 
# loop for calculating
start3 = datetime.datetime.now()
for i in range(len(time)-1):
    XNgs[0] += M*T_s[i+1]
    XNgs= ja.jacobi(A, XNgs, Xgs)
    X5gs[i+1] = XNgs[0]
    X10gs[i+1] = XNgs[1]
    X20gs[i+1] = XNgs[3]
    X50gs[i+1] = XNgs[9]
    X100gs[i+1] = XNgs[19]
end3 = datetime.datetime.now()
print('Ja = ', end3-start3)

fig = plt.figure(figsize = (8,6))
plt.plot(np.linspace(0, 24, 1440), T_s)
plt.plot(np.linspace(0, 24, 1440), X5gs)
plt.plot(np.linspace(0, 24, 1440), X10gs)
plt.plot(np.linspace(0, 24, 1440), X20gs)
plt.plot(np.linspace(0, 24, 1440), X50gs)
plt.plot(np.linspace(0, 24, 1440), X100gs)
plt.xlim([0, 24])
plt.ylim([20, 30])
plt.grid()
plt.xticks(np.linspace(0, 24, 7))
plt.yticks(np.linspace(20, 30, 6))
plt.xlabel('Time [hr]', fontsize = 15)
plt.ylabel('Temperature [K]', fontsize = 15)
plt.title('Soil Tmeperature of 5 cm, 10 cm, 20 cm, 50 cm, 100 cm', fontsize = 15)
plt.legend(['surface', '5 cm', '10 cm', '20 cm', '50 cm', '100 cm'])

plt.savefig('T_Ja.png')
plt.show()