import numpy as np
import matplotlib.pyplot as plt

# a.1
P0 = 1000
Rd = 287
Cp = 1004
Lv = 2.5*(10**6)
Rv = 461

P = np.arange(700,1000,1)

Th1 = np.array([300])
Th1 = np.tile(Th1,(150))
Th2 = np.array([290])
Th2 = np.tile(Th2,(150))
Th = np.hstack((Th1,Th2))

q1 = np.array([0.001])
q1 = np.tile(q1,(150))
q2 = np.array([0.01])
q2 = np.tile(q2,(150))
q = np.hstack((q1,q2))

# a.2
T = Th*((P/P0)**(Rd/Cp))

es = 6.11*np.exp((Lv/Rv)*((1/273)-1/T))

qs = 0.6226*(es/(P-es))

RH = q/qs

e = (1/0.6226)*q*P

# b.1
l1 = RH>1
icloud = np.where(l1,RH,np.nan)

icb = np.nanargmin(icloud)

ict = np.nanargmax(icloud)

# b.2
LWP = (100/9.8)*(np.trapz((q[ict:icb+1]-qs[ict:icb+1]),P[ict:icb+1],dx=1))
LWP = round(LWP,2)

print('Pcb (hPa)= %5.2f' %P[icb])
print('Pct (hPa)= %5.2f' %P[ict])
print('LWP (kg/m2)=',LWP)

data = np.array((list(zip(P,Th,q,RH))))
np.savetxt('midb.txt',data,comments='#',header = ' P(hPa)   Th(K)    q(kg/kg) RH',fmt='%8.1f %8.1f  %9.3f  %9.3f')