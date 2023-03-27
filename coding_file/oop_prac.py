import numpy as np
import matplotlib.pyplot as plt

sigma = 10
rho = 28
beta = 8/3

loop_time = int(input("Please input the loop time: "))
dt = float(input('Input time interval: '))

class create_array:
    def __init__(self):
        self.len = 0

    def zerosarray1D(self, len):
        self.array1d = np.zeros(len)

    def __getitem__(self, index):
        return self.array1d[index]
    
    def __setitem__(self, index, value):
        self.array1d[index] = value

class lm:
    def lorenz(self, x, y, z):
        dx = sigma*(y-x)
        dy = x*(rho-z)-y
        dz = x*y-beta*z
        return dx, dy, dz

    def euler(self, xi, dx):
        xf = xi + dx*dt
        return xf

class intial:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0

    def initial_value(self):
        self.x = float(input("Input intial value of x: "))
        self.y = float(input("Input intial value of y: "))
        self.z = float(input("Input inital value of z: "))
        return self.x, self.y, self.z


x = create_array()
y = create_array()
z = create_array()

x.zerosarray1D(loop_time)
y.zerosarray1D(loop_time)
z.zerosarray1D(loop_time)

initial = intial()
x0, y0, z0 = initial.initial_value()

x[0] = x0
y[0] = y0
z[0] = z0

lm = lm()
for i in range(loop_time-1):
    dx, dy, dz = lm.lorenz(x[i], y[i], z[i])
    x[i+1] = lm.euler(x[i], dx)
    y[i+1] = lm.euler(y[i], dy)
    z[i+1] = lm.euler(z[i], dz)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x.array1d, y.array1d, z.array1d, lw = 0.1)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()
