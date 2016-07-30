#commited by Shlomit

import numbers
import sys
import math
def sqrt(n):
    if not isinstance(n, numbers.Number):
        raise ValueError("Invalid argument type - num arg is not a number")
    elif n < 0:
        raise ValueError ("expected parameter > 0, got: %d"% n)

    return math.sqrt(n)


while True:
  #  try:
        num = int(raw_input())
        sqrt(num)
  #  except ValueError as e:
  #     print "failed to calc sqrt. error was %s"% e.message
         

