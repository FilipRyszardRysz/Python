import cmath as m
import matplotlib.pyplot as plt




fs = 1000
Tc = 1
N = (Tc * fs)

def DFT(x):
    N = len(x)
    tablica = []
    for n in range(0, N):
        a = 0
        for k in range(N):
            a += x[k]* m.exp(-1j *(2 * m.pi * n * k)/N)
        tablica.append(a)
    return tablica

t = []
h = []
for n in range(0, int(N)):
	t.append(n/fs)
	h.append(m.sin(2*m.pi*200*t[n]))

b = DFT(h)

widmo = []
widmoprim = []
N = int(N/2)

for i in range(N):
    image = b[i].imag
    real = b[i].real
    widmo.append(m.sqrt(real**2 + image**2))
    widmoprim.append(10 * m.log10(widmo[i]))
    

plt.plot(range(len(widmo)), widmo)
plt.show()


plot = plt.plot(range(len(widmoprim)),widmoprim)
plt.show()




    




