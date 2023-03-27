import For
import Back

def Gauss_elim(n, A, AX, X):
    A, AX = For.ForwardSub(n, A, AX)
    X = Back.BackwardSub(n, A, AX, X)

    return(X)