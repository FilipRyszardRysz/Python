import cmath as mt

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
    widmo1.append(mt.sqrt(real**2 + image**2).real)
    widmoprim1.append(10 * mt.log10(widmo1[i]).real)


def szerokoscPasma(tabliczka, poziom):
    fmin = 0
    fmax = 0
    maks = max(tabliczka)
    poziomx = maks - poziom
    for i in range(len(tabliczka)):
        if tabliczka[i] >= poziomx and fmin == 0:
            fmin = i
        if fmin != 0 and tabliczka[i] >= poziomx:
            fmax = i
    return fmax-fmin

print(szerokoscPasma(widmoprim1, 10))
