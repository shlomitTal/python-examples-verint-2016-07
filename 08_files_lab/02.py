#Commited by Shlomit
import sys, itertools

if len(sys.argv) < 4:
    print "error - you didn't add any arguments!"
    sys.exit


with open(sys.argv[1], "r") as fr1:
    with open(sys.argv[2], "r") as fr2:
        with open(sys.argv[3], "w") as fw3:
            for rows in itertools.izip_longest(fr1, fr2):
                for i in rows:
                    if i is not None:
                     fw3.write(i)


