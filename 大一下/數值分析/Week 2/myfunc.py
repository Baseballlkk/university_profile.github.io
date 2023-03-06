import math as m
import myfunc as mf
import function as f

# factorial
def factorial(x):
	# loop to calculate the factorial
	if (x == 0):
		print('0! = 1')
	elif (x > 0):
		f = 1
		for i in range(1,x+1):
			f *= i
		return(f)
			

#for specific topic
def f(x):
	r = round(m.exp(x)/x, 5)-round(1/x, 5)
	return(r)

#for specific topic
def f1(x):
	r = (m.exp(x)-1)/x
	return(r)

# taylor's expension of cos(x) first 3
def tc3(x):
	ta = round(1, 6)-round(x**2/mf.factorial(2), 6)+round(x**4/mf.factorial(4),6)
	return(ta)

# Bisection Method
def bisectionmathod(TOL, x1, x2):
	while (TOL < x2-x1):
		x3 = (1/2)*(x1+x2)
		if (f.func(x1)*f.func(x3)<0):
			x2 = x3
		else :
			x1 = x3
	return(x3)
		