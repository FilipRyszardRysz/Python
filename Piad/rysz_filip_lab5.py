import numpy as np
import pandas as pd
import math as m

zoo = pd.read_csv('zoo.csv')

#Zadanie 1
def freq(x, prob=True):
    xi, pi = np.unique(x, return_counts=True)
    if prob==True:
        pi = pi / sum(pi)
    return xi, pi

#Zadanie 2
def freq2(x, y, prob=True):
    ni = {}
    for i,j in zip(x,y):
        if (i,j) in ni:
            ni[(i,j)] += 1
        else:
            ni[(i,j)] = 1
    if prob:
        for k, v in ni.items():
            ni[k] = v/(len(x))
    return ni

print("Nogi: ")
xi, pi = freq(zoo['legs'], "\n")
print(pi, xi, "\n")

slownik = freq2(zoo['animal'], zoo['type'])
print(slownik, '\n')

#Zadanie 3
def entropy1(x):
    xi, licznosc = freq(x) #liczymy true/false
    suma = 0
    for p in licznosc: 
        if p != 0:
            suma += p*m.log2(p) #wzorek na entropie
    suma = suma * (-1) #tez ze wzorku 
    return suma

def entropy2(x, y):
    licznosc = freq2(x, y) #liczymy true/false
    suma = 0
    for p in licznosc.values(): 
        if p != 0: 
            suma += p*m.log2(p) #wzorek na entropie
    suma = suma * (-1) #tez ze wzorku 
    return suma

def infogain(x,y):
    return entropy1(x) + entropy1(y) - entropy2(x,y)

print(entropy1(zoo['hair']))
print(infogain(zoo['legs'], zoo['type']))

#Zadanie 4
typ = []
przyrost = []
for i in zoo.columns[:-1]:
    typ.append(i)
    przyrost.append(infogain(zoo[i], zoo['type']))

bobo = pd.DataFrame({ 'Typ': typ, 'przyrost': przyrost})
print(bobo.sort_values(by=['przyrost'], ascending=False))



