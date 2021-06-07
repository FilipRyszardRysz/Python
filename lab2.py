import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

#Manipulowanie danymi:
#Zapoznaj się z obiektem ’pandas.DataFrame’ i utwórz:
#tabelę złożoną z liczb losowych przedziału normalnego złożoną z trzech
#kolumn z nagłówkiem (A,B,C) i pięciu wierszy z indeksem o nazwie
#”data” złożonym z dat w przedziale od 2020-03-01 do 2020-03-05 np.

#dates = pd.date_range("20200301", periods=5)
#df = pd.DataFrame(np.random.normal(0, 1,(5,3)), index=dates, columns=list("ABC"))
#df.index.name = 'DATA'
#print(df)

#Wygeneruj tabelę złożoną z liczb losowych i indeksie ”id” w formacie
#’integer’ złożoną z 20 wierszy i trzech kolumn (’A’,’B’,’C’). Następnie:

#df1 = pd.DataFrame(np.random.randn(20,3),
#                    index=list(range(1,21,1)),
#                    columns=list("ABC"))
#df1.index.name = 'ID'
#print("Tabela: \n", df1, "\n")
#print("3 pierwsze wiersze: \n", df1.iloc[0:3,:], "\n")
#print("3 ostatnie wiersze: \n", df1.iloc[17:21,:], "\n")
#print("Indeksy tabeli: \n", df1.index, "\n")
#print("Nazwy kolumn: \n", df1.columns , "\n")

#df2 = df1.rename(columns={'A':'','B':'', 'C':''})
#df2.index=[''] * len(df1)
#print("Dane bez indeksów i nazw kolumn: \n", df2, "\n")
#print("5 losowo wybranych wierszy: \n", df1.sample(5) , "\n")
#print("Wartosci kolumny A: \n", df1['A'], "\n")
#print("Wartosci kolumny A i B: \n ", df1[['A','B']] , "\n")
#print("3 pierwsze wartosci kolumny A i B: \n", df1.head(3)[['A','B']], "\n")
#print("Wiersz piąty: \n", df1.iloc[5,:], "\n")
#print("Wiersz 0, 5, 6, 7 i kolumny 1 i 2: \n", df1.iloc[[0,5,6,7], [1,2]], "\n")

#Zapoznaj się z funkcją ’describe’ i wyświetl podstawowe statystyki tabeli:
#print(df1[df1>0])
#print(df1.A[df1.A>0], df1.B[df1.B>0], df1.C[df1.C>0])
#print("Średnia kolumny A: \n", df1["A"].mean())
#print("Średnia wierszy: \n", df1.mean(axis=1))

# Zapoznaj się z funkcją ’concat’. Utwórz dwie dowlone tabele i połącz je ze sobą.
#tab1 = pd.DataFrame(np.random.randn(3,2),
#                    index=list(range(1,4,1)),
#                    columns=list("AB"))
#tab2 = pd.DataFrame(np.random.randn(2,3),
#                    index=list(range(1,3,1)),
#                    columns=list("CDE"))
#print(tab1, "\n")
#print(tab2, "\n")
#bobo = pd.concat([tab1, tab2])
#print(bobo.transpose())

#Sortowanie
#df = pd.DataFrame(data={'x':[1, 2, 3, 4, 5], 'y':['a', 'b', 'a', 'b', 'b']}, index=np.arange(5))
#df.index.name = "ID"
#print(df)
#print(df.sort_values(by='y', ascending=False))


df = pd.DataFrame(data={'x':[1, 2, 3, 4, 5], 'y':['a', 'b', 'a', 'b', 'b']}, index=np.arange(5))

#Zadanie 1
#print(df.groupby('y').mean(), '\n')

#Zadanie 2
#print(df.value_counts())

#Zadanie 3
pd.read_csv('autos.csv')
np.loadtxt('autos.csv', dtype=str)
#pandasy sama zgaduej typy, natomiast przy loadtekscie trzbea podawac typ danych

#Zadanie 4
df1 = pd.read_csv('autos.csv')
#print(df1.groupby('make')['city-mpg','highway-mpg'].mean())

#Zadanie 5
#print(df1.groupby("make")["fuel-type"].value_counts())

#Zadanie 6
p1 = np.polyfit(df1["length"], df1["city-mpg"],1)
print(np.polyval(p1, 1))
p2 = np.polyfit(df1["length"], df1["city-mpg"],2)
print(np.polyval(p2, 2))
a=np.polyval(p1, np.linspace(df1['length'].min(),df1['length'].max(), 100))


#Zadanie 7
corr = stats.pearsonr(df1["city-mpg"], df1["highway-mpg"])
print(corr)

#Zadanie 8

plt.plot(df1["length"], df1["city-mpg"],linestyle="",marker='.',label="Samples")
plt.plot(np.linspace(df1['length'].min(),df1['length'].max(), 100), a, '-g')
plt.show()

#Zadanie 9
gaussian_kde = stats.gaussian_kde(df1['length'].values)
x = np.linspace(df1['length'].min(), df1['length'].max(), 100)
density = gaussian_kde.evaluate(x)

fig, ax = plt.subplots()
plt.hist(df1['length'], color='pink', edgecolor='k', density=True)
plt.plot(x, density, '-g', markeredgecolor='k')
plt.plot(df1['length'],  gaussian_kde.evaluate(df1['length']), '.k', markeredgecolor='k')
plt.show()

# Zadanie 10
plt.subplot(1,2,1)
plt.hist(df1['height'], edgecolor='k', color='red')
plt.subplot(1,2,2)
plt.hist(df1['width'], edgecolor='k', color='pink')
plt.show()