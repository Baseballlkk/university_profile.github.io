import sys
sys.path.append(r"C:/Users/joe51/OneDrive/桌面/profile_ntu/coding_file/as_function/plot.py")

import numpy as np
from matplotlib import pyplot as plt
from as_function import plot as p


x = np.linspace(1,100)
y = np.linspace(1,100)
minus_x = float(input('Input minus_x: '))
add_x = float(input('Input add_x: '))
minus_y = float(input('Input minus_y: '))
add_y = float(input('Input add_y: '))
x_string = input('Please input name of xlabel: ')
y_string = input('Please input name of ylabel: ')
title = input('Please input title: ')

p.single_line(x, y,minus_x, add_x , minus_y, add_y, x_string, y_string, title)

plt.show()
