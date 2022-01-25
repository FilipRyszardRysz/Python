import biblioteka as bobo

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
Fs = 1000
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

