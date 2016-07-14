#commited by Shlomit

list = [chr(i) for i in range (97, 123)]
res = [x+y+z for x in list for y in list for z in list]
print res