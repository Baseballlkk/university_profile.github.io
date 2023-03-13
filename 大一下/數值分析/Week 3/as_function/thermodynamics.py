import numpy as np

def virtual_temp(qv, T):
    epsilon = 0.622
    Tv = (1+(1/epsilon-1)*qv)*T
    return Tv

def buoyancy_acceleration(Tv, Tvs):
    g = 9.81
    a = (Tv-Tvs)/Tvs*g
    return a