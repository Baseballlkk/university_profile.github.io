import math as m

def func(w, p0, T0, Tc):
	ep = 0.622
	A = 2.53*10**9
	B = 5420.0
	ka = 7/2
	f = Tc-B/(m.log((A*ep)/(w*p0))*(T0/Tc)**ka)
	return f