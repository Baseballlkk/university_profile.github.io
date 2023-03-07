'''
This is a package for atmospheric science assignment
including :
1. 1D plot function
2. 
'''

import numpy as np
from matplotlib import pyplot as plt

def 1Dplot(f, H):
	plt.plot(f, H, linewidth = 0.5)
	plt.xlim([np.min(f), np.max(f)])
	plt.ylim([np.min(H), np.max(H)+100])
	plt.xticks(np.linspace(np.min(f), np.max(f), 6))
	plt.yticks(np.linspace(0, np.max(H)+100, 21))