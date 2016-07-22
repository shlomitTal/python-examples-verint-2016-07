#commited by shlomit
import sys
import re
if len(sys.argv) < 3: 
    sys.exit("error - you didn't add any arguments!")

regex= sys.argv[2] + '[ ]*=[ ]*(.*)'

file = sys.argv[1]
with open(file, "r") as f:
    for line in f:
        res = re.search(regex,line)
        if res is not None:
            print res.group(1)