import matplotlib.pyplot as plt
import math as m

f=1
fi=0
fs=22050 #hz
Tc=1
Ts=1/fs
N=(Tc/Ts)

t = [x for x in range(int(N))]
a = [x for x in range(int(N))]
b = [x for x in range(int(N))]
c = [x for x in range(int(N))]

q = 0.0
w = 0.0
e = 0.0
#Zadanie 4 numer 11 z tabeli 4
for n in range(1, int(N)):
    t[n] = n/fs
    for i in range(1, 2):
        q += ((m.cos(12 * t[n] * i**2) + m.cos(16*t[n]*i)) / i**2)
    a[n] = q
    q = 0.0
    for i in range(1, 4):
        w += ((m.cos(12 * t[n] * i**2) + m.cos(16*t[n]*i)) / i**2) 
    b[n] = w
    w = 0.0
    for i in range(1, 16):
        e += ((m.cos(12 * t[n] * i**2) + m.cos(16*t[n]*i)) / i**2)
    c[n] = e
    e = 0.0

plot = plt.plot(t,a)
plt.title('Zadanie 4, wykres a')
plt.xlabel('Czas')
plt.ylabel('Wartosc')
plt.show()
plot = plt.plot(t,b)
plt.title('Zadanie 4, wykres b')
plt.xlabel('Czas')
plt.ylabel('Wartosc')
plt.show()
plot = plt.plot(t,c)
plt.title('Zadanie 4, wykres c')
plt.xlabel('Czas')
plt.ylabel('Wartosc')
plt.show()
