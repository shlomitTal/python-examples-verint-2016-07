#commited by Shlomit

import numbers
def calc(*args):
    sum = 0;
    for i in args:
        if  not isinstance(i, numbers.Number):
            continue
        sum += (abs(i)/ 10) % 10
    return sum


#a = calc(-140,8, 220, 1120, -98,-100)
#print a
          
        