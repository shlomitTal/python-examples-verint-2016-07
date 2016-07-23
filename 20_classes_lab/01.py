#commited by Shlomit
import sys
class Summer(object):
    def __init__(self):
        self.sum = 0

    def add(self, *list):
        for n in list:
            self.sum += int(n)
    def total(self):
        return self.sum

#s = Summer()
#s.add(50, 80)
#print s.total()