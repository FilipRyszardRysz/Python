import cmath as mt
import matplotlib.pyplot as plt

fn = 250
fm = 10
ka = 0.5
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

def zmodulowany_amplitudowo(t):
    return (ka*sygnał_informacyjny(t)+1) * mt.cos(2*mt.pi*fn*t)

N = Tc/Ts
t = []
informacyjny = []
amplitudowo = []

for n in range(0, int(N)):
    t.append(n/fs)
    informacyjny.append(sygnał_informacyjny(t[n]))
    amplitudowo.append(zmodulowany_amplitudowo(t[n]))
N = N/2
widmo1 = []
widmoprim1 = []
c = DFT(amplitudowo)
for i in range(int(N)):
    image = c[i].imag
    real = c[i].real
    widmo1.append(mt.sqrt(real**2 + image**2))
    widmoprim1.append(10 * mt.log10(widmo1[i]))
    
wykres = plt.plot(range(len(widmo1)), widmo1)
plt.title('Widmo sygnału amplitudowego')
plt.show()
wykres = plt.plot(range(len(widmoprim1)), widmoprim1)
plt.title('Widmo w skali decybelowej sygnału amplitudowego')
plt.show()