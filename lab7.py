from sklearn.datasets import make_classification
import numpy as np
from numpy.linalg import norm
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb
import matplotlib.colors as cl
from sklearn import datasets


def euclidean(a, b):
    return norm(a-b)


class KNearestNeighbors:

    def __init__(self, k=1, distance_metric=euclidean):
        self.k = k
        self.distance = distance_metric
        self.data = None

    def fit(self, X, y):
        if len(X) != len(y) or type(X) != type(y):
            raise ValueError("X and y are incompatible.")
        if type(X) == np.ndarray:
            X, y = X.tolist(), y.tolist()
        self.data = [X[i]+[y[i]] for i in range(len(X))]

    def predict(self, a):
        neighbors = []
        distances = {self.distance(x[:-1], a): x for x in self.data}
        for key in sorted(distances.keys())[:self.k]:
            neighbors.append(distances[key][-1])
        return max(set(neighbors), key=neighbors.count)

X, y = make_classification(n_samples=100,n_features=2,n_informative=2,n_redundant=0,n_repeated=0,random_state=3)

df = pd.DataFrame(X, columns=["PC1", "PC2"])
df = pd.concat([df, pd.DataFrame(y, columns=["target"])], axis=1)
#plt.figure(figsize=(6, 6))
#sb.scatterplot(data=df, x="PC1", y="PC2", hue="target", s=60, palette="plasma")
#plt.show()


# Zadanie 3.3
h = 0.4

cmap_light = cl.ListedColormap(['#FFAAAA', '#AAFFAA','#00AAFF'])
cmap_bold = cl.ListedColormap(['#FF0000', '#00FF00','#00AAFF'])

n_neighbors = 5

# Zadanie 3.2
clf = KNearestNeighbors(n_neighbors)
clf.fit(X, y)

x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

prediction = []
for n in np.c_[xx.ravel(), yy.ravel()]:
    prediction.append(clf.predict(n))

cmap_light = cl.ListedColormap(['yellow', 'blue', 'green'])
cmap_bold = ['darkorange', 'darkblue']

Z = np.array(prediction).reshape(np.array(xx).shape)
plt.figure()
plt.contourf(xx, yy, Z, cmap=cmap_light)

sb.scatterplot(x=X[:, 0], y=X[:, 1], hue=y, palette=cmap_bold, alpha=1.0, edgecolor="black")
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.title("Klasyfikacja(k = %i)" % n_neighbors)
plt.show()


# Zadanie 3.4/5
iris = datasets.load_iris()
X1 = iris.data
Y1 = iris.target
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X1)
nx = 50
ix_tmp = np.linspace(np.min(X_reduced,axis=0), np.max(X_reduced,axis=0), nx)
ix1_tmp, ix2_tmp = np.meshgrid(ix_tmp[:,0],ix_tmp[:,1])
ix_tmp = np.vstack((ix1_tmp.ravel(), ix2_tmp.ravel())).T
irisC = KNearestNeighbors(n_neighbors)
irisC.fit(X1, Y1)
ix_inv = pca.inverse_transform(ix_tmp)
iy_pred = []
for s in ix_inv:
    iy_pred.append(irisC.predict(s))
fnn = np.array(iy_pred).reshape(nx, nx)

cmap_light = cl.ListedColormap(['yellow', 'blue', 'green'])
cmap_bold = ['darkorange', 'darkblue']

plt.figure()
plt.contour(ix1_tmp, ix2_tmp, fnn, cmap='viridis')
plt.scatter(X_reduced[:,0], X_reduced[:,1], c=Y1, cmap='plasma', marker='.')
plt.xlim(ix1_tmp.min(), ix1_tmp.max())
plt.ylim(ix2_tmp.min(), ix2_tmp.max())
plt.title("Klasyfikacja (k = %i)" % n_neighbors)
plt.show()