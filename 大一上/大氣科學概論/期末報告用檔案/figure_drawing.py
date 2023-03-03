# import library
import numpy as np
import matplotlib.pyplot as plt
import test_fig as tf

# set array
x = np.zeros(88)
y = np.zeros(88)
vx = np.zeros(88)
t = np.zeros(88)
lat = np.linspace(4,90,88)
# calculate x,y,u-wind
for i in range(4,91):
    x[i-4],y[i-4],vx[i-4],t[i-4] = tf.testgeof(i)

# draw figure
plt.plot(lat,x,'b:')
plt.title('The maximum distance (parallel to isobar) as latitude increase')
plt.xlabel('latitude')
plt.ylabel('maximum distance (parallel to isobar) [m]')
plt.xticks(np.linspace(0,90,7))
plt.yticks(np.linspace(0,49000000,6))
plt.xlim([0,90])
plt.ylim([0,49000000])
plt.show()

plt.plot(lat,y,'b:')
plt.title('The maximum distance (vertical to isobar) as latitude increase')
plt.xlabel('latitude')
plt.ylabel('maximum distance (vertical to isobar) [m]')
plt.xticks(np.linspace(0,90,7))
plt.yticks(np.linspace(0,32000000,11))
plt.xlim([0,90])
plt.ylim([0,32000000])
plt.show()

plt.plot(lat,vx,'b:')
plt.title('The maximum u-wind velocity as latitude increase')
plt.xlabel('latitude')
plt.ylabel('maximum u-wind velocity [m/s]')
plt.xticks(np.linspace(0,90,7))
plt.yticks(np.linspace(0,600,5))
plt.xlim([0,90])
plt.ylim([0,600])
plt.show()

plt.plot(lat,t,'b:')
plt.title('The equilibrium time as latitude increase')
plt.xlabel('latitude')
plt.ylabel('equilibrium time [s]')
plt.xticks(np.linspace(0,90,7))
plt.yticks(np.linspace(0,125000,5))
plt.xlim([0,90])
plt.ylim([0,125000])
plt.show()