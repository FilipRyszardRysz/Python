import cmath as m
import time
import numpy as np
from numba import njit

f=1
fi=0
fs=8000 #hz
Tc=1
Ts=1/fs
N=(Tc/Ts)
N1 = 22050

t = []
x = []
y = []
z = []
v = []
u = []
b1 =[]
b2 =[]
b3 =[]
@njit
def DFT(x):
    N = len(x)
    tablica = []
    for n in range(0, N):
        a = 0
        for k in range(N):
            a += x[k]* m.exp(-1j *(2 * m.pi * n * k)/N)
        tablica.append(a)
    return tablica

for n in range(0, int(N)):
        t.append(n/fs)
        x.append(m.sin(2 * m.pi * f * t[n] * m.cos(3 * m.pi * t[n]) + t[n] * fi))
        y.append((x[n] * t[n]*t[n]*t[n])/3)
        z.append(1.92 * (m.cos(3*m.pi * t[n]/2) + m.cos((y[n]*y[n])/8*x[n]+3)*t[n]))
        v.append((((y[n] * z[n])/(x[n]+2))*m.cos(7.2*m.pi+m.sin(m.pi*t[n]*t[n]))))
        if (t[n] < 0.1) and (t[n] >= 0):
            u.append(m.sin(6*m.pi *t[n])*m.cos(5*m.pi*t[n]))
        if (t[n] < 0.4) and (t[n] >= 0.1):
            u.append(-1.1* t[n]*m.cos(41*m.pi * (t[n] * t[n])))
        if (t[n] < 0.72) and (t[n] >= 0.4):
            u.append(t[n] * m.sin(20 * (t[n]*t[n]*t[n]*t[n])))
        if (t[n] < 1) and (t[n] >= 0.72):
            u.append(3.3*(t[n]-0.72)*m.cos(27 * t[n] + 1.3))

q = 0.0
w = 0.0
e = 0.0

for n in range(0, int(N1)):
    t.append(n/fs)
    for i in range(1, 2):
        q += ((m.cos(12 * t[n] * i**2) + m.cos(16*t[n]*i)) / i**2)
    b1.append(q)
    q = 0.0
    for i in range(1, 4):
        w += ((m.cos(12 * t[n] * i**2) + m.cos(16*t[n]*i)) / i**2) 
    b2.append(w)
    w = 0.0
    for i in range(1, 16):
        e += ((m.cos(12 * t[n] * i**2) + m.cos(16*t[n]*i)) / i**2)
    b3.append(e)
    e = 0.0
    
s = time.time()
c = DFT(b3)
f = time.time()
print("Czas wykonania DFT: ", f-s)

s = time.time()
c = np.fft.fft(b3)
f = time.time()
print("Czas wykonania FFT: ", f-s)

