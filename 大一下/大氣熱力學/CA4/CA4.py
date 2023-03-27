# import lib
import numpy as np
import matplotlib.pyplot as plt

# load data
H, P, T, U = np.loadtxt(r"C:\Users\joe51\OneDrive\桌面\profile_ntu\大一下\大氣熱力學\CA3\46810-2018072100.edt.txt", delimiter = ',', usecols = (1, 2, 3, 4), skiprows = 3, unpack = True)

T = T+273.15

# set constant
g = 9.8
Cp = 1004
P0 = 1000
Rd = 287
K = Rd/Cp

def find_nearest(array, value):
    idxarray = np.empty(len(array))
    for i in range(len(array)):
        idxarray[i] = abs(array[i]-value)
    idx = np.argmin(idxarray)
    return idx

# topic 1
## draw potential temperature & static energy
Sd = Cp*T+g*H
Pt = T*(P0/P)**(Rd/Cp)

# figure = plt.figure(figsize = (8,6))
# plt.plot(Sd, H, lw = 0.5, color = 'blue')
# plt.plot(Cp*Pt, H, lw = 0.5, color = 'orange')
# plt.axhline(y = 15397, xmin = 0, xmax = 1, lw = 0.5)
# plt.axhline(y = np.max(H), xmin = 0, xmax = 1, lw = 0.1)
# plt.xticks(np.linspace(np.min(Sd), np.max(Cp*Pt), 5))
# plt.yticks(np.linspace(0, np.max(H)+1000, 11))
# plt.xlim([np.min(Sd), np.max(Cp*Pt)])
# plt.ylim([0, np.max(H)+1000])
# plt.xlabel('Static Energy & Cp*Potential Temperature [J/kg]', fontsize = 15)
# plt.ylabel('Altitude', fontsize = 15)
# plt.title('Static Energy Proifle - Altitude', fontsize = 15)
# plt.legend([r'$S_d$', r'$C_p*\theta$'])

# plt.savefig('Static_Energy.png', dpi = 600)
# plt.show()

# fig = plt.figure(figsize = (8,6))
# plt.plot(Sd-Cp*Pt, H, lw = 0.5)
# plt.axhline(y = 15397, xmin = 0, xmax = 1)
# plt.axhline(y = np.max(H), xmin = 0, xmax = 1, lw = 0.1)
# plt.xticks(np.linspace(-443040, 280, 5))
# plt.yticks(np.linspace(0, np.max(H)+1000, 11))
# plt.xlim([-443040, 280])
# plt.ylim([0, np.max(H)+1000])
# plt.xlabel('Difference of Static Energy & Cp*Potential Temperature [J/kg]', fontsize = 15)
# plt.ylabel('Altitude', fontsize = 15)
# plt.title('Difference of Static Energy & Cp*Potential Temperature Proifle - Altitude', fontsize = 15)

# plt.savefig('Dif_Static_Energy.png', dpi = 600)
# plt.show()

# topic 2
## calculate dry parcel
lapse_rate = 9.8/1000

## creat array
Td = np.empty(len(T))
Ptd = np.empty(len(T))
Sdd = np.empty(len(T))

## set initial value
Td[0] = T[0]

## calculate for Td
for i in range(len(Td)-1):
    Td[i+1] = Td[i]-lapse_rate*(H[i+1]-H[i])
## calculate for Ptd
for i in range(len(Ptd)):

    Ptd[i] = Pt[0]

## calculate for Sdd
for i in range(len(Sdd)):
    Sdd = Sd[0]

## plot T & Td
fig = plt.figure(figsize = (8,6))
#plt.plot(T, H, lw = 0.5)
plt.plot(Td, H, lw = 0.5, color = 'green')
plt.axhline(y = 15397, xmin =0, xmax = 1, lw = 0.5, color = 'blue')
plt.fill_between(Td, y1 = 0, y2 = 644, color = 'pink')
plt.xticks(np.linspace(140 ,305, 4))
plt.yticks(np.linspace(0, np.max(H), 11))
plt.xlim([140, 305])
plt.ylim([0, 16000])
plt.xlabel('Temperatuer [K]', fontsize = 15)
plt.ylabel('Altitude [m]', fontsize = 15)
plt.title('Temperature for real & dry air profile', fontsize = 15)
plt.legend(['T', r'$T_d$'])

