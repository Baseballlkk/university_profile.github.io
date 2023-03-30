import numpy as np
def GS(n, A, AX, X):
    for i in range(n):
        s = 0
        s = np.dot(A[i, :], X) - A[i, i] * X[i]
        X[i] = (AX[i]-s)/A[i, i]
    return X