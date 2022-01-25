import biblioteka as bobo

strumien = bobo.asciitobin("ab")
print(strumien)
Tc = 1
A = 1
A1 = 1
A2 = 2
Ar = 1
b = len(strumien)
Tb = Tc / b #s
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
h = 19

t = [x for x in range(N)]
for n in range(0, N):
    t[n] = n / Fs

ASK = bobo.ASK(Nc, Nb, b, strumien, Fs, fn, A1, A2, t)
PSK = bobo.PSK(Nc, Nb, b, strumien, Fs, fn, t)
FSK = bobo.FSK(Nc, Nb, b, strumien, Fs, fn1, fn2, t)

DemoASK = bobo.demodulatorASK(ASK, t, N, A, fn, b, Nb, h)
DemoPSK = bobo.demodulatorPSK(PSK, t, N, fn, b, Nb)
DemoFSK = bobo.demodulatorFSK(FSK, t, N, Ar, fn1, fn2, b, Nb)



print(bobo.ct_to_string(DemoASK, b, Nb))
print(bobo.ct_to_string(DemoPSK, b, Nb))
print(bobo.ct_to_string(DemoFSK, b, Nb))

    