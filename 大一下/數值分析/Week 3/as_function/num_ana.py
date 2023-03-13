'''
This is a package for numerical analysis
including:
1. Bisection Method
'''
import numpy as np

def bisection_method(x1, x2, TOL):
    import function as f
    while ((x2-x1) > TOL):
        x3 = (x1+x2)/2
        if ((f.funcb(x1)*f.funcb(x3))<0):
            x2 = x3
        else :
            x1 = x3
    x = (x1+x2)/2
    return x

def Secant_Method(x0, x1, TOL):
    import function as f

    while (abs(x0-x1)>TOL):
        x2 = x1-f.funcs(x1)*((x0-x1)/(f.funcs(x0)-f.funcs(x1)))
    
        x0 = x1
        x1 = x2

    return x2

def Solve_Tc(x0, x1, TOL, w, p0, T0):
    import function as f

    init = 0
    f0 = f.funcs(w, p0, T0, x0)
    f1 = f.funcs(w, p0, T0, x1)
    while (abs(x1-x0)>TOL):
        f0 = f.funcs(w, p0, T0, x0)
        f1 = f.funcs(w, p0, T0, x1)
        x2 = x1-f1*((x0-x1)/(f0-f1))
        print(x2)
        x0 = x1
        #f0 = f1
        x1 = x2
        f1 = f.funcs(w, p0, T0, x1)
        print(x0,x1)
        init += 1
    return x1, init

def Newton_Method(x1, TOL):
    import function as f
    f1, fp1 = f.funcn(x1)
    x2 = x1 - f1/fp1
    while (abs(x1-x2)> TOL):
        f1, fp1 = f.funcn(x1)
        x2 = x1 - f1/fp1

        x1 = x2

    return x2

def Solve_TcN(x1, TOL, w, p0, T0):
    import function as f
    times = 0
    
    f1, fp1 = f.funcs(w, p0, T0, x1)
    x2 = x1 - f1/fp1
    
    
    while (abs(x1-x2)> TOL):
        f1, fp1 = f.funcs(w, p0, T0, x1)
        x2 = x1 - f1/fp1

        x1 = x2
        times +=1
    return x2, times

