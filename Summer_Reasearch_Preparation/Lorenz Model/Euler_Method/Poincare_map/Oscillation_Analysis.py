# import lib
import numpy as np
import matplotlib.pyplot as plt

# loop time
loop_time = 100

# interval time
dt = 0.01

# set constant
rho = 28
sigma = 10
beta = 8/3

# array setting
x = np.zeros(loop_time+1)
y = np.zeros(loop_time+1)
z = np.zeros(loop_time+1)
t = np.zeros(loop_time+1)

x[0], y[0], z[0], t[0] = (0.1, 0.1, 0.1, 0)

# define function of lorenz
def lorenz(a, b, c, sigma = 10, rho = 28, beta = 8/3):
    da = sigma*(b-a)
    db = a*(rho-c)-b
    dc = a*b-beta*c    
    return da, db, dc
    
# define Eulerian Method
def euler(x, y, z, dx, dy, dz, dt):
    x_f = x + dx*dt
    y_f = y + dy*dt
    z_f = z + dz*dt
    return x_f, y_f, z_f

def moving_average(x, w):
    return np.convolve(x, np.ones(w), 'valid') / w

# conduct process
for i in range(loop_time):
    dx, dy, dz = lorenz(x[i], y[i], z[i])
    x[i+1], y[i+1], z[i+1] = euler(x[i], y[i], z[i], dx, dy, dz, dt)
    t[i+1] = t[i] + dt



fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D(x, y, z, lw = 0.1)

ax.set_xlim([np.min(x), np.max(x)])
ax.set_ylim([np.min(y), np.max(y)])
ax.set_zlim([np.min(z), np.max(z)])
plt.show()

# plot oscillation
fig, ax = plt.subplots(3, 1, sharex = 'col')

ax[0].plot(t, x, lw = 0.5, color = 'blue')
ax[0].axhline(y = 0, xmin = 0, xmax = 1, linestyle = '-', lw = 0.5)
# ax[0].set_xlim([np.nanmin(t), np.nanmax(t)])
ax[0].set_ylim([-20, 20])
# ax[0].set_xlabel('Time [s]', fontsize = 15)
ax[0].set_ylabel('x', fontsize = 15)
ax[0].set_title('x(b), y(g), z(p)-t diagram', fontsize = 15)

ax[1].plot(t, y, lw = 0.5, color = 'green')
ax[1].axhline(y = 0, xmin = 0, xmax = 1, linestyle = '-', lw = 0.5)
# ax[1].set_xlim([np.nanmin(t), np.nanmax(t)])
ax[1].set_ylim([-20, 20])
# ax[1].set_xlabel('Time [s]', fontsize = 15)
ax[1].set_ylabel('y', fontsize = 15)

ax[2].plot(t, z, lw = 0.5, color = 'purple')
ax[2].axhline(y = 0, xmin = 0, xmax = 1, lw = 0.5)
ax[2].set_xlim([np.nanmin(t), np.nanmax(t)])
ax[2].set_ylim([0, 40])
ax[2].set_xlabel('Time [s]', fontsize = 15)
ax[2].set_ylabel('z', fontsize = 15)

plt.savefig('Oscillation.png')
plt.show()

