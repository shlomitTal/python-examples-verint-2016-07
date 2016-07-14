#commited by Shlomit

from collections import defaultdict

def groupby(func, *mylist):
    dict = defaultdict(list)
    for item in mylist:
        dict[func(item)].append(item)
    return dict


#a = groupby(lambda(s): s[0], 'helo', 'hi', 'help', 'bye', 'here')
#print a.items()