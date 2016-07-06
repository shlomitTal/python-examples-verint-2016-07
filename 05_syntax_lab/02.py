#commited by Shlomit

from random import randint
sum = 0
for i in range(7) :
    sum += randint(1,100)

print "sum is %d"% sum
if sum %7 == 0 : print "Boom"