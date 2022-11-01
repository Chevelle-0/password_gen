import string 
import random

def listtostring(s):
 
    str1 = ""
 
    for ele in s:
        str1 += str(ele)
 
    return str1


length = int(input("How long would you like the password to be"))

lnum = random.randint(3, 7) - 1

count1 = length - lnum

inum = random.randint(3, count1 - 4)

snum = count1 - inum

print("lnum = " + str(lnum))

print("inum = " + str(inum))

print("snum = " + str(snum))

ri = 0

count = 14

passlength = length

letters = list(string.ascii_lowercase)

numbers = [i for i in range(10)]

for i in range(0,9):
        numbers[i] = str(numbers[i])

symbols = ["|", "`", "<", ">", ",", ".", "?", "/", "~", "@", "#", ":", ";", "}", "{", "]", "[", "!", "$", "%", "^", "&", "*", "(", ")", "_", "+", "="]

all = letters + numbers + symbols

print(all)

password = []

for i in range(0,length):
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

