import cmath as mt
import matplotlib.pyplot as plt

fn = 100
fm = 5
ka = 0.5
kf = 0.5
kp = 0.5
fs = 1000
Tc = 1.0
Ts = 1/fs
N = Tc/Ts

def sygnał_informacyjny(t):
    return mt.sin(2*mt.pi*fm*t)

def zmodulowany_amplitudowo(t):
    return (ka*sygnał_informacyjny(t)+1) * mt.cos(2*mt.pi*fn*t)

def modulacja_fazy(t):
    return mt.cos(2*mt.pi * fn*t + kp * sygnał_informacyjny(t))

def modulacja_czestotliwosci(t):
    return mt.cos(2*mt.pi*fn*t+(kf/fm)*sygnał_informacyjny(t))

t = []
informacyjny = []
amplitudowo = []
fazy = []
czestotliwosci = []

for n in range(0, int(N)):
    t.append(n/fs)
    informacyjny.append(sygnał_informacyjny(t[n]))
    amplitudowo.append(zmodulowany_amplitudowo(t[n]))
    fazy.append(modulacja_fazy(t[n]))
    czestotliwosci.append(modulacja_czestotliwosci(t[n]))
    
wykres = plt.plot(t, informacyjny)
plt.show()
wykres = plt.plot(t, amplitudowo)
plt.show()
wykres = plt.plot(t, fazy)
plt.show()
wykres = plt.plot(t, czestotliwosci)
plt.show()

    

