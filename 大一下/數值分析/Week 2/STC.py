import numpy as np
import myfunc as mf

ep = 0.622
A = 2.53*10**9
B = 5420
ka = 7/2


def Solve_Tc(w, p0, T0, x1, x2, TOL):
	
	Tc = mf.bisectionmathod(TOL, x1, x2)
	return(Tc)