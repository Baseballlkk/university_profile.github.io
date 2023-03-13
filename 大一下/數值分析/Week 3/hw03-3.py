import numpy as np

x1 = 1
y1 = 1
#  calculate for a set of equation
def f1(x,y):
    ff = (x**2)+(2*x)+2*(y**2)-26
    return ff

def f2(x,y):
    fs = 2*(x**3)-(y**2)+4*y-19
    return fs

def J(x,y):
    j = abs(-4*x*y+8*x-4*y+8-24*(x**2)*y)
    return j

def sose(x1, y1, tol = 0.0001): 
    dx = (-f1(x1,y1)*(-2*y1+4)+f2(x1, y1)*(4*y1))/(J(x1,y1))
    dy = (-f2(x1,y1)*(2*x1+2)+f1(x1, y1)*(-2*y1+4))/(J(x1,y1))
    while (abs(dx) > tol) & (abs(dy) > tol):
        dx = (-f1(x1,y1)*(-2*y1+4)+f2(x1, y1)*(4*y1))/(J(x1,y1))
        dy = (-f2(x1,y1)*(2*x1+2)+f1(x1, y1)*(-2*y1+4))/(J(x1,y1))
        x1 = x1+dx
        y1 = y1+dy
        

    return x1, y1
x, y =sose(x1, y1)
print(x,y)



