import random
import string
import math

def listtostring(s):

  str1 = ""

  for ele in s:
    str1 += str(ele)

  return str1


password = []
num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
let = list(string.ascii_lowercase)
sym = [
  "|", "`", "<", ">", ",", ".", "?", "/", "~", "@", "#", ":", ";", "}", "{",
  "]", "[", "!", "$", "%", "^", "&", "*", "(", ")", "_", "+", "="
]

print("Enter a password length of 9+")
length = int(input("Length: "))

while length < 9:
  print("Try again\n")
  print("Lemgth: ")
  length = int(input())
length = length + 1
snum = random.randint(int(length * 0.33 - 1.0), int(length * 0.33))
snum = int(snum)
inum = length - snum - length / 3
lnum = length - snum - inum

lnum = int(lnum)
inum = math.floor(inum)

random.shuffle(let)
random.shuffle(sym)
random.shuffle(num)

while snum != 0:
  password.append(sym[snum])
  snum = snum - 1

while inum != 0:
  password.append(num[inum])
  inum = inum - 1

while lnum != 0:
  password.append(let[lnum])
  lnum = lnum - 1

random.shuffle(password)
random.shuffle(password)
random.shuffle(password)

passw = listtostring(password)

print("Password: " + passw)
