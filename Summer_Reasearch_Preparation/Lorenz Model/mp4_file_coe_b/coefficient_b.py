# import library
import numpy as np
import matplotlib.pyplot as plt
import lm

# set loop time
loop_time = 100000

# set time interval
dt = 0.01

# set inital coefficient


# set position array
x = np.empty(loop_time+1)
y = np.empty(loop_time+1)
z = np.empty(loop_time+1) 

# set initial condition
x[0], y[0], z[0]= (0.1, 0.1, 0.1)

# conduct the lorenz model
for i in range(41):
    sigma = 10
    beta = 1/3
    rho = 28
    beta += 1/3*i
    

    for j in range(loop_time):
        xf, yf, zf = lm.Lorenz(x[j], y[j], z[j], rho, sigma, beta)
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

    rho = str(rho)
    sigma = str(sigma)
    beta = str(beta)

    plt.title('Lorenz model for '+rho+','+sigma+','+beta)
    plt.rcParams['agg.path.chunksize'] = 101
    plt.savefig(r'C:\Users\joe51\OneDrive\桌面\Lorenz Model\mp4_file_coe_b\Lorenz_Model_for_'+rho+','+sigma+','+beta+'.png', dpi = 300)

    rho  = float(rho)
    sigma = float(sigma)
    beta = float(sigma)
