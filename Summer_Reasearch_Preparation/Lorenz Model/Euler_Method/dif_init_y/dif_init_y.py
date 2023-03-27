import numpy as np
from matplotlib import pyplot as plt
import lm 




# running times
loop_time = 1000000

dt = 0.001

x = np.empty(loop_time+1)
y = np.empty(loop_time+1)
z = np.empty(loop_time+1)


# running for lorenz model
for i in range(41):

    x[0], y[0], z[0]= (0.1, dt*i, 0.1)
    for j in range(loop_time):
        xf, yf, zf = lm.Lorenz(x[j], y[j], z[j])
        x[j+1] = x[j]+ xf*dt
        y[j+1] = y[j]+ yf*dt
        z[j+1] = z[j]+ zf*dt
    # plot picture
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot3D(x, y, z, lw = 0.1)

    ax.set_xlim([np.min(x), np.max(x)])
    ax.set_ylim([np.min(y), np.max(y)])
    ax.set_zlim([np.min(z), np.max(z)])

    # ani = animation.FuncAnimation(fig, animate, frames = 100, interval = 50, blit = True)

    lt = str(loop_time)
    plt.title('Lorenz_Model_for x = 0.1, y = '+str(dt*i)+', z = 0.1')

    plt.savefig(r'C:\Users\joe51\OneDrive\桌面\profile_ntu\Summer_Reasearch_Preparation\Lorenz Model\dif_init_y\Lorenz_Model_for x = 0.1, y = '+str(dt*i)+', z = 0.1 .png', dpi = 300)
    # plt.show()

