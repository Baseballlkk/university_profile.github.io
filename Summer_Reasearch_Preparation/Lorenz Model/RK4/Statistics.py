# import lib 
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats as scis
from scipy import io as sciio

A00 = np.loadtxt('Linear_operator[0,0].txt')
A01 = np.loadtxt('Linear_operator[0,1].txt')
A02 = np.loadtxt('Linear_operator[0,2].txt')
A10 = np.loadtxt('Linear_operator[1,0].txt')
A11 = np.loadtxt('Linear_operator[1,1].txt')
A12 = np.loadtxt('Linear_operator[1,2].txt')
A20 = np.loadtxt('Linear_operator[2,0].txt')
A21 = np.loadtxt('Linear_operator[2,1].txt')
A22 = np.loadtxt('Linear_operator[2,2].txt')

# calculate mean value
A00_mean = np.mean(A00)
A01_mean = np.mean(A01)
A02_mean = np.mean(A02)
A10_mean = np.mean(A10)
A11_mean = np.mean(A11)
A12_mean = np.mean(A12)
A20_mean = np.mean(A20)
A21_mean = np.mean(A21)
A22_mean = np.mean(A22)

# calculate standard varible
A00_std = np.std(A00)
A01_std = np.std(A01)
A02_std = np.std(A02)
A10_std = np.std(A10)
A11_std = np.std(A11)
A12_std = np.std(A12)
A20_std = np.std(A20)
A21_std = np.std(A21)
A22_std = np.std(A22)