import matplotlib.pyplot as plt
import biblioteka as bobo
import numpy as np
import math as m


print(bobo.asciitobin('aa'))
strumien = bobo.asciitobin("ab")

ka = 0.5
kp = 0.5
kf = 0.5
Tc = 1
A1 = 1
A2 = 2
b = len(strumien)
Tb = Tc / b
W = 1
fn = (W / Tb)
fn1 = (W + 1)/Tb
fn2 = (W + 2)/Tb
Fs = 560
Nc = Tc * Fs
fm = 10
Nb = int(Fs * Tb)
N = Nb * b
N1 = (N/2)

t = []
for n in range(0, N):
    t.append(n / Fs)


za = bobo.ASK(Nc, Nb, b, strumien, Fs, fn, A1, A2, t)
zp = bobo.PSK(Nc, Nb, b, strumien, Fs, fn, t)
zf = bobo.FSK(Nc, Nb, b, strumien, Fs, fn1, fn2, t)


zaAMPLITUDA = bobo.zmodulowany_amplitudowo(t, za, ka, fn)
zpFAZA = bobo.modulacja_fazy(t, zp, fn, kp)
zfCZESTOTLIWOSC = bobo.modulacja_czestotliwosci(t, zf, kf, fm, fn)


zaFFT = np.fft.fft(zaAMPLITUDA)
zpFFT = np.fft.fft(zpFAZA)
zfFFT = np.fft.fft(zfCZESTOTLIWOSC)

wartosci_za_FFT = []
widmo = []

for i in range(int(N1)):
    image = zaFFT[i].imag
    real = zaFFT[i].real
    widmo.append(m.sqrt(real**2 + image**2))
    wartosci_za_FFT.append(10 * m.log10(widmo[i]))
    
wartosci_zp_FFT = []
widmo1 = []

for i in range(int(N1)):
    image = zpFFT[i].imag
    real = zpFFT[i].real
    widmo1.append(m.sqrt(real**2 + image**2))
    wartosci_zp_FFT.append(10 * m.log10(widmo1[i]))

wartosci_zf_FFT = []
widmo2 = []

for i in range(int(N1)):
    image = zfFFT[i].imag
    real = zfFFT[i].real
    widmo2.append(m.sqrt(real**2 + image**2))
    wartosci_zf_FFT.append(10 * m.log10(widmo2[i]))

plt.plot(range(len(wartosci_za_FFT)), wartosci_za_FFT)
plt.title("Widmo ASK")
plt.show()

plt.plot(range(len(wartosci_zp_FFT)), wartosci_zp_FFT)
plt.title("Widmo PSK")
plt.show()

plt.plot(range(len(wartosci_zf_FFT)), wartosci_zf_FFT)
plt.title("Widmo FSK")
plt.show()