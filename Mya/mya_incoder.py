#ENG -> MYA

def myaIncoder(text):
    L = []

    for i in range(len(text)):
        L.append(ord(text[i]))

    incodedList = []
    for i in range(len(L)):
        quatre = 0
        for j in range(3, -1, -1):
            quatre += (L[i] // (4 ** j)) * (10 ** j)
            L[i] %= 4 ** j
            
        quatre = str(quatre)
        quatre = quatre.zfill(4)

        myaStr = ""
        for j in range(4):
            if quatre[j] == '0':
                myaStr += "ㅁ"
            elif quatre[j] == '1':
                myaStr += "ㅑ"
            elif quatre[j] == '2':
                myaStr += "먀"
            elif quatre[j] == '3':
                myaStr += "먐"
        
       
        incodedList.append(myaStr)
    return ''.join(incodedList)

