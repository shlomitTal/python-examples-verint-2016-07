#commited by Shlomit
import sys
from collections import defaultdict

if len(sys.argv) < 2:
    print "error - you didn't add any arguments!"
    sys.exit
file = sys.argv[1]
hashmap=defaultdict(str)

with open(file, "r") as f:
    for row in f:
       rowVal = row[:-1] if row.endswith("\n") else row            
       sortedRow = "".join([i for i in sorted(rowVal)])
       hashmap[sortedRow] += rowVal + " " 
    
for row in hashmap:
    print (hashmap[row])[:-1]
   