import biblioteka as bobo
import numpy as np

strumien = bobo.asciitobin("a")

def hamm_7_4(wejscie):
    n = 7
    k = 4
    m = n - k
    kod = [0 for i in range(n)]
    
    kod[2] = wejscie[0]
    kod[4] = wejscie[1]
    kod[5] = wejscie[2] 
    kod[6] = wejscie[3]
    kod[0] = (((kod[2] + kod[4])%2) + kod[6]) % 2
    kod[1] = (((kod[2] + kod[5])%2) + kod[6]) % 2
    kod[3] = (((kod[4] + kod[5])%2) + kod[6]) % 2
    return kod
    

def hamm_dek_7_4(kod):
    x1 = (kod[2] + kod[4] + kod[6]) % 2
    x2 = (kod[2] + kod[5] + kod[6]) % 2
    x4 = (kod[4] + kod[5] + kod[6]) % 2 

    kod1 = (kod[0] + x1) % 2
    kod2 = (kod[1] + x2) % 2
    kod4 = (kod[3] + x4) % 2
    S = kod1 * 2**0 + kod2 * 2**1 + kod4 * 2**2
    
    if (S!=0):
        print("Korekcja bitu: ", S)
        if (kod[S] == 0):
            kod[S] = 1
        else:
            kod[S] = 0
    else:
        print("Brak bitu do korekcji")
    return kod

wejscie = [1,1,0,1]
print(hamm_7_4(wejscie))
print(hamm_dek_7_4(hamm_7_4(wejscie)))



def hamm_15_11(wejscie1):
    macierz_i = np.eye(11)
    #print(macierz_i)
    macierz_p = np.array([[1,1,0,0],
                  [1,0,1,0],
                  [0,1,1,0],
                  [1,1,1,0],
                  [1,0,0,1],
                  [0,1,0,1],
                  [1,1,0,1],
                  [0,0,1,1],
                  [1,0,1,1],
                  [0,1,1,1],
                  [1,1,1,1]]
                 )
    macierz_g = np.hstack((macierz_p, macierz_i))
    #print(macierz_g)
    c = np.dot(wejscie1, macierz_g)
    return c%2

wejscie1 = [1,1,0,1,1,1,0,1,1,1,0]
#print(hamm_15_11(wejscie1))

def hamm_dek_15_11(kod1):
    macierz_i=np.eye(4)
    macierz_p = np.array([[1,1,0,0],
                  [1,0,1,0],
                  [0,1,1,0],
                  [1,1,1,0],
                  [1,0,0,1],
                  [0,1,0,1],
                  [1,1,0,1],
                  [0,0,1,1],
                  [1,0,1,1],
                  [0,1,1,1],
                  [1,1,1,1]]
                 )
    macierz_h = np.hstack((macierz_i,macierz_p.transpose()))
    macierz_s = np.dot(kod1, macierz_h.transpose())%2
    s = macierz_s[::-1]
    b = ''
    for i in s:
        b += str(int(i))
    s = int(b,2)
    if (s!=0):
        print("Korekcja bitu: ", s-1)
        if (kod1[s-1] == 0):
            kod1[s-1] = 1
        else:
            kod1[s-1] = 0
    else:
        print("Brak bitu do korekcji")
    return kod1

bobo = hamm_15_11(wejscie1)
print(hamm_dek_15_11(bobo))
    