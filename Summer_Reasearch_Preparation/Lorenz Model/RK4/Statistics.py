# import lib 
import numpy as np
import matplotlib.pyplot as plt

A00 = np.loadtxt('Linear_operator[0,0].txt')
A01 = np.loadtxt('Linear_operator[0,1].txt')
A02 = np.loadtxt('Linear_operator[0,2].txt')
A10 = np.loadtxt('Linear_operator[1,0].txt')
A11 = np.loadtxt('Linear_operator[1,1].txt')
A12 = np.loadtxt('Linear_operator[1,2].txt')
A20 = np.loadtxt('Linear_operator[2,0].txt')
A21 = np.loadtxt('Linear_operator[2,1].txt')
A22 = np.loadtxt('Linear_operator[2,2].txt')

# calculate medium