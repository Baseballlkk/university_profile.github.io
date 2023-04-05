'''
Joseph Kan 20230331
'''
# import lib
import numpy as np
import matplotlib.pyplot as plt
import random as r

# input time interval
loop_time = int(input('Input loop time: '))
h = float(input('Input time interval: '))

#############################################################################
# write class of rk4
class k1:
    def k1x(self, x, y, z, h):
        self.k1_x = 10*(y-x)
        return self.k1_x
    
    def k1y(self, x, y, z, h):
        self.k1_y = x*(28-z)-y
        return self.k1_y
    
    def k1z(self, x, y, z, h):
        self.k1_z = x*y-8/3*z
        return self.k1_z

class k2(k1):
    def k2x(self, x, y, z, h):
        self.k2_x = 10*((y+h/2*self.k1y(x, y, z, h))-(x+h/2))
        return self.k2_x
    
    def k2y(self, x, y, z, h):
        self.k2_y = (x+h/2)*(28-(z+h/2*self.k1z(x, y, z, h)))-(y+h/2*self.k1y(x, y, z, h))
        return self.k2_y
    
    def k2z(self, x, y, z, h):
        self.k2_z = (x+h/2)*(y+h/2*self.k1y(x, y, z, h))-8/3*(z+h/2*self.k1z(x, y, z, h))
        return self.k2_z
    
class k3(k2):
    def k3x(self, x, y, z, h):
        self.k3_x = 10*((y+h/2*self.k2y(x, y, z, h))-(x+h/2))
        return self.k3_x
    
    def k3y(self, x, y, z, h):
        self.k3_y = (x+h/2)*(28-(z+h/2*self.k2z(x, y, z, h)))-(y+h/2*self.k2y(x, y, z, h))
        return self.k3_y
    
    def k3z(self, x, y, z, h):
        self.k3_z = (x+h/2)*(y+h/2*self.k2y(x, y, z, h))-8/3*(z+h/2*self.k2z(x, y, z, h))
        return self.k3_z
    
class k4(k3):
    def k4x(self, x, y, z, h):
        self.k4_x = 10*((y+h*self.k3y(x, y, z, h))-(x+h))
        return self.k4_x
    
    def k4y(self, x, y, z, h):
        self.k4_y = (x+h)*(28-(z+h*self.k3z(x, y, z, h)))-(y+h*self.k3y(x, y, z, h))
        return self.k4_y
    
    def k4z(self, x, y, z, h):
        self.k4_z = (x+h)*(y+h*self.k3y(x, y, z, h))-8/3*(z+h*self.k3z(x, y, z, h))
        return self.k4_z
    
class rk4(k4):
    def x_evo(self, x, y, z, h):
        self.x_1 = x+(h/6)*(self.k1x(x, y, z, h)+2*self.k2x(x, y, z, h)+\
                            2*self.k3x(x, y, z, h)+self.k4x(x, y, z, h))
        return self.x_1

    def y_evo(self, x, y, z, h):
        self.y_1 = y+(h/6)*(self.k1y(x, y, z, h)+2*self.k2y(x, y, z, h)+\
                            2*self.k3y(x, y, z, h)+self.k4y(x, y, z, h))
        return self.y_1
    
    def z_evo(self, x, y, z, h):
        self.z_1 = z+(h/6)*(self.k1z(x, y, z, h)+2*self.k2z(x, y, z, h)+\
                            2*self.k3z(x, y, z, h)+self.k4z(x, y, z, h))
        return self.z_1
##################################################################################
# assign to object
x = np.empty(loop_time)
y = np.empty(loop_time)
z = np.empty(loop_time)

rk = rk4()

# set initial value
x[0] = 0.001
y[0] = 0.001
z[0] = 0.001

# for i in range(loop_time-1):
#     x[i+1] = rk.x_evo(x[i], y[i], z[i], h)
#     y[i+1] = rk.y_evo(x[i], y[i], z[i], h)
#     z[i+1] = rk.z_evo(x[i], y[i], z[i], h)

# fig = plt.figure()
# ax = plt.axes(projection='3d')
# ax.plot3D(x, y, z, lw = 0.3)

# ax.set_xlim([np.min(x), np.max(x)])
# ax.set_ylim([np.min(y), np.max(y)])
# ax.set_zlim([np.min(z), np.max(z)])

# plt.savefig('Test_of_rk4.png', dpi = 600)
# plt.show()
for j in range(1):
    for i in range(10000):

        # calculate between time
        B00 = x[j]+r.uniform(0, 1e-10)
        B01 = x[j]+r.uniform(0, 1e-10)
        B02 = x[j]+r.uniform(0, 1e-10)

        B10 = y[j]+r.uniform(0, 1e-10)
        B11 = y[j]+r.uniform(0, 1e-10)
        B12 = y[j]+r.uniform(0, 1e-10)

        B20 = z[j]+r.uniform(0, 1e-10)
        B21 = z[j]+r.uniform(0, 1e-10)
        B22 = z[j]+r.uniform(0, 1e-10)

        B = np.array([[B00, B01, B02], [B10, B11, B12], [B20, B21, B22]])
        AB = np.array([[rk.x_evo(B00, B10, B20, h), rk.x_evo(B01, B11, B21, h), rk.x_evo(B02, B12, B22, h)],\
                        [rk.y_evo(B00, B10, B20, h), rk.y_evo(B01, B11, B21, h), rk.y_evo(B02, B12, B22, h)],\
                        [rk.z_evo(B00, B10, B20, h), rk.z_evo(B01, B11, B21, h), rk.z_evo(B02, B12, B22, h)]])
        if (np.linalg.det(B) == 0)&(np.linalg.det(AB) == 0):
            break

        # print linear operator
        A = np.dot(AB, np.linalg.inv(B))
        
        with open('Linear_operator.txt', 'a') as file:
            file.write(str(A)+'\n')