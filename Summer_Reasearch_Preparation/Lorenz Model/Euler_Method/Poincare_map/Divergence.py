import numpy as np
from matplotlib import pyplot as plt
import lm 

# running times
loop_time = 1000000

# time interval
dt = 0.001

# array and init
x = np.empty(loop_time+1)
y = np.empty(loop_time+1)
z = np.empty(loop_time+1)
x[0], y[0], z[0]= (0.1, 0.1, 0.1)

inter = []

# running for lorenz model
for i in range(0,100):
    for j in range(loop_time):
        xf, yf, zf = lm.Lorenz(x[j], y[j], z[j])
        x[j+1] = x[j]+ xf*dt
        y[j+1] = y[j]+ yf*dt
        z[j+1] = z[j]+ zf*dt
    # plot picture
    # fig = plt.figure()
    # ax = plt.axes(projection='3d')
    # ax.plot3D(x, y, z, lw = 0.1)

    # ax.set_xlim([np.min(x), np.max(x)])
    # ax.set_ylim([np.min(y), np.max(y)])
    # ax.set_zlim([np.min(z), np.max(z)])

    # plt.title('Lorenz model for 1000000 times')

    # plt.savefig(r'C:\Users\joe51\OneDrive\桌面\profile_ntu\Summer_Reasearch_Preparation\Lorenz Model\Euler_Method\Poincare_map\Lorenz_Model_for 1000000 times.png', dpi = 600)
    # plt.show()
for i in range(loop_time):
    if (x[i+1]*x[i]<=0) :
        inter.append(i)
inter = np.asarray(inter)

dis = np.empty(len(inter)-1)

for i in range(len(inter)-1):
    dis[i] = np.sqrt((x[inter[i]]-x[0])**2+(y[inter[i]]-y[0])**2+(z[inter[i]]-z[0])**2)

for i in range(len(inter)-1):
    div = dis[i+1]/dis[i]
    if div>1:
        
    

