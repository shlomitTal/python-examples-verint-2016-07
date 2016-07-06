#commited by Shlomit

from random import randint

def ReadNumsAndCompare():
    num = randint(1, 100)
    print "try to guess a number:"
    guess = int(raw_input())
    if(num > guess):
       return 1
    elif num < guess:
       return -1
    else:
        return 0
      
def DoMistake():
    x = randint(1, 100)
    if x % 7 == 0: 
        return True
    else:
        return False

def mainfunc():
    while True:
        num = ReadNumsAndCompare()
        mistake =DoMistake()
        if((num == 1 and not mistake) or (num == -1 and  mistake) or (num == 0 and  mistake)):
            print "too small, try again"
        elif((num == 1 and  mistake) or (num == -1 and not mistake)):
            print "too big, try again"
        else:
             print "equal!!"
             break

mainfunc()