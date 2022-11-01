import string 
import random

def listtostring(s):
 
    str1 = ""
 
    for ele in s:
        str1 += str(ele)
 
    return str1

randormanual = "getouttahere"

while randormanual != "R" and randormanual != "M":
    randormanual = input("Would you like to use random (length: 15) or manual character counts? (R/M)\n")

if randormanual == "R":
    lnum = random.randint(3, 7) - 1

    count1 = 15 - lnum

    inum = random.randint(3, count1 - 4)

    snum = count1 - inum

    print("lnum = " + str(lnum))

    print("inum = " + str(inum))

    print("snum = " + str(snum))

    ri = 0

    count = 14

    passlength = 15

    letters = list(string.ascii_lowercase)

    numbers = [i for i in range(10)]

    for i in range(0,9):
        numbers[i] = str(numbers[i])

    symbols = ["|", "`", "<", ">", ",", ".", "?", "/", "~", "@", "#", ":", ";", "}", "{", "]", "[", "!", "$", "%", "^", "&", "*", "(", ")", "_", "+", "="]

    all = letters + numbers + symbols

    print(all)

    password = []

    for i in range(0,15):
        ri = random.randint(0, count)
        password.append(all[ri])

        if all[ri] in letters:
            lnum = lnum - 1

        if all[ri] in numbers:
            inum = inum - 1

        if all[ri] in symbols:
            snum = snum - 1

        if lnum == 0:
            for i in range(0, 25):
                if letters[i] in all:
                    all.remove(letters[i])

        if inum == 0:
            for i in range(0, 9):
                if numbers[i] in all:
                    all.remove(numbers[i])

        if snum == 0:
            for i in range(0, 27):
                if symbols[i] in all:
                    all.remove(symbols[i])

        del all[ri]
        count = count - 1

    random.shuffle(password)
    print(listtostring(password))
    
if randormanual == "M":

    letters = list(string.ascii_lowercase)

    numbers = [i for i in range(10)]

    for i in range(0,9):
        numbers[i] = str(numbers[i])

    symbols = ["|", "`", "<", ">", ",", ".", "?", "/", "~", "@", "#", ":", ";", "}", "{", "]", "[", "!", "$", "%", "^", "&", "*", "(", ")", "_", "+", "="]

    all = letters + numbers + symbols
    
    lnum = int(input("How many letters?\n"))

    inum = int(input("How many numbers?\n"))

    snum = int(input("How many symbols?\n"))

    print("lnum = " + str(lnum))

    print("inum = " + str(inum))

    print("snum = " + str(snum))

    count = len(all)

    print("count = " + str(count))

    password = []

    while lnum != 0:
        print(count)
        ri = random.randint(0, count)
        if all[ri] in letters:
            password.append(all[ri])
            lnum = lnum - 1
            del all[ri]
            count = count - 1

    while inum != 0:
        print(count)
        ri = random.randint(0, count)
        if all[ri] in numbers:
            password.append(all[ri])
            inum = inum - 1
            del all[ri]
            count = count - 1

    while snum != 0:
        print(count)
        ri = random.randint(0, count)
        if all[ri] in symbols:
            password.append(all[ri])
            snum = snum - 1
            del all[ri]
            count = count - 1
        


    random.shuffle(password)
    print(listtostring(password)) 