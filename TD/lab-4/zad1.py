def asciitobin(text):
    tablica = []
    for i in range(len(text)):
        z = ord(text[i])
        while z:
            tablica.append(z & 1)
            z >>= 1
    tablica.reverse()
    return tablica

print(asciitobin('aa'))
