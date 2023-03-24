# import library
import math as m

# input value
n = input('input n:')
n = int(n)

# set initial value
e = []
e[0] = 1

# calculate e
for i in range(n):
    e[i+1] = e[i]+(1/(m.factorial(i+1)))

# output the consequence
print(e[len(n)])