import cmath as m
import numpy as np
import matplotlib.pyplot as plt


def dyskretyzacja(f, Fs):    
    Tc = 1
    Ts = 1/Fs
    N = Tc/Ts
    t = []
    s = []
    for n in range(0, int(N)):
        t.append(n/Fs)
        s.append(m.sin(2* m.pi * f * t[n]))
    return t, s

t, s = dyskretyzacja(10,20)
plot = plt.plot(t, s)
plt.show()

t, s = dyskretyzacja(10,21)
plot = plt.plot(t, s)
plt.show()

t, s = dyskretyzacja(10,30)
plot = plt.plot(t, s)
plt.show()

t, s = dyskretyzacja(10,45)
plot = plt.plot(t, s)
plt.show()

t, s = dyskretyzacja(10,50)
plot = plt.plot(t, s)
plt.show()

t, s = dyskretyzacja(10,100)
plot = plt.plot(t, s)
plt.show()

t, s = dyskretyzacja(10,150)
plot = plt.plot(t, s)
plt.show()

t, s = dyskretyzacja(10,200)
plot = plt.plot(t, s)
plt.show()

t, s = dyskretyzacja(10,250)
plot = plt.plot(t, s)
plt.show()

t, s = dyskretyzacja(10,1000)
plot = plt.plot(t, s)
plt.show()

#Twierdzenie o próbkowaniu, twierdzenie Nyquista–Shannona[a] – fundamentalne twierdzenie 
#teorii informacji, telekomunikacji oraz cyfrowego przetwarzania sygnałów opisujące matematyczne 
#podstawy procesów próbkowania sygnałów oraz ich rekonstrukcji

#Aliasing – nieodwracalne zniekształcenie sygnału w procesie próbkowania wynikające z 
#niespełnienia założeń twierdzenia o próbkowaniu. Zniekształcenie objawia się obecnością w 
#wynikowym sygnale składowych o błędnych częstotliwościach (aliasów).

#Zadanie 6

image = plt.imread("bricks.png") # wczytywanie obrazka
grid = image[::20,::20]          # 100 krotna redukcja rezdzielczosci

#Zadanie 7
methods = [None, 'none', 'nearest', 'bilinear', 'bicubic', 'spline16',
           'spline36', 'hanning', 'hamming', 'hermite', 'kaiser', 'quadric',
           'catrom', 'gaussian', 'bessel', 'mitchell', 'sinc', 'lanczos']



fig, axs = plt.subplots(nrows=3, ncols=6, figsize=(9, 6),
                        subplot_kw={'xticks': [], 'yticks': []})

for ax, interp_method in zip(axs.flat, methods):
    ax.imshow(grid, interpolation=interp_method, cmap='viridis')
    ax.set_title(str(interp_method))

plt.tight_layout()
plt.show()




#Kwantyzacja
#Zadanie 1

image = plt.imread("bricks.png")

#Zadanie 2
print(image.shape, "\n")

#Zadanie 3
print(image.shape[2], "\n")

#Zadanie 4
jasnosc = ((image[:,:].max(axis=-1) + image[:,:].min(axis=-1)) / 2)
#print(jasnosc, '\n')
sredni =  image[:,:].sum(axis=-1) / 3
#print(sredni, '\n')
luminancja = image[:,:,0] * 0.21 + image[:,:,1] * 0.72 + image[:,:,2] * 0.07
#print(luminancja, '\n')

#Zadanie 5
histogram1 = np.histogram(jasnosc)
histogram2 = np.histogram(sredni)
histogram3 = np.histogram(luminancja)


#Zadanie 6
histogram11 = np.histogram(jasnosc, bins=16)
histogram22 = np.histogram(sredni, bins=16)
histogram33 = np.histogram(luminancja, bins=16)


#Zadanie 8
baba = plt.hist(jasnosc.ravel())
plt.title("jasności")
plt.show()
plt.imshow(jasnosc, cmap = plt.get_cmap(name = 'gray'))
plt.show()

bobo = plt.hist(sredni.ravel())
plt.title("sredni")
plt.show()
plt.imshow(sredni, cmap = plt.get_cmap(name = 'gray'))
plt.show()

bibi = plt.hist(luminancja.ravel())
plt.title("luminancja")
plt.show()
plt.imshow(luminancja, cmap = plt.get_cmap(name = 'gray'))
plt.show()


#Zadanie 1
image = plt.imread("lew.png") # wczytywanie obrazka

#zadanie 2
sredni =  image[:,:].sum(axis=-1) / 3
bobo = plt.hist(sredni.ravel(), bins=250)
plt.title("Lew")
plt.show()

plt.imshow(sredni, cmap = plt.get_cmap(name = 'gray'))
plt.show()
plt.imshow(image)