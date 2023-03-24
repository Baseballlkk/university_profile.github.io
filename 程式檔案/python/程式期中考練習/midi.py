import math as m
# declare variables
A1 = 6.112
A2 = 17.67
A3 = 273.15
A4 = 29.65
A5 = 21.87
A6 = 7.66

# input variables
T,E = input('Please input temperature (in K) and vapor pressure (in hPa):').split()
T = float(T)
E = float(E)

# compute Es
if T>=273.15:
    Es = A1*m.exp((A2*(T-A3))/(T-A4))
    RH = (E/Es)*100
    print('RH = ',RH,'%')
elif 0<=T<273.15:
    Es = A1*m.exp((A5*(T-A3))/(T-A6))
    RH = (E/Es)*100
    print('RH = ',RH,'%')
elif (T<0)or(E<0):
    RH = -999.9
    print('RH = ',RH,'%')