plt.savefig('Temp_of_dry.png', dpi = 600)
plt.show()


## potential temperature
fig = plt.figure(figsize = (8,6))
plt.plot(Pt, H, lw = 0.5)
plt.plot(Ptd, H, lw = 0.5, color = 'green')
plt.axhline(y = 15397, xmin =0, xmax = 1, lw = 0.5, color = 'blue')
plt.xticks(np.linspace(240,400, 5))
plt.yticks(np.linspace(0, np.max(H), 11))
plt.xlim([240,400])
plt.ylim([0, 16000])
plt.xlabel('Potential Temperatuer [K]', fontsize = 15)
plt.ylabel('Altitude [m]', fontsize = 15)
plt.title('Potential Temperature for real & dry air profile', fontsize = 15)
plt.legend([r'$\theta$', r'$\theta_d$'])
plt.savefig('PTemp_of_dry.png', dpi = 600)
plt.show()

# emphisize low
fig = plt.figure(figsize = (8,6))
plt.plot(Pt, H, lw = 0.5)
plt.plot(Ptd, H, lw = 0.5, color = 'green')
plt.axhline(y = 636, xmin = 0, xmax = 1, lw = 0.5, color = 'orange')
plt.xticks(np.linspace(300, 310, 6))
plt.yticks(np.linspace(0, 1000, 11))
plt.xlim([300,310])
plt.ylim([0, 1000])
plt.xlabel('Potential Temperatuer [K]', fontsize = 15)
plt.ylabel('Altitude [m]', fontsize = 15)
plt.title('Potential Temperature for real & dry air profile', fontsize = 15)
plt.legend([r'$\theta$', r'$\theta_d$'])

plt.savefig('PTemp_of_dry_low.png', dpi = 600)
plt.show()

## dry static
fig = plt.figure(figsize = (8,6))

# plt.plot(Sdd, H, lw = 0.5, color = 'green')
# plt.xticks(np.linspace(np.min(Sdd), np.max(Sdd), 6))
# plt.yticks(np.linspace(0, np.max(H)+1000, 11))
# plt.xlim([np.min(Sdd), np.max(Sdd)])
# plt.ylim([0, np.max(H)+1000])
# plt.xlabel('Static Energy [J/kg]', fontsize = 15)
# plt.ylabel('Altitude [m]', fontsize = 15)
# plt.title('Satic Energy of dry air profile', fontsize = 15)

# plt.savefig('Sdd.png', dpi = 600)
# plt.show()

# plt.plot(Sd, H, lw = 0.5, color = 'blue')
# plt.axhline(y = 15397, xmin = 0, xmax = 1, lw = 0.5)
# plt.axhline(y = np.max(H), xmin = 0, xmax = 1, lw = 0.1)
# plt.xticks(np.linspace(np.min(Sd), np.max(Sd), 5))
# plt.yticks(np.linspace(0, np.max(H)+1000, 11))
# plt.xlim([np.min(Sd), np.max(Sd)])
# plt.ylim([0, np.max(H)+1000])
# plt.xlabel('Static Energy [J/kg]', fontsize = 15)
# plt.ylabel('Altitude', fontsize = 15)
# plt.title('Static Energy Proifle - Altitude', fontsize = 15)

# plt.savefig('Sd.png', dpi = 300)
# plt.show()
# plt.plot(Sd, H, lw = 0.5)

# topic 3
index = find_nearest(H, 500)
index_t = find_nearest(H, 14897)
index_m = find_nearest(H, 15397)
index_b = find_nearest(H, 15893)

## case 1
Tt = np.empty(index_t-index+1)
Ptt = np.empty(index_t-index+1)
Sdt = np.empty(index_t-index+1)
Ht = H[index:index_t+1]
Prt = P[index:index_t+1]
Trt = T[index:index_t+1]
Ptrt = Pt[index:index_t+1]
Sdrt = Sd[index:index_t+1]


Tt[0] = T[index]
Ptt[0] = Pt[index]
Sdt[0] = Sd[index]

for i in range(len(Tt)-1):
    Tt[i+1] = Tt[i]-lapse_rate*(Ht[i+1]-Ht[i])

for i in range(len(Tt)):
    Ptt[i] = Ptt[0]

for i in range(len(Tt)):
    Sdt[i] = Sdt[0]

