import cmath as m

x = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

def DFT(x):
    tablica = []
    N = len(x)
    for n in range(0, N):
        a = 0
        for k in range(N):
            a += x[k]* m.exp(-1j *(2 * m.pi * n * k)/N)
        tablica.append(a)
    return tablica

print(DFT(x))