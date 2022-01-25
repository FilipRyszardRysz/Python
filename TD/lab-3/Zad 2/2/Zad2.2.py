import cmath as mt
import matplotlib.pyplot as plt

fn = 250
fm = 10
kp = 2
fs = 1000
Tc = 1.0
fi = 0
n = Tc * fs
Ts = 1/fs

def DFT(x):
    N = len(x)
    tablica = []
    for n in range(0, N):
        a = 0
        for k in range(N):
            a += x[k]* mt.exp(-1j *(2 * mt.pi * n * k)/N)
        tablica.append(a)
    return tablica

def sygnał_informacyjny(t):
    return mt.sin(2*mt.pi*fm*t)

def modulacja_fazy(t):
    return mt.cos(2*mt.pi * fn*t + kp * sygnał_informacyjny(t))

N = Tc/Ts
t = []
informacyjny = []
fazy = []

for n in range(0, int(N)):
    t.append(n/fs)
    informacyjny.append(sygnał_informacyjny(t[n]))
    fazy.append(modulacja_fazy(t[n]))
N = N/2
widmo2 = []
widmoprim2 = []
d = DFT(fazy)
for i in range(int(N)):
    image = d[i].imag
    real = d[i].real
    widmo2.append(mt.sqrt(real**2 + image**2))
    widmoprim2.append(10 * mt.log10(widmo2[i]))

wykres = plt.plot(range(len(widmo2)), widmo2)
plt.title('Widmo modulacji fazy')
plt.show()
wykres = plt.plot(range(len(widmoprim2)), widmoprim2)
plt.title('Widmo w skali decybelowej modulacji fazy')
plt.show()
    