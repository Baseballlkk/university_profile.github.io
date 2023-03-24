a = 10e+2
b = 11100
c = 111110
d = 1111111
A = [a,b,c,d]
for i in range(6):
    if (i <= 3):
        print('%07.i' %A[i])
    else:
        print('%07.i' %A[1])
