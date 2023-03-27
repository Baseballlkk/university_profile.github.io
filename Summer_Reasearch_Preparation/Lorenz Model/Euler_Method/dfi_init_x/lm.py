import numpy as np
def Lorenz(xi, yi, zi, rho = 28, sigma = 10, beta = 8/3):
    xf = sigma*(yi-xi)
    yf = xi*(rho-zi)-yi
    zf = xi*yi-beta*zi

    return xf, yf, zf


