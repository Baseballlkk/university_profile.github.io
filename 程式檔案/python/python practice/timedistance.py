x_1 = input('please input hours 1:')
y_1 = input('please input minutes 1:')
z_1 = input('please input secconds 1:')
x_2 = input('please input hours 2:')
y_2 = input('please input minutes 2:')
z_2 = input('please input secconds 2:')
x_1 = int(x_1)
y_1 = int(y_1)
z_1 = int(z_1)
x_2 = int(x_2)
y_2 = int(y_2)
z_2 = int(z_2)
x = (x_2-x_1)*3600
y = (y_2-y_1)*60
z = (z_2-z_1)
t = x+y+z
print("The total time distance between the two time is :",t,'seconds')
