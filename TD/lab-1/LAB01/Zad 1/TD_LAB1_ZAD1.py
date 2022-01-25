import matplotlib.pyplot as plt
import math as m

f=1
fi=0
fs=8000 #hz
Tc=1
Ts=1/fs
N=(Tc/Ts)

t = []
x = []

#Zadanie 1 numer 5 z tabeli 1
for n in range(0, int(N)):
	t.append(n/fs)
	x.append(m.sin(2 * m.pi * f * t[n] * m.cos(3 * m.pi * t[n]) + t[n] * fi))
    
plot = plt.plot(t,x)
plt.title('Zadanie 1, wykres x')
plt.show()