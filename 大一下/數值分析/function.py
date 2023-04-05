# import lib
import numpy as np
import scipy.misc
import func as f

# absolte error
def abs_err(arr_est, arr_true):
    abserr = np.abs(arr_est-arr_true)
    return abserr

# rlative error
def rel_err(arr_est, arr_true):
    relerr = abs_err(arr_est, arr_true)/arr_true
    return relerr

# bisection method
def bi_method(x1, x2, TOL):
    if f.func(x1)*f.func(x2) < 0:
        while (abs(x2-x1) < TOL):
            x3 = 1/2*(x1+x2)
            if (f.func(x1)*f.func(x3) < 0):
                x2 = x3
            else :
                x1 = x3
        x = 1/2*(x1+x2)
    return x

# Newton method
def newton_method(x0, tol):
    x = x0
    while abs(f.func(x)) > tol:
        df = scipy.misc.derivative(f.func(), x, dx=1e-6, n=1)  # 估算一阶导数
        x = x - f.func(x) / df
    return x

# secant method
def sec_method(x0, x1, tol):
    while (abs(x0-x1) < tol):
        x2 = x1 - f.func(x1)*(x0-x1)/(f.func(x0)-f.func(x1))
        x0 = x1
        x1 = x2
    return x2

# Gauss elimination
def gaussian_elimination(A, b):
    aug_matrix = np.column_stack((A, b))

    n = len(A)
    for i in range(n-1):
        max_row = i + np.argmax(np.abs(aug_matrix[i:, i]))
        if max_row != i:
            aug_matrix[[i, max_row], :] = aug_matrix[[max_row, i], :]
        for j in range(i+1, n):
            factor = aug_matrix[j, i] / aug_matrix[i, i]
            aug_matrix[j, i:] = aug_matrix[j, i:] - factor * aug_matrix[i, i:]

    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (aug_matrix[i, n] - np.dot(aug_matrix[i, i+1:n], x[i+1:])) / aug_matrix[i, i]

    return x

# Guass seidel
def gauss_seidel(A, b, x0, max_iter=10000, tol=1e-6):
    
    n = len(A)
    x = np.array(x0)
    for k in range(max_iter):
        for i in range(n):
            x[i] = (b[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
        if np.linalg.norm(np.dot(A, x) - b) < tol:
            return x
    return x

# Jacobi
def jacobi(A, b, x0, max_iter=10000, tol=1e-6):
    n = len(A)
    x = np.array(x0)
    D = np.diag(A) 
    R = A - np.diagflat(D)  
    for k in range(max_iter):
        x_new = (b - np.dot(R, x)) / D
        if np.linalg.norm(x_new - x) < tol:
            return x_new
        x = x_new
    return x

