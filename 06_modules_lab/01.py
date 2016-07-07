#Commited by Shlomit
import sys
if(len(sys.argv)) < 1:
    print "error - you didn't add any arguments!"
    sys.exit

loopCount = sys.argv[1]

if(loopCount[0] == "-"):
      print "error - you enter a negetive number!"
if(not loopCount.isdigit()):
     print "error - you enter!"
     sys.exit

i = 0
while i < int(loopCount):
    print "Hello Python"
    i+=1

