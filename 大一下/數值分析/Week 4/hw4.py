import numpy as np

n = int(input("Please input the size of the matrix: "))

# X = input("Input the solution set of equations:")

def Backward_Sub(n):
    A = np.empty((n,n))
    AX = np.empty(n)
    dS = []
    X = np.empty(n)

    for i in range(n):
        for j in range(n):
            print('Input a list of coefficients [', i, ',',  j,'  ] : ')
            A[i, j] = input()

    for i in range(n):
        print('Input a list of coefficients [', i, ',',  j,'  ] : ')
        AX[i] = input()
    
    for i in range(n-1, -1, -1):
        if (i==n-1):
            X[i] = AX[i]/A[i,i]

        else :
            a0 = 0
            for j in range(n-1, i-1, -1):
                a = A[i, j]*X[j]
                a0 = a0+a
            X[i] = (AX[i]-a0)/A[i,i]
    return X
print(Backward_Sub(n))