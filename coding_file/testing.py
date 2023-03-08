import sys
sys.path.append(r'C:\Users\joe51\OneDrive\桌面\profile_ntu\coding_file\asfunc.py')

import numpy as np
from matplotlib import pyplot as plt
import asfunc as asf
from asfunc import thermodyamics as thermo


x = np.linspace(1,100)
y = np.linspace(1,100)
minus_y = 0
add_y = 0

asf.one_dimension_plot(x, y, minus_y, add_y)

plt.show()
