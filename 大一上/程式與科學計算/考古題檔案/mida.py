
#import library
import math as m
import numpy as np

#accept value from user
n = input('input n:')
n = float(n)
n = round(n,0)
n = int(n)

# create s  array
s = np.zeros(n+1)
s[0] = 1

# calculate foactorial
for i in range(n):
 s[i+1] =  (1/(m.factorial(i+1)))+s[i]

print(s[n])
