import numpy as np

def jacobi(A, b, x0, tol=1e-8, max_iter=1000):
    """
    Solve the linear system Ax = b using the Jacobi method.
    
    Parameters:
    A (ndarray): n x n matrix of coefficients
    b (ndarray): n x 1 matrix of constants
    x0 (ndarray): n x 1 matrix of initial guesses
    tol (float): tolerance for convergence
    max_iter (int): maximum number of iterations
    
    Returns:
    x (ndarray): n x 1 matrix of solution
    iter (int): number of iterations required for convergence
    """
    n = A.shape[0]
    x = np.copy(x0)
    iter = 0
    error = tol + 1
    while error > tol and iter < max_iter:
        x_new = np.zeros_like(x)
        for i in range(n):
            s = np.dot(A[i, :], x) - A[i, i] * x[i]
            x_new[i] = (b[i] - s) / A[i, i]
        error = np.linalg.norm(x - x_new, np.inf)
        x = np.copy(x_new)
        iter += 1
        print(x)
    return x
