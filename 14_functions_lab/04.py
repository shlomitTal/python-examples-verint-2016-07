#commited by Shlomit
import numbers
list=[]
def longer_than(num, *args):
    if not isinstance(num, numbers.Integral):
        raise Exception("not send a number")
    for i in args:
        if not isinstance(i, basestring):
            continue
        if len(i) > num:
            list.append(i)
    return list

#print longer_than(5, "hhh", "gggggggg", "h", "ttttttttt")
