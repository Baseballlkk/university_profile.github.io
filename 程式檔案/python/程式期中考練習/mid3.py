# import library
import numpy as np
import matplotlib.pyplot as plt
import math as m
import matplotlib.cm as cm
import matplotlib.colors
import RET 

# c.2
S0 = np.arange(1300,1400,2)
ap = np.arange(0.1,0.9,0.02)
ss,aa = np.meshgrid(S0,ap)

Te = RET.myfun_Te(ss,aa)

# c.3
plt.xticks(np.linspace(1300,1400,6))
plt.yticks(np.linspace(0.1,0.9,9))
plt.xlim([1300,1400])
plt.ylim([0.1,0.9])
plt.xlabel(r'$S_{\odot}(Wm^{-2})$')
plt.ylabel(r'$\alpha_p$')
plt.text(1361,0.25,'Earth')
plt.title('Rediative Equilibrium Temperature [K]')

p1 = plt.contourf(S0,ap,Te, levels = np.arange(150,275,5),cmap = cm.inferno)
plt.colorbar(p1,orientation = 'vertical')
plt.plot(1361,0.3,'ko')
plt.savefig('midc.png')
plt.show()