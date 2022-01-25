import cmath as m
import matplotlib.pyplot as plt


N = 1000
tablica = []
fs = 1000
Tc = 1

def DFT(x):
    for n in range(0, N):
        a = 0
        for k in range(N):
            a += x[k]* m.exp(-1j *(2 * m.pi * n * k)/N)
        tablica.append(a)
    return tablica


t = [g for g in range(int(N))]
h = [g for g in range(int(N))]

for n in range(0, int(N)):
	t[n] = n/fs
	h[n] = m.sin(2*m.pi*200*t[n])

b = DFT(h)
c = []

for i in range(N):
    image = b[i].imag
    real = b[i].real
    c.append(m.sqrt(real**2 + image**2))

plt.plot(range(len(c)), c)

    
    




