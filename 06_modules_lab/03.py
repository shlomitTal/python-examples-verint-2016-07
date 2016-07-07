#Commited by Shlomit
import sys
import os

if(len(sys.argv)) < 3:
    print "error - you didn't add  arguments!"
    sys.exit

path = sys.argv[1]
if not os.path.isdir(path):
    print "Invalid folder"
    sys.exit() 


size = sys.argv[2]
if(not size.isdigit()):
    print "error - second arg is not a number"
    sys.exit

intsize= int(size) * 1024 *1024
for root, dirs,files in os.walk(path):
    for name in files:
        fullFilePathName = os.path.join (root,name)
        statinfo = os.stat(fullFilePathName)
        if(statinfo.st_size > intsize):
            print "file:"+ name +"is  bigger then:%", sys.argv[2], "mega"
            shouldRemove = raw_input("do you want to remove the file:"+ name +"? please enter Yes Or No\n")
            if(shouldRemove[0].lower() == 'y'):
                os.remove(fullFilePathName)
            
