# import library
import numpy as np
import matplotlib.pyplot as plt

#c.1
prec = np.loadtxt('TCCIP_daily_precip_2018-2020.txt')
d = np.linspace(1,1096,1096)
plt.plot(d,prec,color = 'dodgerblue',linewidth = 1)

g6 = prec>=66.75
dg6 = d[g6]
prec10 = np.sort(prec)
prec10 = prec10[::-1]
prec10 = prec10[:9]
print(prec10)


plt.plot(dg6,prec10,'r*')
plt.xlim([-10,1100])
plt.ylim([0,130])
plt.xticks(np.linspace(0,1100,12))
plt.yticks(np.linspace(0,130,14))
plt.xlabel('Days',fontsize = 15)
plt.ylabel('Rainfall [mm/day]',fontsize = 15)
plt.title('TCCIP 2018-2020 precipitation time series',fontsize = 18)

plt.savefig('midc1.png')
plt.show()

# c.2
bins = np.array([0,10,20,30,40,50,60,70,80,90,100,130])
counts = np.zeros(11)

counts[0] = prec[0<=prec<10]
counts[1] = prec[10<=prec<20]
counts[2] = prec[20<=prec<30]
counts[3] = prec[30<=prec<40]
counts[4] = prec[40<=prec<50]
counts[5] = prec[50<=prec<60]
counts[6] = prec[60<=prec<70]
counts[7] = prec[70<=prec<80]
counts[8] = prec[80<=prec<90]
counts[9] = prec[90<=prec<100]
counts[10] = prec[100<=prec<=130]

# c.3
x = np.array([5,15,25,35,45,55,65,75,85,95,120])
plt.plot(x,counts,'b-.')
plt.xlim([0,130])
plt.ylim([0,10**3])
plt.yscale('log')
plt.xticks(bins)
plt.yticks([r'$10^0$',r'$10^1$',r'$10^3$'])
plt.xlabel('Rainfall [mm/day]',fontsize = 15)
plt.ylabel('Counts',fontsize = 15)
plt.title('TCCIP 2018-2020 precipitation distribution',fontsize = 18)

plt.savefig('midc2.png')
plt.show()
