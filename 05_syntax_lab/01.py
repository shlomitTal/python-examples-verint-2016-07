#commited by Shlomit

import sys
biggest = -sys.maxint - 1
for i in range(10):
    num = int(raw_input())
    if num > biggest :
        biggest = num

print "biggest number is %d" % biggest
