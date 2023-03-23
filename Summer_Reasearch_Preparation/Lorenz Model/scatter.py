import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
from PIL import Image
import lm

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def func(i):
    ax.clear()
    loop_time = 1000000+100000*i

    dt = 0.001

    x = np.empty(loop_time+1)
    y = np.empty(loop_time+1)
    z = np.empty(loop_time+1)
    x[0], y[0], z[0]= (1e-2, 1e-3, 1e-4)

    for j in range(loop_time):
        xf, yf, zf = lm.Lorenz(x[j], y[j], z[j])
        x[j+1] = x[j]+ xf*dt
        y[j+1] = y[j]+ yf*dt
        z[j+1] = z[j]+ zf*dt
    
    ax.set_xlim([np.min(x), np.max(x)])
    ax.set_ylim([np.min(y), np.max(y)])
    ax.set_zlim([np.min(z), np.max(z)])
    ax.view_init(elev=30, azim=45)
    lt = str(loop_time)
    ax.set_title('Lorenz model for '+ lt +' times')
    ax.plot3D(x, y, z, lw = 0.1)

ani = animation.FuncAnimation(fig, func, frames=20, interval=100, repeat=True)
ani.save('lorenz_model.gif', fps=10, savefig_kwargs={'transparent': True}, writer='imagemagick')

# compress the .gif file using Pillow
with Image.open('lorenz_model.gif') as im:
    new_frames = []
    for frame in range(im.n_frames):
        im.seek(frame)
        new_frames.append(im.copy().convert('P', palette=Image.ADAPTIVE, colors=256))
    new_frames[0].save('lorenz_model_compressed.gif', save_all=True, append_images=new_frames[1:], optimize=True, duration=100)
