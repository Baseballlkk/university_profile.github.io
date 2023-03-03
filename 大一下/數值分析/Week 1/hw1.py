# input the number we wanna do factorial
n = input('Please input the number you wanna do factorial(only input integer):')
n = int(n)

# loop to calculate the factorial
if (n == 0):
    print('0! = 1')
elif (n > 0):
    f = 1
    for i in range(1,n+1):
        f *= i
    print(n,'! = ',f)
else :
    print('Out of Range!!')