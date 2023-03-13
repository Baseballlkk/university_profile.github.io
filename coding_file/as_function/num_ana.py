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
        if ((f.func(x1)*f.func(x3))<0):
            x2 = x3
        else :
            x1 = x3
    x = (x1+x2)/2
    return x

def Newton_Method(x1, h, TOL):
    import function as f

    x = x1
    xa = x1
    while (abs(xa-x1)>TOL):
        x = xa
        df = (f(x+h)-f(x-h))/(2*h)
        xa = x-(f(x)/df(x))
    
    return xa


# def Secant_Method(x0, x1):
