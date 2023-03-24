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

# a.3
f,ax = plt.subplots(2,2,sharey = 'all')

ax[0,0].plot(Th,P,'g--')
ax[0,0].plot(T,P,'r:')
ax[0,0].set_xlim([260,320])
ax[0,0].set_ylim([1000,700])
ax[0,0].set_xticks(np.linspace(260,320,4))
ax[0,0].set_yticks(np.linspace(1000,700,4))
ax[0,0].set_ylabel('P(hPa)')
ax[0,0].set_title('temperature (K)')
ax[0,0].legend([r'$\theta$','T'],loc = 'upper right')

ax[0,1].plot(q,P,'g--')
ax[0,1].plot(qs,P,'r:')
ax[0,1].set_xlim([0,0.02])
ax[0,1].set_ylim([1000,700])
ax[0,1].set_xticks(np.linspace(0.00,0.02,5))
ax[0,1].set_yticks(np.linspace(1000,700,4))
ax[0,1].set_title('mixing ratio (kg/kg)')
ax[0,1].legend(['q',r'$q_s$'],loc = 'upper right')


ax[1,0].plot(e,P,'g--')
ax[1,0].plot(es,P,'r:')
ax[1,0].set_xlim([0,30])
ax[1,0].set_ylim([1000,700])
ax[1,0].set_xticks(np.linspace(0,30,4))
ax[1,0].set_yticks(np.linspace(1000,700,4))
ax[1,0].set_xlabel('vapor pressure (hPa)')
ax[1,0].set_ylabel('P(hPa)')
ax[1,0].legend(['e',r'$e_s$'],loc = 'upper right')

p = np.array([1])
p = np.tile(p,(300))
ax[1,1].plot(RH,P,'r-')
ax[1,1].plot(p,P,'k:')
ax[1,1].set_xlim([0,2])
ax[1,1].set_ylim([1000,700])
ax[1,1].set_xticks(np.linspace(0,2,5))
ax[1,1].set_yticks(np.linspace(1000,700,4))
ax[1,1].set_xlabel('relative humidity')

plt.savefig('mida.png')
plt.show()