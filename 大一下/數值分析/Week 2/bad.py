ep = 0.622
A = 2.53*10**9
B = 5420
ka = 7/2
w = 10*10**(-3)
p0 = 1000
T0 = 300

def func(x):
	y = x-B/(log(A*ep/(w*p0))*(T0/x)**ka)
	return(y)