print(np.nanmin(Tt), np.nanmin(Trt))
print(np.nanmin(Ptt), np.nanmax(Ptrt))
print(np.nanmin(Sdt), np.nanmax(Sdrt))

fig = plt.figure(figsize = (8,6))
plt.plot(Tt, Ht, lw = 0.5, color = 'blue')
plt.plot(Trt, Ht, lw = 0.5, color = 'orange')
plt.axhline(y = 500, xmin = 0, xmax = 1, lw = 0.5, color = 'red')
plt.axhline(y = 15397, xmin = 0, xmax = 1, lw = 0.5, color = 'red')
plt.xlim([156, 300])
plt.ylim([0,16000])
plt.xticks(np.linspace(156, 300, 5))
plt.yticks(np.linspace(0,16000, 6))
plt.xlabel('Temperature [K]', fontsize = 15)
plt.ylabel('Altitude [m]', fontsize = 15)
plt.title('Temperature of top hit tropopause', fontsize = 15)
plt.legend(['Parcel', 'Surrounding'])

plt.savefig('Temp_top.png', dpi = 300)
plt.show()

fig = plt.figure(figsize = (8,6))
plt.plot(Ptt, Ht, lw = 0.5)
plt.plot(Ptrt, Ht, lw = 0.5, color = 'orange')
plt.axhline(y = 500, xmin = 0, xmax = 1, lw = 0.5, color = 'red')
plt.axhline(y = 15397, xmin = 0, xmax = 1, lw = 0.5, color = 'red')
plt.xlim([276, 360])
plt.ylim([0,16000])
plt.xticks(np.linspace(276, 360, 4))
plt.yticks(np.linspace(0,16000, 6))
plt.xlabel('Potential Temperature [K]', fontsize = 15)
plt.ylabel('Altitude [m]', fontsize = 15)
plt.title('Potential Temperature of top hit tropopause', fontsize = 15)
plt.legend(['Parcel', 'Surrounding'])

plt.savefig('PTemp_top.png', dpi = 300)
plt.show()

fig = plt.figure(figsize = (8,6))
plt.plot(Sdt, Ht, lw = 0.5)
plt.plot(Sdrt, Ht, lw = 0.5, color = 'orange')
plt.axhline(y = 500, xmin = 0, xmax = 1, lw = 0.5, color = 'red')
plt.axhline(y = 15397, xmin = 0, xmax = 1, lw = 0.5, color = 'red')
plt.xlim([302765, np.max(Sdrt)])
plt.ylim([0,16000])
plt.xticks(np.linspace(302765, np.max(Sdrt), 6))
plt.yticks(np.linspace(0,16000, 6))
plt.xlabel('Static Energy [J/kg]', fontsize = 15)
plt.ylabel('Altitude [m]', fontsize = 15)
plt.title('Static Energy of top hit tropopause', fontsize = 15)
plt.legend(['Parcel', 'Surrounding'])

plt.savefig('Sd_top.png', dpi = 300)
plt.show()

fig = plt.figure(figsize = (8,6))
plt.plot(Sdt, Ht, lw = 0.5)
plt.axhline(y = 500, xmin = 0, xmax = 1, lw = 0.5, color = 'red')
plt.axhline(y = 15397, xmin = 0, xmax = 1, lw = 0.5, color = 'red')
plt.xlim([302765, 303330])
plt.ylim([0,16000])
plt.xticks(np.linspace(302765, 303330, 6))
plt.yticks(np.linspace(0,16000, 6))
plt.xlabel('Static Energy [J/kg]', fontsize = 15)
plt.ylabel('Altitude [m]', fontsize = 15)
plt.title('Static Energy of top hit tropopause', fontsize = 15)

plt.savefig('Sd_top_p.png', dpi = 300)
plt.show()

## case 2
Tm = np.empty(index_m-index+1)
Ptm = np.empty(index_m-index+1)
Sdm = np.empty(index_m-index+1)
Hm = H[index:index_m+1]
Prm = P[index:index_m+1]
Trm = T[index:index_m+1]
Ptrm = Pt[index:index_m+1]
Sdrm = Sd[index:index_m+1]



Tm[0] = T[index]
Ptm[0] = Pt[index]
Sdm[0] = Sd[index]

