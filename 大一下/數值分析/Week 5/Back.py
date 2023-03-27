import numpy as np

def BackwardSub(n, A, AX, X):
    for i in range(n-1,-1,-1):
        if (i==n-1):
            X[i] = AX[i]/A[i,i]
        else:
            a0 = 0
            for j in range(n-1,i,-1):
                   a1 = A[i,j]*X[j]
                   a0 = a0 + a1
            X[i] = (AX[i]-a0)/A[i,i]

    return(X)