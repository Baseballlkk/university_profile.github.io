'''
This is a package for atmospheric science assignment
including :
1. 1D plot function
'''

import numpy as np
from matplotlib import pyplot as plt

def single_line(f, H, minus_x = 0, add_x = 0, minus_y = 0, add_y=0, x = '', y_string = '', title = ''):
	plt.plot(f, H, linewidth = 0.5)
	plt.xticks(np.linspace(np.min(f)-minus_x, np.max(f)+add_x, 6))
	plt.yticks(np.linspace(0-minus_y, np.max(H)+add_y, 21))
	plt.xlim([np.min(f)-minus_x, np.max(f)+add_x])
	plt.ylim([np.min(H)-minus_y, np.max(H)+add_y])
	plt.xlabel(x)
	plt.ylabel(y_string)
	plt.title(title)
	