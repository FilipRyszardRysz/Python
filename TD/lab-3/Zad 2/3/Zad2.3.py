import cmath as mt
import matplotlib.pyplot as plt

fn = 250
fm = 10
kf = 4
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

def modulacja_czestotliwosci(t):
    return mt.cos(2*mt.pi*fn*t+(kf/fm)*sygnał_informacyjny(t))

N = Tc/Ts
t = []
informacyjny = []
czestotliwosci = []

for n in range(0, int(N)):
    t.append(n/fs)
    informacyjny.append(sygnał_informacyjny(t[n]))
    czestotliwosci.append(modulacja_czestotliwosci(t[n]))
N = N/2
widmo3 = []
widmoprim3 = []
e = DFT(czestotliwosci)
for i in range(int(N)):
    image = e[i].imag
    real = e[i].real
    widmo3.append(mt.sqrt(real**2 + image**2))
    widmoprim3.append(10 * mt.log10(widmo3[i]))
    
wykres = plt.plot(range(len(widmo3)), widmo3)
plt.title('Widmo modulacji częstotliwosci')
plt.show()
wykres = plt.plot(range(len(widmoprim3)), widmoprim3)
plt.title('Widmo w skali decybelowej modulacji częstotliwosci')
plt.show()