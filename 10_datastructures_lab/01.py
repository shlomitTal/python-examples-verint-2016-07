#commited by shlomit
import sys

if len(sys.argv) < 2:
    print "error - you didn't add any arguments!"
    sys.exit

hashKey={}
file = sys.argv[1]
with open(file, "r") as f:
    for line in f:
        fields = line.split("=")
        if len(fields) != 2:
            continue
        hashKey[fields[0]] = fields[1]

print "please write the wanted computer names"

for row in raw_input().split():
    if row in hashKey:
        print "the ip of computer name: "+ row+ " is: "+ hashKey[row]
    else:
         print "error - the computer name: "+ row + " is not exist in the file"