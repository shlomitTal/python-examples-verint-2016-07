#commited by Shlomit

from random import randint
x = randint(1, 10)
y = randint(1, 10)

greater = 0
if x > y:
       greater = x
else:
       greater = y

while(True):
    if((greater % x == 0) and (greater % y == 0)):
           break
    greater += 1
print "the least common multiple of the two nums: ",(x,y) ,"is:", greater


