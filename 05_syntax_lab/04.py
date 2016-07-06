#commited by Shlomit

line =raw_input()
st=""
while len(line) > 0:
    st = line + "\n" + st
    line =raw_input()

print "the opposite sting is:\n", st

