import numpy as np

def ForwardSub(n, A, AX):
    for j in range(n):
        if A[j,j] == 0:
            for k in range(j+1, n):
                cA = np.empty((1,n))
                if A[k,j] != 0:
                    cA[0,:] = A[j,:]
                    A[j,:] = A[k,:]
                    A[k,:] = cA[:]
                    cAX = AX[j,0]
                    AX[j] = AX[k]
                    AX[k] = cAX

        for i in range(j+1, n):
            ratio = A[i,j] / A[j,j]
            A[i,:] = A[i,:] - ratio * A[j,:]
            AX[i] = AX[i] - ratio * AX[j]
    
    return(A,AX)