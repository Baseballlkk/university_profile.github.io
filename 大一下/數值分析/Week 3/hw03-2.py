import numpy as np
import as_function.num_ana as num
import math as m

x0 = float(input('Input the initial value 1: '))
x1 = float(input('Input the initial value 2: '))
tol = 1*10**(-6)
w = 0.01
p0 = 1000
t0 = 300

Tc, times = num.Solve_Tc(x0, x1, tol, w, p0, t0)
Tcn, timen  = num.Solve_TcN(x1, tol, w, p0, t0)
print(Tc)
print(times)

print(Tcn)
print(timen)