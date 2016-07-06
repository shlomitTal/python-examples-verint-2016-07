#commited by Shlomit

from random import randint
num = randint(1, 10000)
tmpnum = num
digitCount = 0
while num > 0 :
   digitCount += num % 10
   num /= 10
print "the sum of %d number is: %d"% (tmpnum, digitCount)