# import lib
import numpy as np
import matplotlib.pyplot as plt

# set run times
loop_times = 1000000

# set time interval
dt = 0.001

# set constant
sigma = 10
rho = 28
beta = 8/3


# class for array
class array:
    def x_array(self):
        x = np.empty(loop_times+1)
    
    def y_array(self):
        y = np.empty(loop_times+1)

    def z_array(self):
        z = np.empty(loop_times+1)

# class of lm
class Lorenz(array):
    def lm(self, array1, array2, array3):
        for i in range():
            self.dxdt = sigma*(array2[i]-array1[i])
            self.dydt = array1[i]*(rho-array3[i])
            self.dzdt = array1[i]*array2[i]-beta*array3[i]
            self.k1x = self.dxdt
            self.k2x = self.dxdt+

    def position(self):





