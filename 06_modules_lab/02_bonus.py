#Commited by Shlomit
import sys
if(len(sys.argv)) < 3:
    print "error - you didn't add any arguments!"
    sys.exit

arg1 = (sys.argv[1]).lstrip("-+")
arg2 = (sys.argv[2]).lstrip("-+")

if(not arg1.isdigit() or not arg2.isdigit()):
     print "error - you dont enter a number!"
     sys.exit

print "the sum of :",(arg1, arg2), "is:", int(arg1) + int(arg2)