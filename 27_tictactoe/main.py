#commited by shlomit
import sys
from pprint import pprint
from random import randint

class player:
    def __init__(self, _uniqe):
        self.uniqe=_uniqe
        self.count=0

class Board:
    def __init__(self):
        self.mat= [['*','*','*'],['*','*','*'],['*','*','*']]

    def printAll(self):
        pprint(self.mat)

    def Play(self, _player, row, column):
        if self.mat[row][column] is not '*':
            raise AttributeError("square [%d][%d] is taken"% (row, column) )
        else:
            self.mat[row][column]= _player.uniqe
            _player.count += 1

    def checkWinner(self, uniqeChar):
       if ((uniqeChar == self.mat[0][0] == self.mat[0][1] == self.mat[0][2]) or
           (uniqeChar == self.mat[1][0] == self.mat[1][1] == self.mat[1][2]) or
           (uniqeChar == self.mat[2][0] == self.mat[2][1] == self.mat[2][2]) or
           (uniqeChar == self.mat[0][0] == self.mat[1][0] == self.mat[2][0]) or
           (uniqeChar == self.mat[0][1] == self.mat[1][1] == self.mat[2][1]) or
           (uniqeChar == self.mat[0][2] == self.mat[1][2] == self.mat[2][2]) or
           (uniqeChar == self.mat[0][0] == self.mat[1][1] == self.mat[2][2]) or
           (uniqeChar == self.mat[0][2] == self.mat[1][1] == self.mat[2][0])):
           return 1
       else:
           return 0


play1=player('X')
play2=player('0')
indxTurn = 0
b=Board()
b.printAll()
while True:
    val = b.checkWinner('*')

    if indxTurn % 2 == 0:
        currplayer = play1
    else:
        currplayer = play2

    indxTurn +=1

    row = randint(0,2)
    column = randint(0,2)
    b.Play(currplayer, row, column)
    print str(play1.count) + " "+ str(play2.count)
    b.printAll()
    if b.checkWinner(currplayer.uniqe):
        print "there is a winner! the winner is Player %S" +currplayer.uniqe
        break