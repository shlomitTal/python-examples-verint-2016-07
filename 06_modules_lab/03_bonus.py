#Commited by Shlomit
import sys
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("path")
parser.add_argument("size",type=int)
args = parser.parse_args()


path = args.path
if not os.path.isdir(path):
    print "Invalid folder"
    sys.exit() 

size = args.size

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
            
