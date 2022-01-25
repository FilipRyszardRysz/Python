import matplotlib
import matplotlib.pyplot as plt


def wielomian(x):
    wiel = 3 * x * x + 2
    return wiel

t = [x for x in range(41)]
s = [x for x in range(41)]

for x in range(-41,41):
    t[x] = wielomian(x-20)
    s[x] = x-20
    
    
wykres = plt.plot(s, t)
plt.show()



