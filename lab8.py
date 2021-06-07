import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Zadanie 1 
def distp(X, C):  #punkty X i C
    de = np.zeros([len(X), len(C)])

    for i, xi in enumerate(X):
        for k, ck in enumerate(C):
            de[i, k] = np.sqrt((xi - ck) @ np.transpose(xi - ck))

    return de

def distm(X, C, V): #punkty X i C. V to macierz kowariancji zbioru X
    dm = np.zeros([len(X), len(C)])

    for i, xi in enumerate(X):
        for k, ck in enumerate(C):
            dm[i, k] = np.sqrt((xi - ck) @ np.linalg.inv(V) @ np.transpose(xi - ck))

    return dm

# Zadanie 2
def ksrodki(X, K): #wzorce X orak liczba grup k
    n = X.shape[0]

    P = np.zeros([n, K])

    # Krok 1, wektory macierzy C są inicjowane losowo
    
    C = X[np.random.randint(n, size=K), :] #centra

    while True:
        bobo_C = C
        bobo_P = P

        P = np.zeros([n, K])

        # Krok 2. Dla każdego i oraz k:
        D = distp(X, C)

        for i in range(n):
            closest_k = np.argmin(D[i])
            P[i, closest_k] = 1

        # Krok 3. Dla kazdego k obliczyc ck
        for k in range(K):
            denominator = sum(P[i, k] for i in range(n))

            if denominator:
                C[k] = sum((P[i, k] * X[i] for i in range(n))) / denominator

        e = 0.0001
        C_bobo = np.max(C - bobo_C) >= e
        P_bobo = np.max(P - bobo_P) >= e

        # Krok 4. powtarzac kroki dopoki grupowanie sie nie ustabilizuje
        if not P_bobo and not C_bobo:
            break

    CX = [[] for k in range(K)] #sasiedztwa

    # Krok 5. kazdy obiekt xi nalezy do klasy k w przypadku gdy pik = 1
    for i in range(n):
        for k in range(K):
            if P[i, k] == 1:
                CX[k].append(X[i])

    CX = [np.array(vector) for vector in CX]

    return C, CX

#Zadanie 4 

def F(C, CX):
    m = np.mean(np.concatenate(CX, axis=0), axis=0)
    m = np.asmatrix(m)

    num = 0
    nom = 0
    n = 0

    for k in range(len(C)):
        Ck = np.asmatrix(C[k])
        num += distp(Ck, m)
        n += 1

    num /= n

    n = 0

    for k in range(len(C)):
        for x in CX[k]:
            x = np.asmatrix(x)
            Ck = np.asmatrix(C[k])
            nom += distp(x, Ck) ** 2
            n += 1

    nom /= n

    return np.ravel(num / nom)

# Zadanie 2
data = pd.read_csv("autos.csv")
data = data[["width", "height"]]
X = np.array(data)
X = X.astype(float)

k = 3

C, CX = ksrodki(X, k)
COLORS = "rgb"

#Zadanie 3
for i, cx, c in zip(range(k), CX, C):
    color = COLORS[i % len(COLORS)]
    if len(cx):
        plt.plot(cx[:, 0], cx[:, 1], "." + color, markersize=2)
            
    plt.plot(c[0], c[1], "o" + color, markersize=4)
plt.show()

# Zadanie 4
print(F(C, CX))
    


