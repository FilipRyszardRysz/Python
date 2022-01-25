import matplotlib.pyplot as plt
import math as m

f=1
fi=0
fs=44000 #hz
Tc=1
Ts=1/fs
N=(Tc/Ts)

t = []
x = []
y = []
z = []
v = []

#Zadanie 2, numer 2 z tabeli 2
for n in range(0, int(N)):
	t.append(n/fs)
	x.append(m.sin(2 * m.pi * f * t[n] * m.cos(3 * m.pi * t[n]) + t[n] * fi))
	y.append(((x[n] * t[n]*t[n]*t[n])/3))
	z.append(1.92 * (m.cos(3*m.pi * t[n]/2) + m.cos((y[n]*y[n])/8*x[n]+3)*t[n]))
	v.append((((y[n] * z[n])/(x[n]+2))*m.cos(7.2*m.pi+m.sin(m.pi*t[n]*t[n]))))


plot = plt.plot(t,y)
plt.title('Zadanie 2, wykres y')
plt.show()
plot = plt.plot(t,z)
plt.title('Zadanie 2, wykres z')
plt.show()
plot = plt.plot(t,v)
plt.title('Zadanie 2, wykres v')
plt.show()