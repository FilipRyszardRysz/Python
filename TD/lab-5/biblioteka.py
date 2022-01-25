import math as m
import matplotlib.pyplot as plt

def ASK(Nc, Nb, B, bity, fs, fn, A1, A2, t):
    ASK = []
    counter = 0
    for i in range(B):
        for j in range(Nb):
            if bity[i]==0:
                ASK.append(A1 * m.sin(2 * m.pi * fn * (counter/fs)))
            if bity[i]==1:
                ASK.append(A2 * m.sin(2 * m.pi * fn * (counter/fs)))
            counter += 1
    plt.plot(t, ASK)
    plt.title('ASK')
    plt.show()
    return ASK

def PSK(Nc, Nb, B, bity, fs, fn, t):        
    PSK = []
    counter = 0
    for i in range(B):
        for j in range(0, Nb):
            if bity[i]==0:
                PSK.append(m.sin(2 * m.pi * fn * (counter/fs)))
            if bity[i]==1:
                PSK.append(m.sin(2 * m.pi * fn * (counter/fs) + m.pi))
            counter += 1
    plt.plot(t, PSK)
    plt.title('PSK')
    plt.show()
    return PSK


def FSK(Nc, Nb, B, bity, fs, fn1, fn2, t):           
    FSK = []
    counter = 0
    for i in range(B):
        for j in range(Nb):
            #tbprobka = j/fs
            if bity[i]==0:
                FSK.append(m.sin(2 * m.pi * fn1 * t[counter]))
            if bity[i]==1:
                FSK.append(m.sin(2 * m.pi * fn2 * t[counter]))
            counter +=1
    plt.plot(t, FSK)
    plt.title('FSK')
    plt.show()
    return FSK

def DFT(x):
    N = len(x)
    tablica = []
    for n in range(0, N):
        a = 0
        for k in range(N):
            a += x[k]* m.exp(-1j *(2 * m.pi * n * k)/N)
        tablica.append(a)
    return tablica

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

def sygnał_informacyjny(t, fm):
    return m.sin(2*m.pi*fm*t)

def zmodulowany_amplitudowo(t, tab, ka, fn):
    y = [x for x in range(len(t))]
    for n in range(len(t)):
        y[n] = (ka*tab[n]+1) * m.cos(2*m.pi*fn*t[n])
    return y

def modulacja_fazy(t, tab, fn, kp):
    y = [x for x in range(len(t))]
    for n in range(len(t)):
        y[n] = (m.cos(2*m.pi * fn * t[n] + kp * tab[n]))
    return y

def modulacja_czestotliwosci(t, tab, kf, fm, fn):
    y = [x for x in range(len(t))]
    for n in range(len(t)):
        y[n] = (m.cos(2*m.pi*fn*t[n]+(kf/fm)*tab[n]))
    return y

def demodulatorFSK(za, t, N, Ar, fn1, fn2, b, Nb):
    x1=[]
    x2=[]
    p1=[]
    p2=[]
    p=[]
    ct=[]

    for n in range(len(za)):
        x1.append((za[n])*(Ar*m.sin(2*m.pi*fn1*t[n])))
        x2.append((za[n])*(Ar*m.sin(2*m.pi*fn2*t[n])))
    plt.plot(t, x1)
    plt.title('Demodulator FSK x1')
    plt.show()
    plt.plot(t, x2)
    plt.title('Demodulator FSK x2')
    plt.show()
    for n in range(int(len(x1)/Nb)):
        S1=0
        S2=0
        for i in range(Nb):
            S1+= x1[n*Nb+i]
            S2+= x2[n*Nb+i]
            p1.append(S1)
            p2.append(S2)
            p.append(-1 * S1 + S2)
    plt.plot(t, p1)
    plt.title('Demodulator FSK p1')
    plt.show()
    plt.plot(t, p2)
    plt.title('Demodulator FSK p2')
    plt.show()
    plt.plot(t, p)
    plt.title('Demodulator FSK pt')
    plt.show()

    ct = []
    for n in range(0, N):
        if p[n] > 0:
            ct.append(1)
        else:
            ct.append(0)
    plt.plot(t, ct)
    plt.title('Demodulator FSK ct')
    plt.show()

    return ct

def demodulatorPSK(za, t, N, fn, b, Nb):

    xt = []
    for n in range(0, N):
        xt.append(za[n] * (m.sin(2 * m.pi * fn * t[n])))
    plt.plot(t, xt)
    plt.title('Demodulator PSK xt')
    plt.show()


    # x(t) to p(t)
    pt = []
    for n in range(0, b):
        s = 0
        for i in range(0, Nb):
            s += xt[i + Nb * n]
            pt.append(s)
    plt.plot(t, pt)
    plt.title('Demodulator PSK pt')
    plt.show()


    ct = []
    for n in range(0, N):
        if pt[n] < 0:
            ct.append(1)
        else:
            ct.append(0)
    plt.plot(t, ct)
    plt.title('Demodulator PSK ct')
    plt.show()

    return ct


def demodulatorASK(za, t, N, A, fn, b, Nb, h):

    xt = []
    for n in range(0, N):
        xt.append(za[n] * (A * m.sin(2 * m.pi * fn * t[n])))
    plt.plot(t, xt)
    plt.title('Demodulator ASK xt')
    plt.show()
    # x(t) to p(t)
    pt = []
    for n in range(0, b):
        s = 0
        for i in range(0, Nb):
            s += xt[i + Nb * n]
            pt.append(s)
    plt.plot(t, pt)
    plt.title('Demodulator ASK pt')
    plt.show()

    ct = []
    for n in range(0, N):
        if pt[n] > h:
            ct.append(1)
        else:
            ct.append(0)
    plt.plot(t, ct)
    plt.title('Demodulator ASK ct')
    plt.show()
    return ct

def ct_to_string(ct, b, Nb):
    cts = []
    for n in range(0, b):
        zero = 0
        jeden = 0
        for i in range(Nb):
            if(ct[i+n*Nb] == 0):
                zero += 1
            else: 
                jeden += 1
        if zero > jeden:
            cts.append(0)
        else:
            cts.append(1)
    return cts


def asciitobin(text):
    tablica = []
    literki = []
    for i in range(len(text)):
        z = ord(text[i])
        for n in range(7):
            x = z & 1
            z = z >> 1
            literki.append(x)
        literki.reverse()
        for i in range(7):
            tablica.append(literki[i])
    return tablica