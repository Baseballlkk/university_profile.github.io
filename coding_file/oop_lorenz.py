import numpy as np
import matplotlib.pyplot as plt

sigma = 10
rho = 28
beta = 8/3

loop_time = int(input("Please input the loop time: "))
dt = float(input('Input time interval: '))

class Array:
    def __init__(self, length):
        self.array = np.zeros(length)

    def __getitem__(self, index):
        return self.array[index]
    
    def __setitem__(self, index, value):
        self.array[index] = value

class Lorenz:
    def __init__(self):
        self.sigma = 10
        self.rho = 28
        self.beta = 8/3

    def __call__(self, x, y, z):
        dx = self.sigma*(y-x)
        dy = x*(self.rho-z)-y
        dz = x*y-self.beta*z
        return dx, dy, dz

class Euler:
    def __init__(self, dt):
        self.dt = dt

    def __call__(self, xi, dx):
        xf = xi + dx*self.dt
        return xf

class Initial:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0

    def __call__(self):
        self.x = float(input("Input intial value of x: "))
        self.y = float(input("Input intial value of y: "))
        self.z = float(input("Input inital value of z: "))
        return self.x, self.y, self.z

class Plot:
    def __init__(self, fig, ax):
        self.fig = fig
        self.ax = ax

    def __call__(self, x, y, z, lw):
        self.ax.plot(x.array, y.array, z.array, lw=lw)
        self.ax.set_xlabel('X Label')
        self.ax.set_ylabel('Y Label')
        self.ax.set_zlabel('Z Label')
        plt.show()

class Simulation:
    def __init__(self, loop_time, dt):
        self.loop_time = loop_time
        self.dt = dt

        self.x = Array(loop_time)
        self.y = Array(loop_time)
        self.z = Array(loop_time)

        self.initial = Initial()
        self.lorenz = Lorenz()
        self.euler = Euler(dt)

    def run(self):
        x0, y0, z0 = self.initial()
        self.x[0] = x0
        self.y[0] = y0
        self.z[0] = z0

        for i in range(self.loop_time-1):
            dx, dy, dz = self.lorenz(self.x[i], self.y[i], self.z[i])
            self.x[i+1] = self.euler(self.x[i], dx)
            self.y[i+1] = self.euler(self.y[i], dy)
            self.z[i+1] = self.euler(self.z[i], dz)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

simulation = Simulation(loop_time, dt)
simulation.run()

plot = Plot(fig, ax)
plot(simulation.x, simulation.y, simulation.z, lw=0.1)
