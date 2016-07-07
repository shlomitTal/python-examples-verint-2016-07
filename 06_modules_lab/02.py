#Commited by Shlomit
import sys
if(len(sys.argv)) < 3:
    print "error - you didn't add any arguments!"
    sys.exit

arg1 = int(sys.argv[1])
arg2 = int(sys.argv[2])

print "the sum of :",(arg1, arg2), "is:", arg1 + arg2

