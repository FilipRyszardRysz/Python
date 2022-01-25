import matplotlib.pyplot as plt
import math as m

f=1
fi=0
fs=8000 #hz
Tc=1
Ts=1/fs
N=(Tc*fs)
a = m.sin
b = m.cos
t = [x for x in range(int(N))]
s = [x for x in range(int(N))]


for n in range(0, int(N)):
	t[n] = n/fs
	s[n] = a(2 * m.pi * f * t[n] * b(3 * m.pi * t[n]) + t[n] * fi)


