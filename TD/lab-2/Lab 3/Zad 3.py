import cmath as m
import matplotlib.pyplot as plt


f=1
fi=0
fs=8192 #hz
Tc=1
Ts=1/fs
N=(Tc/Ts)
N1 = 22050


def DFT(x):
    tablica = []
    N = len(x)
    for n in range(0, N):
        a = 0
        for k in range(N):
            a += x[k]* m.exp(-1j *(2 * m.pi * n * k)/N)
        tablica.append(a)
    return tablica


t = []
x = []
y = []
z = []
v = []
u = []
b1 =[]
b2 =[]
b3 =[]
for n in range(0, int(N)):
        t.append(n/fs)
        x.append(m.sin(2 * m.pi * f * t[n] * m.cos(3 * m.pi * t[n]) + t[n] * fi))
        y.append((x[n] * t[n]*t[n]*t[n])/3)
        z.append(1.92 * (m.cos(3*m.pi * t[n]/2) + m.cos((y[n]*y[n])/8*x[n]+3)*t[n]))
        v.append((((y[n] * z[n])/(x[n]+2))*m.cos(7.2*m.pi+m.sin(m.pi*t[n]*t[n]))))
        t[n] = n/fs
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

widmo11 = []
widmo12 = []
widmo13 = []
widmo14 = []
widmo15 = []
widmo16 = []
widmo17 = []
widmo18 = []

widmo1 = DFT(x)
widmo2 = DFT(y)
widmo3 = DFT(z)
widmo4 = DFT(v)
widmo5 = DFT(u)
widmo6 = DFT(b1)
widmo7 = DFT(b2)
widmo8 = DFT(b3)

for i in range(int(N)):
    widmo11.append(m.sqrt((widmo1[i].real)**2 + (widmo1[i].imag)**2))
    widmo12.append(m.sqrt((widmo2[i].real)**2 + (widmo2[i].imag)**2))
    widmo13.append(m.sqrt((widmo3[i].real)**2 + (widmo3[i].imag)**2))
    widmo14.append(m.sqrt((widmo4[i].real)**2 + (widmo4[i].imag)**2))
    widmo15.append(m.sqrt((widmo5[i].real)**2 + (widmo5[i].imag)**2))
for i in range(int(N1)):
    widmo16.append(m.sqrt((widmo6[i].real)**2 + (widmo6[i].imag)**2))
    widmo17.append(m.sqrt((widmo7[i].real)**2 + (widmo7[i].imag)**2))
    widmo18.append(m.sqrt((widmo8[i].real)**2 + (widmo8[i].imag)**2))
    
plt.plot(range(len(widmo11)), widmo11)
plt.title('Widmo z wykresu x')
plt.show()

plt.plot(range(len(widmo12)), widmo12)
plt.title('Widmo z wykresu y')
plt.show()

plt.plot(range(len(widmo13)), widmo13)
plt.title('Widmo z wykresu z')
plt.show()

plt.plot(range(len(widmo14)), widmo14)
plt.title('Widmo z wykresu v')
plt.show()

plt.plot(range(len(widmo15)), widmo15)
plt.title('Widmo z wykresu u')
plt.show()

plt.plot(range(len(widmo16)), widmo16)
plt.title('Widmo z wykresu b1')
plt.show()

plt.plot(range(len(widmo17)), widmo17)
plt.title('Widmo z wykresu b2')
plt.show()

plt.plot(range(len(widmo18)), widmo18)
plt.title('Widmo z wykresu b3')
plt.show()