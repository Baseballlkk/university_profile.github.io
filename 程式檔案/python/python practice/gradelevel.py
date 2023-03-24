x = input('Please input your grade:')
x = float(x)
if (90<=x<=100):
    print('A')
elif (80<=x<90):
    print('B')
elif (70<=x<80):
    print('C')
elif (60<=x<70):
    print('D')
elif (0<=x<60):
    print('F')
else:
    print('You enter wrong grade, please input again.')