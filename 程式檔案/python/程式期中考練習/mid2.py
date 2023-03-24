# import library
import numpy as np
import matplotlib.pyplot as plt

# announce variables
P0 = 1000
H = 8500
Rd = 287
cp = 1004
Rv = 461.5
Lv = 2.5*(10**6)
epsilon = 0.622
g = 9.8

T0 = 298
q0 = 0.015
z = np.arange(0,12000,20)
iqv = []

# compute
P = P0*np.exp(-z/H)

Tp = T0+(-g/cp)*z

e_s = 6.11*np.exp((Lv/Rv)*((1/273.15)-1/Tp))
q_vsp = (epsilon*e_s)/(P-(1-epsilon)*e_s)

Th_p = Tp*((P0/P)**(Rd/cp))

# find LCL
i = q0>=q_vsp
iqv = np.where(i, q_vsp, np.nan)
LCL = np.nanargmax(iqv)

# plot
f,ax = plt.subplots(1,3,sharex = 'none',sharey = 'row')
ax[0].plot(Th_p,z,'g--')
ax[0].plot(Tp,z,'r:')
ax[0].set_xticks(np.linspace(180,300,5))
ax[0].set_yticks(np.linspace(0,12000,7))
ax[0].set_ylim([0,12000])
ax[0].set_xlim([180,300])
ax[0].set_title('temperature')
ax[0].set_xlabel('[K]')
ax[0].set_ylabel('height[m]')
ax[0].legend([r'$\theta_p$',r'$T_p$'])

Q15 = np.array([15])
q15 = np.tile(Q15,600)

ax[1].plot(q_vsp*1000,z,'r-')
ax[1].plot(q15,z,'k:')
ax[1].plot(1000*q0,z[LCL],'bo')
ax[1].set_xlim([0,20])
ax[1].set_xticks(np.linspace(0,20,5))
ax[1].set_xlabel('[g/kg]')
ax[1].set_title('mixing ratio')
ax[1].legend([r'$q_{vsp}$',r'$q_0$','LCL'])

ax[2].plot(P,z,'k-')
ax[2].set_title('pressure')
ax[2].set_xlabel('[hPa]')
ax[2].set_xticks(np.linspace(200,1000,5))
ax[2].set_xlim([200,1000])
plt.show()
