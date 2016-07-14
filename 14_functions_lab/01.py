#commited by Shlomit
import operator

def mysum(*mylist):
  return  sum([i for i in mylist if type(i)== int])
  
def mymul(*mylist):
   return reduce(operator.mul, [i for i in mylist if type(i)== int])

#sum = mysum(5,7,"jj", 5, "", 10)
#print "sum is: %d" % sum

#sum = mymul(5,7,"jj", 5, "", 10)
#print "mymul is: %d" % sum