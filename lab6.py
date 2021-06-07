from sklearn import datasets
import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb


def bobopca(data, n):
    mean = np.mean(data, 0)
    new_matrix = data - mean
    covariance_matrix = np.cov(np.transpose(new_matrix))
    w, v = LA.eig(covariance_matrix)
    U_Truncated = v[:, :n]
    U_Truncated_Transpose = np.transpose(U_Truncated)
    new_dimension_matrix = np.dot(U_Truncated_Transpose, np.transpose(new_matrix))
    newData = np.transpose(new_dimension_matrix)
    val = (-w).argsort()[:n]
    nowe = newData * (-1)
    wynik = v[..., val]
    return w, v, mean, wynik.T, nowe


def draw_vector(v0, v1, ax=None):
    ax = ax or plt.gca()
    arrowprops=dict(arrowstyle='->', linewidth=2, shrinkA=0, shrinkB=0)
    ax.annotate('', v1, v0, arrowprops=arrowprops)

def inversePCA(X_r, comps, m=None):
    if m is not None:
        return np.dot(X_r, comps.T) + m
    return np.dot(X_r, comps.T) + X_r.mean(axis=0)


    
#1
rng = np.random.RandomState(1)
X = np.dot(rng.rand(2, 2), rng.randn(2, 200)).T
plt.scatter(X[:, 0], X[:, 1])
plt.axis('equal')
plt.title("Zad 1")
plt.show()

x1, y1, mmean, res, WipcaD = bobopca(X, 1)

plt.scatter(X[:, 0], X[:, 1], alpha=0.2)
for length, vector in zip(x1.T, y1.T):
    v = vector * 3 * np.sqrt(length)
    draw_vector(mmean, mmean + v)
plt.axis('equal')
WipcaINV = inversePCA(WipcaD, res.T, mmean)
plt.scatter(X[:, 0], X[:, 1], alpha=0.2)
plt.scatter(WipcaINV[:, 0], WipcaINV[:, 1], alpha=0.8)
plt.axis('equal')
plt.title("C")
plt.show()

#2
iris = datasets.load_iris()
X = iris.data
Y = iris.target
wi = bobopca(X,2)[4]
df = pd.DataFrame(wi, columns=["PC1", "PC2"])
df = pd.concat([df,pd.DataFrame(Y,columns=["target"])], axis=1)
plt.figure(figsize=(6,6))
sb.scatterplot(data=df,x="PC1", y="PC2", hue="target", s=60, palette="magma")
plt.title("Zad 2")
plt.show()

#3
from sklearn.datasets import load_digits
digits = load_digits()
digits.data.shape

dx, dy, dmean, dres, dwipca = bobopca(digits.data, 2)
sumka = np.cumsum(dx)
plt.plot(sumka/sumka.max())
plt.xlabel("number of components")
plt.ylabel("cumulative explained varianceration ")
plt.title("Zad 3c")
plt.show()

projected = (digits.data)
plt.scatter(dwipca[:, 0], dwipca[:,1], c = digits.target, edgecolor ='none', alpha = 0.5, cmap = plt.cm.get_cmap('magma', 10))
plt.xlabel('c1')
plt.ylabel('c2')
plt.title("Zad 3d")
plt.show()