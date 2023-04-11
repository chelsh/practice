#MYA -> ENG

def myaDecoder(text):
    L = []

    for i in range(len(text) // 4):
        L.append(text[4*i : 4*i + 4])

    decodedList = []
    for i in range(len(L)):
        ascii = 0
        for j in range(4):
            if L[i][j] == "ㅁ":
                ascii += 0
            elif L[i][j] == "ㅑ":
                ascii += 1 * 4 ** (3 - j)
            elif L[i][j] == "먀":
                ascii += 2 * 4 ** (3 - j)
            elif L[i][j] == "먐":
                ascii += 3 * 4 ** (3 - j)
        decodedList.append(chr(ascii))

    return ''.join(decodedList)