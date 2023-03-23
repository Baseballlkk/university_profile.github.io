import numpy as np
def Lorenz(xi, yi, zi, rho, sigma, beta):
    xf = sigma*(yi-xi)
    yf = xi*(rho-zi)-yi
    zf = xi*yi-beta*zi

    return xf, yf, zf


