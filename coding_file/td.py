'''
this package is collection of equation which is often uesd in atmospheric thermodynamics
version: 1.0.0 by Joseph Kan 20230330
'''
# import lib
import numpy as np

# set constant
epsilon = 0.622
K = (287/1004)

# input mass of vapor & dry air
def mixing_ratio(mv, md):
    print("Transform the quatities into numpy array.")
    rv = np.empty(len(mv))
    rv = mv/md
    return rv

# input mass of vapor & dry air
def relative_humidity(mv, md):
    print("Transform the quatities into numpy array.")
    qv = np.empty(len(mv))
    qv = mv/(mv+md)
    return qv

# input mixing ratio
def rv_to_qv(rv):
    print("Transform the quatities into numpy array.")
    qv = np.empty(len(rv))
    qv = rv/(1+rv)
    return qv

# input relative humidity and temp
def virtual_temperature(qv, T):
    print("Transform the quatities into numpy array.")
    Tv = np.empty(len(qv))
    Tv = (1+(1/epsilon-1)*qv)*T
    return Tv

#
def potential_temperature(T, P, P0):
    P0 = float(input("Input the pressure level: (in hPa)"))
    theta = np.empty(len(T))
    theta = T*(P0/P)**K
    return theta