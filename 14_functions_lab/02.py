#commited by Shlomit

import numbers
def validateTypes(num, st):
    if not isinstance(num, numbers.Number):
        raise Exception("Invalid argument type - num arg is not a number")
    if not isinstance(st, basestring):
        raise Exception("Invalid argument type - st arg is not a string")
    print num , st

#validateTypes(5, "ffgd")