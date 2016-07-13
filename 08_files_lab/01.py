#Commited by Shlomit
#D:\tmp\t1.txt D:\tmp\t2.txt

import sys
if len(sys.argv) < 3:
    print "error -not enugh args"
    sys.exit

file1 = sys.argv[1]
file2 = sys.argv[2]


with open(file1, "r") as fr:
    with open (file2, "a") as fw:
        for line in fr:
            fw.write(line);
