I = input('Please input benefit:(tens of thousand)')
I = float(I)
if (0< I <= 10):
    m = I * 0.1
    print(m)
elif (10 < I <= 20):
    m = (I-10)*0.075 + 10*0.1
    print(m)
elif (20 < I <= 40):
    m = (I-20)*0.05 + 10*0.075 + 10*0.1
    print(m)
elif (40 < I <= 60):
    m = (I-40)*0.03 + 20*0.05 + 10*0.075 + 10*0.1
    print(m)
elif (60 < I <= 100):
    m = (I-60)*0.015 + 20*0.03 + 20*0.05 + 10*0.075 + 10*0.1
    print(m)
elif (I < 100):
    m = (I-100)*0.01 + 40*0.015 + 20*0.03 + 20*0.05 + 10*0.075 + 10*0.1
    print(m)
else:
    print('negative number')

