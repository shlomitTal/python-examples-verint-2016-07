#commited by Shlomit

from random import randint

while True:
    num = randint(1, 1000000)
    if (num % 7 == 0 and num % 13 == 0 and num % 15 == 0): break
print "the num:", num, "is divied by 7, 13 and 15"
