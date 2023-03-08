'''
This is a package for atmospheric science assignment
including :
1. 1D plot function
2. thermodynamics
'''

import numpy as np
from matplotlib import pyplot as plt

def one_dimension_plot(f, H,minus_y = 0, add_y=0):
	plt.plot(f, H, linewidth = 0.5)
	plt.xticks(np.linspace(np.min(f), np.max(f), 6))
	plt.yticks(np.linspace(0-minus_y, np.max(H)+add_y, 21))
	plt.xlim([np.min(f), np.max(f)])
	plt.ylim([np.min(H)-minus_y, np.max(H)+add_y])

def thermodyamics():
	def virtual_temp(qv, T):
		epsilon = 0.622
		Tc = (1+((1/epsilon-1)*qv))*T
		
		return Tc