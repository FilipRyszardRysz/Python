import matplotlib.pyplot as plt
import math as m

f=1
fi=0
fs=44000 #hz
Tc=1
Ts=1/fs
N=(Tc/Ts)

t = []
u = []

#Zadanie 3, funkcja 1 z tabeli 3

for n in range(0, int(N)):
    t.append(n/fs)
    if (t[n] < 0.1) and (t[n] >= 0):
        u.append((m.sin(6*m.pi *t[n])*m.cos(5*m.pi*t[n])))
    if (t[n] < 0.4) and (t[n] >= 0.1):
        u.append((-1.1* t[n]*m.cos(41*m.pi * (t[n] * t[n]))))
    if (t[n] < 0.72) and (t[n] >= 0.4):
        u.append((t[n] * m.sin(20 * (t[n]*t[n]*t[n]*t[n]))))
    if (t[n] < 1) and (t[n] >= 0.72):
        u.append((3.3*(t[n]-0.72)*m.cos(27 * t[n] + 1.3)))

plot = plt.plot(t,u)
plt.title('Zadanie 3, wykres u')
plt.show()