for i in range(len(Tm)-1):
    Tm[i+1] = Tm[i]-lapse_rate*(Hm[i+1]-Hm[i])

for i in range(len(Tm)):
    Ptm[i] = Ptm[0]

for i in range(len(Tm)):
    Sdm[i] = Sdm[0]

print(np.nanmin(Tm), np.nanmin(Trm))
print(np.nanmin(Ptm), np.nanmax(Ptrm))
print(np.nanmin(Sdm), np.nanmax(Sdrm))

fig = plt.figure(figsize = (8,6))
plt.plot(Tm, Hm, lw = 0.5)
plt.plot(Trm, Hm, lw = 0.5, color = 'orange')
plt.axhline(y = 500, xmin = 0, xmax = 1, lw = 0.5, color = 'red')
plt.axhline(y = 15397, xmin = 0, xmax = 1, lw = 0.5, color = 'red')
plt.xlim([150, 300])
plt.ylim([0,16000])
plt.xticks(np.linspace(150, 300, 6))
plt.yticks(np.linspace(0,16000, 6))
plt.xlabel('Temperature [K]', fontsize = 15)
plt.ylabel('Altitude [m]', fontsize = 15)
plt.title('Temperature of mid hit tropopause', fontsize = 15)
plt.legend(['Parcel', 'Surrounding'])

plt.savefig('Temp_mid.png', dpi = 300)
plt.show()

fig = plt.figure(figsize = (8,6))
plt.plot(Ptm, Hm, lw = 0.5)
plt.plot(Ptrm, Hm, lw = 0.5, color = 'orange')
plt.axhline(y = 500, xmin = 0, xmax = 1, lw = 0.5, color = 'red')
plt.axhline(y = 15397, xmin = 0, xmax = 1, lw = 0.5, color = 'red')
plt.xlim([274,362])
plt.ylim([0,16000])
plt.xticks(np.linspace(274,362, 5))
plt.yticks(np.linspace(0,16000, 6))
plt.xlabel('Potential Temperature [K]', fontsize = 15)
plt.ylabel('Altitude [m]', fontsize = 15)
plt.title('Potntial Temperature of mid hit tropopause', fontsize = 15)
plt.legend(['Parcel', 'Surrounding'])

plt.savefig('PTemp_mid.png', dpi = 300)
plt.show()

fig = plt.figure(figsize = (8,6))
plt.plot(Sdm, Hm, lw = 0.5)
plt.plot(Sdrm, Hm, lw = 0.5, color = 'orange')
plt.axhline(y = 500, xmin = 0, xmax = 1, lw = 0.5, color = 'red')
plt.axhline(y = 15397, xmin = 0, xmax = 1, lw = 0.5, color = 'red')
plt.xlim([302745, np.max(Sdrm)])
plt.ylim([0,16000])
plt.xticks(np.linspace(302745, np.max(Sdrm), 6))
plt.yticks(np.linspace(0,16000, 6))
plt.xlabel('Static Energy [J/kg]', fontsize = 15)
plt.ylabel('Altitude [m]', fontsize = 15)
plt.title('Static Energy of mid hit tropopause', fontsize = 15)
plt.legend(['Parcel', 'Surrounding'])

plt.savefig('Sd_mid.png', dpi = 300)
plt.show()

fig = plt.figure(figsize = (8,6))
plt.plot(Sdm, Hm, lw = 0.5)
plt.axhline(y = 500, xmin = 0, xmax = 1, lw = 0.5, color = 'red')
plt.axhline(y = 15397, xmin = 0, xmax = 1, lw = 0.5, color = 'red')
plt.xlim([302745, 303330])
plt.ylim([0,16000])
plt.xticks(np.linspace(302745, 303330, 6))
plt.yticks(np.linspace(0,16000, 6))
plt.xlabel('Static Energy [J/kg]', fontsize = 15)
plt.ylabel('Altitude [m]', fontsize = 15)
plt.title('Static Energy of mid hit tropopause', fontsize = 15)

plt.savefig('Sd_mid_p.png', dpi = 300)
plt.show()

## case 3
Tb = np.empty(index_b-index+1)
Ptb = np.empty(index_b-index+1)
Sdb = np.empty(index_b-index+1)
Hb = H[index:index_b+1]
Pb = P[index:index_b+1]
Trb = T[index:index_b+1]
Ptrb = Pt[index:index_b+1]
Sdrb = Sd[index:index_b+1]



