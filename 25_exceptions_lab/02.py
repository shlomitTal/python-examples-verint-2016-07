import sys
if len(sys.argv) < 2 :
    raise BaseException("dont enter a file as argument!")
try:
    count = 0
    with open(sys.argv[1], "r") as f:
        for line in f:
            count +=1
    print count
except Exception as e:
    print "sory, file %s, not exist"% sys.argv[1]