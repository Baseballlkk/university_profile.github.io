# import For
# import Back

# def Gauss_elim(n, A, AX, X):
#     A, AX = For.ForwardSub(n, A, AX)
#     X = Back.BackwardSub(n, A, AX, X)

#     return(X)
import numpy as np

def gauss_elimination(A, b):
    
    # Augment A with b to form the augmented matrix
    Ab = np.hstack((A, b.reshape(-1, 1)))
    n = Ab.shape[0]
    
    # Perform Gaussian elimination with partial pivoting
    for j in range(n-1):
        pivot = np.argmax(np.abs(Ab[j:, j])) + j
        if Ab[pivot, j] == 0:
            raise ValueError("Matrix is singular")
        Ab[[j, pivot], :] = Ab[[pivot, j], :]
        for i in range(j+1, n):
            ratio = Ab[i,j] / Ab[j,j]
            Ab[i, j:] -= ratio * Ab[j, j:]
    
    # Back-substitute to find the solution vector x
    x = np.zeros((n, 1))
    for i in range(n-1, -1, -1):
        x[i] = (Ab[i, -1] - Ab[i, i+1:-1].dot(x[i+1:])) / Ab[i,i]
    
    return x