Tb[0] = T[index]
Ptb[0] = Pt[index]
Sdb[0] = Sd[index]

for i in range(len(Tb)-1):
    Tb[i+1] = Tb[i]-lapse_rate*(Hb[i+1]-Hb[i])

for i in range(len(Tb)):
    Ptb[i] = Ptb[0]

for i in range(len(Tb)):
    Sdb[i] = Sdb[0]

print(np.nanmin(Tb), np.nanmin(Trb))
print(np.nanmin(Ptb), np.nanmax(Ptrb))
print(np.nanmin(Sdb), np.nanmax(Sdrb))

fig = plt.figure(figsize = (8,6))
plt.plot(Tb, Hb, lw = 0.5)
plt.plot(Trb, Hb, lw = 0.5, color = 'orange')
plt.axhline(y = 500, xmin = 0, xmax = 1, lw = 0.5, color = 'red')
plt.axhline(y = 15397, xmin = 0, xmax = 1, lw = 0.5, color = 'red')
plt.xlim([146, 299])
plt.ylim([0,16000])
plt.xticks(np.linspace(146, 299, 4))
plt.yticks(np.linspace(0,16000, 6))
plt.xlabel('Temperature [K]', fontsize = 15)
plt.ylabel('Altitude [m]', fontsize = 15)
plt.title('Temperature of bottom hit tropopause', fontsize = 15)
plt.legend(['Parcel', 'Surrounding'])

plt.savefig('Temp_bot.png', dpi = 300)
plt.show()

fig = plt.figure(figsize = (8,6))
plt.plot(Ptb, Hb, lw = 0.5)
plt.plot(Ptrb, Hb, lw = 0.5, color = 'orange')
plt.axhline(y = 500, xmin = 0, xmax = 1, lw = 0.5, color = 'red')
plt.axhline(y = 15397, xmin = 0, xmax = 1, lw = 0.5, color = 'red')
plt.xlim([272, 368])
plt.ylim([0,16000])
plt.xticks(np.linspace(272, 368, 5))
plt.yticks(np.linspace(0,16000, 6))
plt.xlabel('Potential Temperature [K]', fontsize = 15)
plt.ylabel('Altitude [m]', fontsize = 15)
plt.title('Potntial Temperature of bottom hit tropopause', fontsize = 15)
plt.legend(['Parcel', 'Surrounding'])

plt.savefig('PTemp_bot.png', dpi = 300)
plt.show()


fig = plt.figure(figsize = (8,6))
plt.plot(Sdb, Hb, lw = 0.5)
plt.plot(Sdrb, Hb, lw = 0.5, color = 'orange')
plt.axhline(y = 500, xmin = 0, xmax = 1, lw = 0.5, color = 'red')
plt.axhline(y = 15397, xmin = 0, xmax = 1, lw = 0.5, color = 'red')
plt.xlim([302725, np.max(Sdrb)])
plt.ylim([0,16000])
plt.xticks(np.linspace(302725, np.max(Sdrb), 6))
plt.yticks(np.linspace(0,16000, 6))
plt.xlabel('Static Energy [J/kg]', fontsize = 15)
plt.ylabel('Altitude [m]', fontsize = 15)
plt.title('Static Energy of bottom hit tropopause', fontsize = 15)
plt.legend(['Parcel', 'Surrounding'])

plt.savefig('Sd_bot.png', dpi = 300)
plt.show()

fig = plt.figure(figsize = (8,6))
plt.plot(Sdb, Hb, lw = 0.5)
plt.axhline(y = 500, xmin = 0, xmax = 1, lw = 0.5, color = 'red')
plt.axhline(y = 15397, xmin = 0, xmax = 1, lw = 0.5, color = 'red')
plt.xlim([302725, 303330])
plt.ylim([0,16000])
plt.xticks(np.linspace(302725, 303330, 6))
plt.yticks(np.linspace(0,16000, 6))
plt.xlabel('Static Energy [J/kg]', fontsize = 15)
plt.ylabel('Altitude [m]', fontsize = 15)
plt.title('Static Energy of bottom hit tropopause', fontsize = 15)

plt.savefig('Sd_bot_p.png', dpi = 300)
plt.show()

